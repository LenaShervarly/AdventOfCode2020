with open("aoc9.txt") as file1:
    puzzleInput = list(map(int, file1.read().splitlines()))

preambule = 25

def hasValidSum(data, sum):
    for i in range(len(data)):
        for j in range(1, len(data) -1):
            if data[i] + data[j] == sum:
                return True
    return False

invalidNumber = 0
for i in range(preambule, len(puzzleInput)):
    if not hasValidSum(puzzleInput[i - preambule: i], puzzleInput[i]):
        invalidNumber = puzzleInput[i]

print(invalidNumber)

contiguousSet = []
sum = puzzleInput[0]
pointer = 0
localPointer = 1
while sum != invalidNumber:
        entry = puzzleInput[pointer + localPointer]
        sum += entry
        contiguousSet.append(entry)
        if sum > invalidNumber:
            sum = 0
            localPointer = 0
            contiguousSet.pop
            pointer += 1
        elif sum == invalidNumber:
            print(min(contiguousSet) + max(contiguousSet))
        else:
            localPointer += 1
