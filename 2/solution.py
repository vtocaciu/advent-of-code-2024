
def is_safe_increasing(num):
    i = 1
    n = len(num)
    while i < n:
        if num[i] <= num[i-1]:
            return False
        if num[i] - num[i-1] > 3:
            return False
        
        i = i + 1
    
    return True


def is_safe_decreasing(num):
    i = 1
    n = len(num)
    while i < n:
        if num[i] >= num[i-1]:
            return False
        if num[i-1] - num[i] > 3:
            return False
        i = i + 1

    return True


def is_safe_increasing_tolerating(num):
    if is_safe_increasing(num):
        return True
    i = 0
    n = len(num)
    while i < n:
        numb = num[:]
        del numb[i]
        if is_safe_increasing(numb):
            return True
        i = i + 1
        

    return False

def is_safe_decreasing_tolerating(num):
    if is_safe_decreasing(num):
        return True
    i = 0
    n = len(num)
    while i < n:
        numb = num[:]
        del numb[i]
        if is_safe_decreasing(numb):
            return True
        
        i = i + 1

    return False


safe = 0
safe_tolerating = 0
with open("input.txt", "r") as file:
    while line:= file.readline():
        numbers = [int(num) for num in line.split(" ")]
        if is_safe_increasing(numbers) or is_safe_decreasing(numbers):
            safe = safe + 1
        if is_safe_increasing_tolerating(numbers) or is_safe_decreasing_tolerating(numbers):
            safe_tolerating = safe_tolerating + 1

print(safe)
print(safe_tolerating)
