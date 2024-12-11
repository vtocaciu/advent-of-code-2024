with open("input.txt", "r") as file:
    stones = file.readline()



import functools
from collections import defaultdict


st = defaultdict(int)

for stone in stones.strip().split(" "):
    st[int(stone)] = st[int(stone)] + 1

stones = st

# fuck this, application quit like a gazzilion times
@functools.lru_cache
def apply_rule(stone):
    str_stone = str(stone)
    if len(str_stone) % 2 == 0:
        left = int(str_stone[:len(str_stone)//2])
        right = int(str_stone[len(str_stone)//2:])
        return left, right
    elif stone == 0:
        return 1
    else:
        return stone*2024

def blink(stones):
    new_stones = defaultdict(int)
    for stone in stones.keys():
        value = apply_rule(stone)
        if isinstance(value,tuple):
           new_stones[value[0]] = new_stones[value[0]] + stones[stone]
           new_stones[value[1]] = new_stones[value[1]] + stones[stone]
        else:
           new_stones[value] = new_stones[value] + stones[stone]
    return new_stones

i = 0
blinks = 75
while i < blinks:
    stones = blink(stones)
    i = i + 1

print(sum([val for val in stones.values()]))