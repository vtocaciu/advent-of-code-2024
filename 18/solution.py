import heapq

def dijkstra(walls, n, m, start, end):
    dirs = [(-1, 0), (0, -1), (0, 1), (1, 0)]

    pq = [(0, start, [])]  # priority queue: (current cost, position)
    heapq.heapify(pq)
    costs = {start: 0} 
    visited = set()

    while pq:
        current_cost, current_pos, path = heapq.heappop(pq)

        if current_pos in visited:
            continue
        visited.add(current_pos)

        if current_pos == end:
            return current_cost, path

        for dir in dirs:
            next_pos = (current_pos[0] + dir[0], current_pos[1] + dir[1])

            if not (0 <= next_pos[0] < n and 0 <= next_pos[1] < m):
                continue
            if (next_pos[0],next_pos[1]) in walls:
                continue

            
            next_cost = current_cost + 1  

            if next_pos not in costs or next_cost < costs[next_pos]:
                costs[next_pos] = next_cost
                heapq.heappush(pq, (next_cost, next_pos, path + [next_pos]))

    
    return -1, None  # no more path

bytes = []
file_name = "input.txt"
with open(file_name, "r") as file:
    for line in file.readlines():
        bytes.append((int(line.split(",")[1]), int(line.split(",")[0])))

small = file_name == "small_input.txt"
if not small:
    n = 71
    m = 71
    kb = 1024

else:
    n = 7
    m = 7
    kb = 12

start = (0, 0)
end = (n-1, m-1)
walls = set(bytes[:kb])

steps, path = dijkstra(walls, n, m, start, end)
print(steps)
path = set(path)
for byte in bytes[kb+1:]:
    walls.add(byte)
    if byte in path:
        steps, path = dijkstra(walls, n, m, start, end)
        if steps == -1:
            print("done", byte[1], byte[0]) # x, y order
            break