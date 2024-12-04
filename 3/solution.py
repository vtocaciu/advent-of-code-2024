import re

pattern = r"mul\(\d+,\d+\)"

with open("input.txt", "r") as file:
    text = file.read()
    matches = re.findall(pattern, text)

    res = []

    for match in matches:
        match = match[4:-1]
        first_number = int(match.split(",")[0])
        second_number = int(match.split(",")[1])
        res.append(first_number*second_number)
    
    print(sum(res))

    res = []
    mul_enabled = True
    i = 0

    while i < len(text):
        if text[i] == 'd':
            if i + 5 < len(text) and text[i:i+5] == 'don\'t':
                mul_enabled = False
            elif i + 2 < len(text) and text[i:i+2] == 'do':
                mul_enabled = True
        if text[i] == 'm' and mul_enabled:
            if i + 4 < len(text) and text[i:i+4] == 'mul(':
                j = i + 4
                valid = True
                current_number = 0
                first_number = None
                second_number = None
                while j < len(text):
                    if text[j] in [str(i) for i in range(10)]:
                        current_number = current_number * 10 + int(text[j])
                    elif text[j] == ')':
                        second_number = current_number
                        if second_number and first_number:
                            valid = True
                            break
                        break
                    elif text[j] == ',':
                        first_number = current_number
                        current_number = 0
                    else:
                        valid = False
                        break
                    j = j + 1
                
                if valid:
                    res.append(first_number*second_number)

        i = i + 1    
    print(sum(res))

