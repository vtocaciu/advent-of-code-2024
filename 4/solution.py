lines = []
with open("input.txt", "r") as file:
    text = file.read()
    lines = text.splitlines()

n = len(lines)
m = len(lines[0])


letters = ["X", "M", "A", "S"]
dir = [(-1, -1), (-1, 0), (0, -1), (0, 1), (1, 0), (1, 1), (-1, 1), (1, -1)]

found = 0

def is_in_border(x, y):
    return 0 <= x < n and 0 <= y < m

def find_xmas(x, y, way, current):
    global found
    if current == len(letters) - 1:
        found = found + 1
        return
    dirX, dirY = way
    if is_in_border(x+dirX, y+dirY) and lines[x+dirX][y+dirY] == letters[current + 1]:
        find_xmas(x+dirX, y+dirY, way, current+1)


for i in range(n):
    for j in range(m):
        if lines[i][j] == 'X':
            for way in dir:
                find_xmas(i, j, way, 0)

print(found)

xfound = 0

for i in range(n):
    for j in range(m):
        if lines[i][j] == 'A':
            if is_in_border(i+1, j+1) and is_in_border(i-1, j-1):
                if lines[i-1][j-1] in "SM" and lines[i+1][j+1] in "SM" and lines[i-1][j-1] != lines[i+1][j+1] and lines[i-1][j+1] in "SM" and lines[i+1][j-1] in "SM" and lines[i+1][j-1] != lines[i-1][j+1]:
                    xfound = xfound + 1

print(xfound)
