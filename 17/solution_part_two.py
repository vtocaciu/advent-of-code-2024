with open("input.txt", "r") as file:
    a = int(file.readline()[12:])
    b = int(file.readline()[12:])
    c = int(file.readline()[12:])
    file.readline()
    program = file.readline()[9:].split(",")


def solve(registrar, program):
    out = []
    i = 0
    while i < len(program):
        values = {0: 0, 1:1, 2:2, 3:3, 4: registrar["a"], 5: registrar["b"], 6: registrar["c"]}
        opcode = int(program[i])
        operand = int(program[i+1])
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
    
    return out


def find_a(program):
  # only the last 3 bits count %8 gets printed
  out = []
  matched = program[-1:]
  a = 8 ** 15 # min value for 16 digits to get outputed
  power = 14 # increment by 8 ** 13 to start with

  while out != program:
    a += 8 ** power
    registrar = dict(a=a, b=0, c=0)
    out = solve(registrar, program)
    # by decreasing the power, the matched digits will no longer change
    if out[-len(matched):] == matched:
      power = max(0, power - 1)
      matched = program[-(len(matched)+1):]

  return a

print(find_a(program))