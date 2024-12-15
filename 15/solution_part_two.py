map = []
movements = ""

with open("input.txt", "r") as file:
   guard_pos = None
   i = 0

   is_movements = False
   
   for line in file.readlines():
        if line == "\n":
            is_movements = True
            continue
        if not is_movements:
            j = 0
            map.append([])
            for c in line:
                if c == "#":
                    map[i].append('#')
                    map[i].append('#')
                if c == "@":
                    guard_pos = (i,j)
                    map[i].append("@")
                    map[i].append(".")
                if c == "O":
                    map[i].append("[")
                    map[i].append("]")
                if c == ".":
                    map[i].append('.')
                    map[i].append('.')
                j = j + 2
            i = i + 1
        else:
            movements = f"{movements}{line.strip()}"

n = len(map)
m = len(map[0])

def get_way(move):
    if move == "^":
        return -1, 0
    if move == ">":
        return 0, 1
    if move == "v":
        return 1, 0
    return 0, -1


map[guard_pos[0]][guard_pos[1]] = "."

def print_map(pos):
    map[pos[0]][pos[1]] = "@"
    for line in map:
        print("".join(line))
    map[pos[0]][pos[1]] = "."
    print("")

# print("Initial")
# print_map(guard_pos)

def get_value(pos):
    return map[pos[0]][pos[1]]

# print("INITIAL")
# print_map(guard_pos)

from collections import defaultdict

for i, move in enumerate(movements):
    dir = get_way(move)
    next_pos = guard_pos[0] + dir[0], guard_pos[1] + dir[1]
    if get_value(next_pos) == ".":
        # print(move, "moved fara probleme")
        # print_map(guard_pos)
        guard_pos = next_pos   
    elif get_value(next_pos) == "#":
        # print(move, "didn't move")
        # print_map(guard_pos)
        continue
    else: # it's a box
        if move in "^v":
            other_box_pos = (next_pos[0], next_pos[1]+1) if get_value(next_pos) == "[" else (next_pos[0], next_pos[1]-1)

            next_box_pos = next_pos
            next_other_box_pos = other_box_pos
            coord_boxes = defaultdict(set)
            coord_boxes[next_box_pos[0]].add(next_pos[1])
            coord_boxes[next_box_pos[0]].add(other_box_pos[1])
            boxes = [next_pos, other_box_pos]
            wall = False
            empty = False
            while not (wall or empty):
                next_line = next_box_pos[0] + dir[0]
                empty = True
                for coord in coord_boxes[next_box_pos[0]]:
                    if get_value((next_line, coord)) == "[":
                        empty = False
                        coord_boxes[next_line].add(coord)
                        coord_boxes[next_line].add(coord+1)
                    if get_value((next_line, coord)) == "]":
                        empty = False
                        coord_boxes[next_line].add(coord)
                        coord_boxes[next_line].add(coord-1)
                    if get_value((next_line, coord)) == "#":
                        empty = False
                        wall = True
                next_box_pos = next_box_pos[0] + dir[0], next_box_pos[1]
            
            if wall:
                # print(move, "didnt move, cant happen, blocking wall")
                # print_map(guard_pos)
                continue
            if empty:
                # print(coord_boxes, next_line)
                while next_line-dir[0] in coord_boxes.keys():
                    coords = coord_boxes[next_line-dir[0]]
                    for coord in coords:
                        map[next_line][coord] = map[next_line-dir[0]][coord]
                        map[next_line-dir[0]][coord] = "."
                    next_line = next_line - dir[0]
                # print(move, "can happen if you do it")
                # print_map(guard_pos)
                guard_pos = next_pos
                continue

        elif move in "<>":
            next_box_pos = next_pos
            while get_value(next_box_pos) in "[]":
                next_box_pos = next_box_pos[0] + dir[0], next_box_pos[1] + dir[1]
            
            if get_value(next_box_pos) != ".":
                # print(move, "didnt move left/right, something")
                # print_map(guard_pos)
                continue

            moving = next_box_pos
            while moving != next_pos:
                map[moving[0]][moving[1]] = map[moving[0]][moving[1]-dir[1]] 
                moving = moving[0], moving[1]-dir[1]
        
            map[next_pos[0]][next_pos[1]] = "."
            guard_pos = next_pos
            # print(move, "moved left right, fara probleme")
            # print_map(guard_pos)

sum = 0
for i in range(1,n):
    for j in range(1,m):
        if map[i][j] == "[":
            sum = sum + 100 * i + j 

print("Final")    
print_map(guard_pos)
print(sum)
