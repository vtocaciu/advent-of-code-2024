map = []
movements = ""
boxes = set()
walls = set()
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
                    walls.add((i,j))
                if c == "@":
                    guard_pos = (i,j)
                    map[i].append("@")
                if c == "O":
                    map[i].append(c)
                    boxes.add ((i,j))
                if c == ".":
                    map[i].append('.')
                j = j + 1
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

for move in movements:
    dir = get_way(move)
    next_pos = guard_pos[0] + dir[0], guard_pos[1] + dir[1]
    if next_pos not in walls and next_pos not in boxes:
        guard_pos = next_pos
        continue
    if next_pos in boxes:
        next_box_pos = next_pos[0] + dir[0], next_pos[1] + dir[1]
        while next_box_pos in boxes:
            next_box_pos = next_box_pos[0] + dir[0], next_box_pos[1] + dir[1]
        if next_box_pos in walls:
            continue
        else:
            map[next_box_pos[0]][next_box_pos[1]] = "0"
            map[next_pos[0]][next_pos[1]] = "."
            boxes.add(next_box_pos)
            boxes.remove(next_pos)
            guard_pos = next_pos

map[guard_pos[0]][guard_pos[1]] = "@"
for line in map:
    print(line)

sum = 0
for box in boxes:
    sum = sum + box[0]*100+box[1]
print(sum)