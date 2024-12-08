from collections import defaultdict

map = []
i = 0
coords = defaultdict(list)
with open("input.txt", "r") as file:
    for line in file.readlines():
        map.append([])
        j = 0
        for c in line.strip():
            map[i].append(c)
            if c != '.':
                coords[c].append((i,j))
            j = j + 1
        i = i + 1

n_map = len(map)
m_map = len(map[0])

def is_in_border(pos):
    i = pos[0]
    j = pos[1]
    return 0 <= i < n_map and 0 <= j < m_map

total_nodes = 0 
simple_antinode_position = set()
harmonic_antinode_position = set()

def add_antinode(antinode, pos_set):
    global total_nodes
    if is_in_border(antinode):
        if (antinode[0], antinode[1]) not in pos_set:
            total_nodes = total_nodes + 1
            pos_set.add((antinode[0], antinode[1]))
            #map[antinode[0]][antinode[1]] = '#'

for letter in coords.keys():
    n = len(coords[letter])
    for i in range(n):
        first_coord = coords[letter][i]
        for j in range(i+1, n):
            second_coord = coords[letter][j]
            x_dif = first_coord[0] - second_coord[0]
            y_dif = first_coord[1] - second_coord[1]


            if y_dif < 0:
                first_antinode = first_coord[0] + x_dif, first_coord[1] + y_dif
                second_antinode = second_coord[0] + abs(x_dif), second_coord[1] + abs(y_dif)
            
            else:
                first_antinode = first_coord[0] + x_dif, first_coord[1] + y_dif
                second_antinode = second_coord[0] + abs(x_dif), second_coord[1] - y_dif
            
                      
            add_antinode(first_antinode, simple_antinode_position)            
            add_antinode(second_antinode, simple_antinode_position)


for letter in coords.keys():
    n = len(coords[letter])
    for i in range(n):
        first_coord = coords[letter][i]
        for j in range(i+1, n):
            second_coord = coords[letter][j]
            x_dif = first_coord[0] - second_coord[0]
            y_dif = first_coord[1] - second_coord[1]

            
            init_new_antinode = first_coord[0] + x_dif, first_coord[1] + y_dif

            new_antinode = init_new_antinode

            while is_in_border(new_antinode):
                add_antinode(new_antinode, harmonic_antinode_position)
                new_antinode = new_antinode[0] + x_dif, new_antinode[1] + y_dif
                
            new_antinode = init_new_antinode

            while is_in_border(new_antinode):
                add_antinode(new_antinode, harmonic_antinode_position)
                new_antinode = new_antinode[0] - x_dif, new_antinode[1] - y_dif
            
            init_new_antinode = second_coord[0] + x_dif, second_coord[1] + y_dif

            new_antinode = init_new_antinode

            while is_in_border(new_antinode):
                add_antinode(new_antinode, harmonic_antinode_position)
                new_antinode = new_antinode[0] + x_dif, new_antinode[1] + y_dif
                
            new_antinode = init_new_antinode

            while is_in_border(new_antinode):
                add_antinode(new_antinode, harmonic_antinode_position)
                new_antinode = new_antinode[0] - x_dif, new_antinode[1] - y_dif



print(len(simple_antinode_position))
print(len(harmonic_antinode_position))

