map = []
i = 0
start_pos = set()
with open("input.txt", "r") as file:
    for line in file.readlines():
        map.append([])
        j = 0
        for c in line.strip():
            map[i].append(int(c))
            if int(c) == 0:
                start_pos.add((i,j))
            j = j + 1
        i = i + 1

n = len(map)
m = len(map[0])


def is_in_border(x, y):
    return 0 <= x < n and 0 <= y < m

def dfs(pos):
    visited = set()
    queue = [pos]
    total_end = 0
    while queue:
        i,j = queue.pop()
        visited.add((i,j))
        value = map[i][j]
        if value == 9:
            total_end = total_end + 1
        else:
            for nextI, nextJ in [(i-1,j),(i+1, j), (i, j-1), (i, j+1)]:
                if is_in_border(nextI,nextJ) and (nextI, nextJ) not in visited and map[nextI][nextJ] == value+1:
                    queue.append((nextI,nextJ))
    return total_end

def bfs(pos):
    visited = set()
    queue = [pos]
    total_end = 0
    while queue:
        i,j = queue.pop(0)
        visited.add((i,j))
        value = map[i][j]
        if value == 9:
            total_end = total_end + 1
        else:
            for nextI, nextJ in [(i-1,j),(i+1, j), (i, j-1), (i, j+1)]:
                if is_in_border(nextI,nextJ) and (nextI, nextJ) not in visited and map[nextI][nextJ] == value+1:
                    queue.append((nextI,nextJ))
    return total_end

total_end = 0
for pos in start_pos:
    total_end = total_end + dfs(pos)

print(total_end)

total_end = 0
for pos in start_pos:
    total_end = total_end + bfs(pos)

print(total_end)

