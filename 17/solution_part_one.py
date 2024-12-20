
with open("input.txt", "r") as file:
    a = int(file.readline()[12:])
    b = int(file.readline()[12:])
    c = int(file.readline()[12:])
    file.readline()
    program = file.readline()[9:].split(",")



registrar = dict(a=a, b=b, c=c)
out = []
i = 0
while i < len(program):
    values = {0: 0, 1:1, 2:2, 3:3, 4: registrar["a"], 5: registrar["b"], 6: registrar["c"]}
    opcode = int(program[i])
    operand = int(program[i+1])
    # print(i, opcode, operand, registrar)
    if opcode == 0:
        registrar["a"] = registrar["a"] // pow(2, values[operand])
        i = i + 2
    elif opcode == 1:
        registrar["b"] = registrar["b"] ^ operand
        i = i + 2
    elif opcode == 2:
        registrar["b"] = values[operand] % 8
        i = i + 2
    elif opcode == 3:
        if registrar["a"] == 0:
            i = i + 2
        else:
            i = operand
    elif opcode == 4:
        registrar["b"] = registrar["b"] ^ registrar["c"]
        i = i + 2
    elif opcode == 5:
        out.append(str(values[operand] % 8))
        i = i + 2
    elif opcode == 6:
        registrar["b"] = registrar["a"] // pow(2, values[operand])
        i = i + 2
    elif opcode == 7:
        registrar["c"] = registrar["a"] // pow(2, values[operand])
        i = i + 2


print(",".join(out))
