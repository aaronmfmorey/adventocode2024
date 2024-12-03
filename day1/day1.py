f = open("day1_input.txt")

leftColumn = [] 
rightColumn = []

for line in f:
    line = line.split()
    leftColumn.append(int(line[0]))
    rightColumn.append(int(line[1]))

leftColumn.sort()
rightColumn.sort()

total = 0
for i in range(0, len(leftColumn)):
    total += abs(leftColumn[i] - rightColumn[i])

print(total)

rightCounts = dict()
for rc in rightColumn:
    if rc in rightCounts:
        rightCounts[rc] = rightCounts[rc] + 1
    else:
        rightCounts[rc] = 1

similarity = 0
for lc in leftColumn:
    lcCount = rightCounts.get(lc)
    if lcCount == None:
        lcCount = 0
    similarity += lc * lcCount

print(similarity)