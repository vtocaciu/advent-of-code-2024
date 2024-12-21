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
                map[i].append(".") 
            if c == "E":
                map[i].append(c)
                end_pos = (i,j)
            if c == ".":
                map[i].append('.')
            j = j + 1
        i = i + 1
n = len(map)
m = len(map[0])

import heapq

def dijkstra(walls, cheats, start, end):
    dirs = [(-1, 0), (0, -1), (0, 1), (1, 0)]

    pq = [(0, start)]  # priority queue: (current score, position,)
    heapq.heapify(pq)
    scores = {start: 0}
    visited = set()
    all_possible_cheats = set()
    walls_to_remove = set()

    while pq:
        score, current_pos = heapq.heappop(pq)

        if current_pos in visited:
            continue
        visited.add(current_pos)

        if current_pos == end:
            if not cheats:
                return score, all_possible_cheats
            return score

        for dir in dirs:
            next_pos = (current_pos[0] + dir[0], current_pos[1] + dir[1])

            if not cheats and (next_pos[0], next_pos[1]) in walls:
                if  (next_pos[0], next_pos[1]) not in walls_to_remove and 1 <= next_pos[0] < n-1 and 1 <= next_pos[1] < m-1:
                    all_possible_cheats.add(((current_pos[0], current_pos[1]), (next_pos[0], next_pos[1])))
                    walls_to_remove.add((next_pos[0], next_pos[1]))

            if (next_pos[0], next_pos[1]) in walls and (next_pos[0], next_pos[1]) not in cheats:
                continue
            
            if next_pos not in scores or score+1 < scores[next_pos]:
                scores[next_pos] = score+1
                heapq.heappush(pq, (score+1, next_pos))

    
    return -1
        
count = 0
initial, cheats = dijkstra(walls, [], start_pos, end_pos)

from collections import defaultdict
saved = defaultdict(int)
for cheat in cheats:
    other = dijkstra(walls, cheat, start_pos, end_pos)
    if other < initial:
        saved[initial - other] += 1
    if other != -1 and initial - other >= 100:
        count = count + 1

print(count)
