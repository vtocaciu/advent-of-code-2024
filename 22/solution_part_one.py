
numbers = []
with open("input.txt", "r") as file:
    for line in file.readlines():
        numbers.append(int(line))


def get_price(number):
    iter = 2000
    mod = 16777216
    for _ in range(iter):
        number =(number * 64) ^ number
        number = number % mod
        number = (number // 32) ^ number
        number = number % mod
        number =(number * 2048) ^ number
        number = number % mod

    return number

new_number = []
for number in numbers:
    new_number.append(get_price(number))

print(sum(new_number))