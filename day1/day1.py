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

bCounts = dict()
for bi in b:
    if bi in bCounts:
        bCounts[bi] = bCounts[bi] + 1
    else:
        bCounts[bi] = 1

similarity = 0
for ai in a:
    aiCount = bCounts.get(ai)
    if aiCount == None:
        aiCount = 0
    sim = ai * aiCount
    similarity += sim

print(similarity)