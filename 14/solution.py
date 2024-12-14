lines = []

with open("input.txt", "r") as file:
    text = file.read()
    for line in text.split("\n"):
        lines.append(line)
    
robots = []
for rob in lines:
    pos, vel = None, None
    for e in rob.split(" "):
        if e.startswith("p="):
            e = e[2:]
            x, y = e.split(",")
            x = int(x)
            y = int(y)
            pos = (x, y)
        elif e.startswith("v="):
            e = e[2:]
            x, y = e.split(",")
            x = int(x)
            y = int(y)
            vel = (x, y)
       
    robots.append((pos, vel))

map = []
i = 0
width = 101
height = 103

def init_map():
    i=0
    global map
    map = []
    for _ in range(height):
        map.append([])
        for _ in range(width):
            map[i].append(".")
        i = i + 1

def print_map():
    for line in map:
        print("".join([str(l) for l in line]))


def get_quandrant(x,y):
    mid_width = width // 2 
    mid_height = height // 2

    if y == mid_height or x == mid_width:
        return None
    
    if x < mid_width and y < mid_height:
        return 1

    if x > mid_width and y < mid_height:
        return 2

    if x < mid_width and y > mid_height:
        return 3

    if x > mid_width and y > mid_height:
        return 4

from collections import defaultdict
quandrants = defaultdict(int)

for robot in robots:
    pos, velocity = robot
    seconds = 100
    new_pos = (pos[0] + velocity[0] * seconds) % width, (pos[1] + velocity[1] * seconds) % height

    quandrant = get_quandrant(new_pos[0], new_pos[1])
    if quandrant:
        quandrants[quandrant] += 1


p = 1
for _, val in quandrants.items():
    p = p * val
print(quandrants)
print(p)

second = 0
no_unique_pos = True

robot_dict = {}

positions = set()
for i, robot in enumerate(robots):
    robot_dict[i] = {"pos": robot[0], "velocity": robot[1]}
    if robot[0] in positions:
        no_unique_pos = False
    positions.add(robot[0])

seconds = 0
while not no_unique_pos:
    no_unique_pos = True
    positions = set()
    init_map()
    for i in robot_dict.keys():
        pos = robot_dict[i]["pos"]
        velocity = robot_dict[i]["velocity"]
        new_pos = (pos[0] + velocity[0]) % width, (pos[1] + velocity[1]) % height
        if new_pos in positions:
            no_unique_pos = False
        positions.add(new_pos)
        robot_dict[i]["pos"] = new_pos
        map[new_pos[1]][new_pos[0]] = "1"
    if no_unique_pos:
        print_map()
    seconds = seconds + 1

print(seconds)