with open("input.txt", "r") as file:
    stones = file.readline()

stones = [stone for stone in stones.strip().split(" ")]

import functools
@functools.lru_cache
def apply_rule(stone, blink):
    if len(stone) % 2 == 0:
        left = str(int(stone[:len(stone)//2]))
        right = str(int(stone[len(stone)//2:]))
        return left, right
    elif stone == "0":
        return "1"
    else:
        return str(int(stone)*2024)

i = 0
blinks = 75
queue = [(stone, blinks) for stone in stones]
final_stones = []
j = 0
iter = 0
while queue:
    print(iter)
    i = 0
    stone, blinks = queue.pop(0)
    while i < blinks:
        if len(stone) % 2 == 0:
            left = str(int(stone[:len(stone)//2]))
            right = str(int(stone[len(stone)//2:]))
            stone = left
            queue.append((right, blinks-i-1))
        elif stone == "0":
            stone = "1"
        else:
            stone = str(int(stone)*2024)
        i = i + 1
    final_stones.append(1)
    iter = iter + 1
print(len(final_stones))

# while i < blinks:
#     #print(i, stones)
#     new_stones = []
#     for stone in stones:
#         if len(stone) % 2 == 0:
#             left = str(int(stone[:len(stone)//2]))
#             right = str(int(stone[len(stone)//2:]))
#             new_stones.append(left)
#             new_stones.append(right)
#         elif stone == "0":
#             new_stones.append("1")
#         else:
#             new_stones.append(str(int(stone)*2024))
#     stones = new_stones[:]
#     i = i + 1

# print(len(stones))