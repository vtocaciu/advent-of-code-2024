with open("input.txt", "r") as file:
    disk_map = file.read().strip()

id = 0
ids = {}
expanded_disk_map = []
expanded_disk_map_blocks = []
for i, space in enumerate(disk_map):
    if i % 2 == 0:
        ids[id] = (int(space), len(expanded_disk_map))
        expanded_disk_map = expanded_disk_map + [str(id) for _ in range(int(space))]
        id = id + 1
    else:
        expanded_disk_map = expanded_disk_map + ["." for _ in range(int(space))]

expanded_disk_map_blocks = expanded_disk_map[:]

def get_next_available_space(i, disk_map):
    while disk_map[i] != '.':
        i = i+1
    return i

def get_next_memory(i, disk_map):
    while disk_map[i] == '.':
        i = i - 1
    return i


start = get_next_available_space(0, expanded_disk_map)
end = get_next_memory(len(expanded_disk_map)-1, expanded_disk_map)
while start < end:
    expanded_disk_map[start] = expanded_disk_map[end]
    expanded_disk_map[end] = "."
    end = get_next_memory(end-1, expanded_disk_map)
    start = get_next_available_space(start, expanded_disk_map)

checksum = 0
for i, num in enumerate(expanded_disk_map):
    if num != '.':
        checksum = checksum + i*int(num)
    else:
        break

print(checksum)

def move(start_id, id, units, remove_id, disk_map):
    for i in range(start_id, start_id+units):
        disk_map[i] = str(id)
    
    for i in range(remove_id, remove_id+units):
        disk_map[i] = "."


def all_dots(disk_map):
    for val in disk_map:
        if val != ".":
            return False
    return True

start = get_next_available_space(0, expanded_disk_map_blocks)
current_id = id - 1
while current_id > 0:
    end = ids[current_id][0]
    while start < ids[current_id][1]:
        if all_dots(expanded_disk_map_blocks[start:start+end]):
            move(start, current_id, end, ids[current_id][1], expanded_disk_map_blocks)
            break
        start = get_next_available_space(start+1, expanded_disk_map_blocks)
    current_id = current_id - 1
    start = get_next_available_space(0, expanded_disk_map_blocks)

checksum = 0
for i, num in enumerate(expanded_disk_map_blocks):
    if num != '.':
        checksum = checksum + i*int(num)


print(checksum)
