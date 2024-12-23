from collections import defaultdict

connections = defaultdict(set)
start_with_t = set()
networks = set()

with open("input.txt", "r") as file:
    for line in file.readlines():
        first = line.split("-")[0].strip()
        second = line.split("-")[1].strip()
        connections[first].add(second)
        connections[second].add(first)

        networks.add(first)
        networks.add(second)

        if first[0] == "t":
            start_with_t.add(first)
        if second[0] == "t":
            start_with_t.add(second)

networks = list(networks)
lans = set()

for first in start_with_t:
    for second in connections[first]:
        for third in connections[second]:
            if first in connections[third]:
                new_lan = [first, second, third]
                new_lan.sort()
                new_lan = tuple(new_lan)
                if new_lan not in lans:
                    lans.add(new_lan)

print(len(lans))


from copy import deepcopy

largest_set = set()

def check(current_set, network):
    if len(current_set) == 0:
        return True
    if len(connections[network].intersection(current_set))  == len(current_set):
        return True

    return False


def find_largest_set(current_set, idx):
    global largest_set
    if idx >= len(networks):
        return
    if len(largest_set) < len(current_set):
        largest_set = deepcopy(current_set)
    
    find_largest_set(current_set, idx+1)

    if check(current_set, networks[idx]):
        current_set.add(networks[idx])
        find_largest_set(current_set, idx+1)
        current_set.remove(networks[idx])

find_largest_set(set(), 0)

largest_set = list(largest_set)
largest_set.sort()
print(",".join(largest_set))