from string import ascii_uppercase, ascii_lowercase
alp = ascii_lowercase + ascii_uppercase
data = {}

def part1():
    with open('./day3.txt') as f:
        for line in f:
            line = line.strip()
            set1 =  line[int((len(line)) / 2) : ]
            set2 =  line[: int((len(line)) / 2) ]
            commonChar = ''.join(set(set1) & set(set2))
            if(commonChar not in data):
                data[commonChar] = alp.find(commonChar) + 1
            else:
                data[commonChar] += alp.find(commonChar) + 1

def part2():
    lines = []
    with open('./day3.txt') as f:
        for line in f:
            line = line.strip()
            lines.append(line)
            if(len(lines) == 3):
                commonChar = ''.join(set(lines[0]) & set(lines[1]) & set(lines[2]))
                lines = []
                if(commonChar not in data):
                    data[commonChar] = alp.find(commonChar) + 1
                else:
                    data[commonChar] += alp.find(commonChar) + 1


                

# part1()
part2()
print(data)
print(sum(data.values()))