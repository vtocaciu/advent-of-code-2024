with open("input.txt", "r") as file:
    stones = file.readline()

stones = [stone for stone in stones.strip().split(" ")]

i = 0
blinks = 25
from collections import defaultdict
cache = defaultdict(dict)
queue = [(stone, blinks) for stone in stones]
final_stones = []
j = 0
iter = 0
while queue:
    i = 0
    init_stone, blinks = queue.pop()
    stone = init_stone
    print(iter, stone, blinks, cache.get(stone))
    while i < blinks:
        if cache.get(stone):
            if cache[stone].get(i):
                value = cache[stone]
                if isinstance(value, tuple):
                    stone = value[0]
                    queue.append((value[1], blinks-i-1))
                else:
                    stone = value
        elif len(stone) % 2 == 0:
            left = str(int(stone[:len(stone)//2]))
            right = str(int(stone[len(stone)//2:]))
            cache[stone][0]=(left, right)
            cache[init_stone][i] = (left, right)
            stone = left
            queue.append((right, blinks-i-1))
        elif stone == "0":
            stone = "1"
        else:
            cache[stone][0] = str(int(stone)*2024)
            cache[init_stone][i] = cache[stone][0]
            stone = cache[stone]
        i = i + 1
    final_stones.append(stone)
    iter = iter + 1


print(len(final_stones))