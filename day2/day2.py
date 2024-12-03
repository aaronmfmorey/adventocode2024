def graduallyIncreasing(record):
    previousLevel = 0
    isFirst = True
    for level in record.split(" "):
        if isFirst:
            previousLevel = int(level)
            isFirst = False
            continue

        iLevel = int(level)
        if iLevel > previousLevel:
            diff = iLevel - previousLevel
            if diff > 3:
                return False
        else:
            return False
        previousLevel = iLevel
    return True

def graduallyDecreasing(record):
    previousLevel = 0
    isFirst = True
    for level in record.split(" "):
        if isFirst:
            previousLevel = int(level)
            isFirst = False
            continue

        iLevel = int(level)
        if iLevel < previousLevel:
            diff = previousLevel - iLevel
            if diff > 3:
                return False
        else:
            return False
        previousLevel = iLevel
    return True

f = open("day2_input.txt")

safeCount = 0
for line in f:
    if graduallyIncreasing(line) or graduallyDecreasing(line):
        safeCount+= 1

print(safeCount)