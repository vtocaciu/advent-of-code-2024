patterns = set()
new_designs = []
from collections import defaultdict
startswith = defaultdict(list)
with open("input.txt", "r") as file:
    patterns = set([pattern.strip() for pattern in file.readline().split(", ")])

    for pattern in patterns:
        startswith[pattern[0]].append(pattern)

    file.readline()
    for design in file.readlines():
        new_designs.append(design.strip())

from functools import lru_cache
@lru_cache(maxsize=1024)
def solve(design):
    if design == "":
        return True

    if design in patterns:
        return True

    for pattern in startswith[design[0]]:
        i = 0
        j = 0
        while i < len(pattern) and j < len(design) and design[j] == pattern[i]:
            i = i + 1
            j = j + 1
        if i == len(pattern) and j == len(design):
            return True
        if i == len(pattern) and solve(design[j:]) == True:
            return True

    return False

from functools import lru_cache
@lru_cache(maxsize=1024)
def solve_with_matches(design):
    matches = 0
    if design == "":
        matches = matches + 1
    else:
        for pattern in startswith[design[0]]:
            i = 0
            j = 0
            while i < len(pattern) and j < len(design) and design[j] == pattern[i]:
                i = i + 1
                j = j + 1
            if i == len(pattern):
                matches = matches + solve_with_matches(design[j:])
            
    return matches

count = 0
matches = 0
for i, design in enumerate(new_designs):
    if solve(design):
        matches = matches + solve_with_matches(design)
        count = count + 1

print(count, matches)

