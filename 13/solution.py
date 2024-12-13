lines = []

with open("input.txt", "r") as file:
    text = file.read()
    for line in text.split("\n\n"):
        lines.append(line)
    
equations = []
for eq in lines:
    a, b, res = None, None, None
    for e in eq.split("\n"):
        if e.startswith("Button A: "):
            e = e[10:]
            x, y = e.split(", ")
            x = int(x[2:])
            y = int(y[2:])
            a = (x, y)
        elif e.startswith("Button B: "):
            e = e[10:]
            x, y = e.split(", ")
            x = int(x[2:])
            y = int(y[2:])
            b = (x, y)
        else:
            e = e[7:]
            x, y = e.split(", ")
            x = int(x[2:])
            y = int(y[2:])
            res = (x, y)
    equations.append((a,b,res))

def solve(first, second, res):
    x1, y1 = first
    x2, y2 = second
    resX, resY = res
    

    a = (resX * y2 - resY * x2)/(x1 * y2 - x2 * y1)
    
    if int(a) != a or a > 100 or a < 0:
        return False, -1, -1
    
    b = (resX - x1*a)/x2
    if b > 100 or b < 0:
        return False, -1, -1
    
    return True, a, b

def solve_wrong_coords(first, second, res):
    x1, y1 = first
    x2, y2 = second
    resX, resY = res

    resX = resX + 10000000000000
    resY = resY + 10000000000000

    a = (resX * y2 - resY * x2)/(x1 * y2 - x2 * y1)
    
    if int(a) != a :
        return False, -1, -1
    
    b = (resX - x1*a)/x2

    return True, a, b
       
tokens = 0
for eq in equations:
    solved, a, b = solve(*eq)
    if solved:
        tokens = tokens + 3*a + b
print(tokens)

tokens = 0
for eq in equations:
    solved, a, b = solve_wrong_coords(*eq)
    if solved:
        tokens = tokens + 3*a + b

print(tokens)