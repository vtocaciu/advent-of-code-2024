map = []
walls = set()
with open("input.txt", "r") as file:
   start_pos = None
   end_pos = None
   i = 0
   
   for line in file.readlines():
        j = 0
        map.append([])
        for c in line:
            if c == "#":
                map[i].append('#')
                walls.add((i,j))
            if c == "S":
                start_pos = (i,j)
                map[i].append("v") 
            if c == "E":
                map[i].append(c)
                end_pos = (i,j)
            if c == ".":
                map[i].append('.')
            j = j + 1
        i = i + 1
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

def get_orientation(dir):
    if dir == (-1, 0):
        return "^"
    if dir == (0, 1):
        return ">"
    if dir == (1, 0):
        return "v"
    if dir == (0, -1):
        return "<"

import heapq

def dijkstra(walls, start, end):
    dirs = [(-1, 0), (0, -1), (0, 1), (1, 0)]

    pq = [(0, start, map[start_pos[0]][start_pos[1]], [])]  # priority queue: (current score, position, orientation, path)
    heapq.heapify(pq)
    scores = {start: 0}
    visited = set()

    while pq:
        score, current_pos, move, path = heapq.heappop(pq)

        if current_pos in visited:
            continue
        visited.add(current_pos)

        if current_pos == end:
            return score, path

        for dir in dirs:
            next_pos = (current_pos[0] + dir[0], current_pos[1] + dir[1])

            if (next_pos[0], next_pos[1]) in walls:
                continue
            
            way = get_way(move)
            if way == dir:
                next_score = score + 1
            else:
                next_score = score + 1001
            
            if next_pos not in scores or next_score < scores[next_pos]:
                scores[next_pos] = next_score
                heapq.heappush(pq, (next_score, next_pos, get_orientation(dir), path + [next_pos]))

    
    return -1, None





# for i in range(len(map)):
#     line = ""
#     for j in range(len(map[0])):
#         if (i,j) in walls:
#             line = f"{line}#"
#         elif (i,j) in paths:
#             line = f"{line}0"
#         elif (i,j) in [start_pos, end_pos]:
#             line = f"{line}X"
#         else:
#             line = f"{line}."
#     print(line)
        

print(dijkstra(walls, start_pos, end_pos))