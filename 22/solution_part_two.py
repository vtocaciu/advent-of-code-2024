
from collections import defaultdict
numbers = []
with open("input.txt", "r") as file:
    for line in file.readlines():
        numbers.append(int(line))


occurences = defaultdict(int)
def get_price_ranges(number):
    iter = 2000
    mod = 16777216
    ranges = []
    prev = number%10
    seen = set()
    for _ in range(iter):
        number =(number * 64) ^ number
        number = number % mod
        number = (number // 32) ^ number
        number = number % mod
        number =(number * 2048) ^ number
        number = number % mod
        ranges.append(number % 10 - prev)
        prev = number % 10
        if len(ranges) == 5:
            ranges.pop(0)
        if len(ranges) == 4:
            if tuple(ranges) not in seen:
                seen.add(tuple(ranges))
                occurences[tuple(ranges)] += number % 10

for number in numbers:
    get_price_ranges(number)

max_bananas = None
max_key = None

for key, value in occurences.items():
    if max_bananas is None:
        max_bananas = occurences[key]
        max_key = key
    if value > max_bananas:
        max_bananas = occurences[key]
        max_key = key

print(max_key, max_bananas)
