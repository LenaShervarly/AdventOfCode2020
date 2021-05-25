with open("aoc10.txt") as file1:
    puzzleInput = list(map(int, file1.read().splitlines()))

oneDiffCount = 0
threeDiffCount = 1
prev = 0
while len(puzzleInput) > 0:
    minJ = min(puzzleInput)
    if minJ - prev == 1:
        oneDiffCount += 1
    elif minJ - prev == 3:
        threeDiffCount += 1
    else:
        print('2 count')
    prev = minJ
    puzzleInput.remove(minJ)

print('## part1 ##')
print(oneDiffCount * threeDiffCount)


print('## part 2 ##')

with open("aoc10.txt") as file1:
    inputData2 = list(map(int, file1.read().splitlines()))

maxAmountOfWays = 0
def findAmountOptions(prevJ):
    options = []
    for adapter in inputData2:
        if (adapter - prevJ) <= 3 and (adapter - prevJ) > 0:
            options.append(adapter)
    if len(options) > 1:
        result = len(options)
        for option in options:
            result += findAmountOptions(option)
        return result
    else:
        return 0

for adapter in inputData2:
    maxAmountOfWays += findAmountOptions(adapter)

#print(maxAmountOfWays)

def part_2(adapters):
    adapters.append(0)
    adapters.sort()
    possibilities = {adapters[-1]: 1}
    for i, adapter in reversed(list(enumerate(adapters[:-1]))):
        choices = []
        for neigbour in adapters[(i + 1):(i + 4)]:
            if neigbour - adapter <= 3:
                choices.append(neigbour)

        sumOfNeigboursPossibilities = 0
        for choice in choices:
            sumOfNeigboursPossibilities += possibilities[choice]

        possibilities[adapter] = sumOfNeigboursPossibilities #sum(possibilities[c] for c in myChoices)
    return possibilities[0]

print(part_2(inputData2))