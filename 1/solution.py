left = []
right = []

with open("input.txt", "r") as file:
    while line:= file.readline():
        lft, rght = int(line.split("   ")[0]), int(line.split("   ")[1])
        left.append(lft)
        right.append(rght)

left.sort()
right.sort()

dif = [abs(left[i]-right[i]) for i in range(len(left))]

print(sum(dif))

from collections import defaultdict

app_lft = defaultdict(int)
app_rght = defaultdict(int)

for i in range(len(left)):
    app_lft[left[i]] = app_lft[left[i]] + 1
    app_rght[right[i]] = app_rght[right[i]] + 1


sim = []

for num in left:
    sim.append(num * app_rght[num])



print(sum(sim))