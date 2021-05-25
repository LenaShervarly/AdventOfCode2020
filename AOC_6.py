with open("aoc6.txt") as file1:
    puzzleInput = file1.read().splitlines()

yesCount = 0
yesSet = set()
for answer in puzzleInput:
    if answer:
        for j in range(len(answer)):
            yesSet.add(answer[j])
    else :
        yesCount += len(yesSet)
        yesSet.clear()

print(yesCount)

#part2
commonYesCount = 0
group = []
for answer in puzzleInput:
    if answer:
        yes = set()
        for j in range(len(answer)):
            yes.add(answer[j])
        group.append(yes)
    else :
        groupIntersection = group[0]
        for j in range(len(group) -1):
            groupIntersection.intersection_update(group[j+1])
        commonYesCount += len(groupIntersection)
        group.clear()
        groupIntersection.clear()

print(commonYesCount)

