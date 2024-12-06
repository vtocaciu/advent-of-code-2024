map = []

with open("input.txt", "r") as file:
   guard_pos = None
   i = 0
   
   for line in file.readlines():
        j = 0
        map.append([])
        for c in line:
            if c == ".":
                map[i].append(0)
            if c == "#":
                map[i].append(-1)
            if c in "v><^":
                map[i].append(c)
                guard_pos = (i,j)
            j = j + 1
        i = i + 1

n = len(map)
m = len(map[0])

fake_map = []
for line in map[:]:
    fake_map.append(line[:])

def turn_right(guard):
    if guard == "^":
        return ">"
    if guard == ">":
        return "v"
    if guard == "v":
        return "<"
    return "^"

def is_in_border(i, j):
    return 0 <= i < n and 0 <= j < m

def get_way(guard):
    if guard == "^":
        return -1, 0
    if guard == ">":
        return 0, 1
    if guard == "v":
        return 1, 0
    return 0, -1


current_pos = guard_pos
guard = map[current_pos[0]][current_pos[1]]
map [current_pos[0]][current_pos[1]] = 'X'

obstructions = 0
rect = []


corners = []
right_turns = 0

def fake_place_border(i,j):
    init_map = fake_map[i][j]
    fake_map[i][j] = -1
    visited = set()
    loop = False
    x, y = guard_pos
    nguard = fake_map[x][y]
    while is_in_border(x, y):
        key = f"{x},{y},{nguard}"
        if key in visited:
            loop = True
            break
        visited.add(key)
        dirX, dirY = get_way(nguard)
        if is_in_border(x+dirX, y+dirY) and fake_map[x+dirX][y+dirY] == -1:
            nguard = turn_right(nguard)
        else:
            x,y = x+dirX, y+dirY
    fake_map[i][j] = init_map
    return loop


while is_in_border(current_pos[0], current_pos[1]):
    dirX, dirY = get_way(guard)
    x, y = current_pos

    if is_in_border(x+dirX, y+dirY) and map[x+dirX][y+dirY] == -1:
        guard = turn_right(guard)
            
    else:
        if is_in_border(x+dirX, y+dirY):
            map[x+dirX][y+dirY] = 'X'
        current_pos = x+dirX, y+dirY


steps = 0
for line in map:
    steps = steps + sum([1 for p in line if p == 'X'])


# fuck it
for x in range(n):
    for y in range(m):
        if (x,y)!= guard_pos and fake_place_border(x,y):
            obstructions = obstructions + 1

print(steps, obstructions)