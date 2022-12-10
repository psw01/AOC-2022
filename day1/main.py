
elf = 0
bag = []

current = 0

with open('./day1.txt') as f:
    for line in f:
        if(line.strip().isdigit()):
            current += int(line)
        else:
            bag.append(current)
            current = 0

bag.sort(reverse=True)

print("Top Elves has ", bag[0], "Calories ")
print("Top3 Elves has ", (bag[0]+bag[1]+bag[2]), "Calories ")

