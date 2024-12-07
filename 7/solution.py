
numbers = []
equations = []

with open("input.txt", "r") as file:
    for line in file.readlines():
        numbers.append(int(line.split(":")[0]))
        equations.append([int(num) for num in line.split(":")[1].strip().split(" ")])

def solve(num, eqs, current_sum, i):
    if current_sum == num and i == len(eqs):
        return True
    
    if i == len(eqs):
        return False
    
    return solve(num, eqs, current_sum+eqs[i], i+1) or solve(num, eqs, current_sum*eqs[i], i+1)

def solve_with_concat(num, eqs, current_sum, i):
    if current_sum == num and i == len(eqs):
        return True
    
    if i == len(eqs):
        return False
    
    left = str(current_sum)
    right = str(eqs[i])
    concat = left+right
    concat = left+right
    

    return solve_with_concat(num, eqs, current_sum+eqs[i], i+1) or solve_with_concat(num, eqs, current_sum*eqs[i], i+1) or solve_with_concat(num, eqs, int(concat), i+1)

n = len(numbers)

sum = 0
concat_sum = 0
for i in range(n):
    if solve(numbers[i], equations[i], 0, 0):
        sum = sum + numbers[i]
    
    if solve_with_concat(numbers[i], equations[i], 0, 0):
        concat_sum = concat_sum + numbers[i]


print(sum)
print(concat_sum)

