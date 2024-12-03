f = open("day1_input.txt")

a = [] 
b = []

for x in f:
    line = x.split()
    a.append(int(line[0]))
    b.append(int(line[1]))

a.sort()
b.sort()

total = 0
for i in range(0, len(a)):
    total += abs(a[i] - b[i])

print(total)