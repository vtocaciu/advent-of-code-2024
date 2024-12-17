map = []
i = 0

with open("input.txt", "r") as file:
    for line in file.readlines():
        map.append([])
        j = 0
        for c in line.strip():
            map[i].append(c)
            j = j + 1
        i = i + 1

n = len(map)
m = len(map[0])


def is_in_border(x, y):
    return 0 <= x < n and 0 <= y < m

def dfs(pos):
    visited = set()
    queue = [pos]
    while queue:
        i,j = queue.pop()
        visited.add((i,j))
        value = map[i][j]
        for nextI, nextJ in [(i-1,j),(i+1, j), (i, j-1), (i, j+1)]:
            if is_in_border(nextI,nextJ) and (nextI, nextJ) not in visited and map[nextI][nextJ] == value:
                queue.append((nextI,nextJ))
    return visited


pos_visited = set()
islands = {}
total_islands = 0
for i in range(n):
    for j in range(m):  
        if (i,j) in pos_visited: 
            continue

        visited = dfs((i,j))
        total_islands = total_islands + 1
        islands[(total_islands, map[i][j])] = visited
        pos_visited = pos_visited.union(visited)


print(total_islands)

areas = {}
first_sum = 0
for tag, positions in islands.items():
    id, island = tag
    area = len(positions)
    areas[tag] = area
    perimeter = 0
    for pos in positions:
        i, j = pos
        pos_perimeter = 0
        for nextI, nextJ in [(i-1,j),(i+1, j), (i, j-1), (i, j+1)]:        
            if not is_in_border(nextI, nextJ):
                pos_perimeter = pos_perimeter + 1
            elif (nextI, nextJ) not in positions:
                pos_perimeter = pos_perimeter + 1
        perimeter = perimeter + pos_perimeter
    first_sum = first_sum + area * perimeter
print(first_sum)


corners = {}


for tag, positions in islands.items():
    left_up =  set()
    left_down = set()
    right_up = set()
    right_down = set()
    for pos in positions:
        row, col = pos
        if (row-1, col) not in positions and (row, col-1) not in positions: # up and left corner
            left_up.add((row,col))

        if (row+1, col) not in positions and (row, col+1) not in positions: # down and right corner
            right_down.add((row, col))

        if (row-1, col) not in positions and (row, col+1) not in positions: # up and right corner
            right_up.add((row,col))

        if (row+1, col) not in positions and (row, col-1) not in positions: # down and left corner
            left_down.add((row,col))

        if (row, col+1) not in positions and is_in_border(row-1, col+1) and (row-1, col+1) in positions:
            right_up.add((row,col))
        

        if (row, col+1) not in positions and is_in_border(row+1, col+1) and (row+1, col+1) in positions:
            right_down.add((row,col))
    

        if (row, col-1) not in positions and is_in_border(row-1, col-1) and (row-1, col-1) in positions:
            left_up.add((row,col))
        

        if (row, col-1) not in positions and is_in_border(row+1, col-1) and (row+1, col-1) in positions:
            left_down.add((row,col))
    corners[tag] = len(left_up) + len(left_down) + len(right_down) + len(right_up)

# print("LEFT_UP", left_up)
# print("LEFT_DOWN", left_down)
# print("RIGHT_UP", right_up)
# print("RIGHT_DOWN", right_down)


# print(corners)

second_sum = 0
for id in corners.keys():
    second_sum = second_sum + areas[id]*corners[id]

print(second_sum)