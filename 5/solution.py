rules = []
pages = []
with open("input.txt", "r") as file:
    for line in file.readlines():
        if "|" in line:
            rules.append(line)
        else:
            pages.append(line)

from collections import defaultdict

requires = defaultdict(set)

for rule in rules:
    first = int(rule.split("|")[0])
    second = int(rule.split("|")[1])

    requires[second].add(first)

numpages = []
for page in pages:
    page = page.strip()
    numpage = [int(n) for n in page.split(",") if n != ""]
    if numpage:
        numpages.append(numpage)

midnumbers = []

imidnumbers = []

def check_valid(page):
    valid = True
    spage = set(page)
    seennumber = set()
    for i, num in enumerate(page):
        if requires[num]:
            for r in requires[num]:
                if r not in seennumber and r in spage:
                    valid = False
                    break
            if not valid:
                break
        seennumber.add(num)
    return valid
    

for page in numpages:
    valid = check_valid(page)

    
    if valid:
        mid = len(page) // 2
        midnumbers.append(page[mid])
    
    else:
        i = 0
        correct_page = []
        seennumber = set()
        spage = set(page)
        while i < len(page):
            num = page[i]
            if requires[num]:
                before = requires[num].intersection(spage).difference(seennumber)
                if before:
                    for k in before:
                        page.remove(k)
                        page.insert(i, k)
                else:
                    seennumber.add(page[i])
                    i = i + 1
            else:
                seennumber.add(page[i])
                i = i + 1
        mid = len(page) // 2
        imidnumbers.append(page[mid])
                        

print(sum(midnumbers))
print(sum(imidnumbers))
