with open("aoc7.txt") as file1:
    puzzleInput = file1.read().splitlines()

def findBag(color) :
    bags = []
    for i in range(len(puzzleInput)):
        line = puzzleInput[i].split(' bags contain')
        if color in line[1]:
            bags.append(line[0].strip())
    return list(set(bags))

def depthBagSearch(bags):
    for color in set(bags):
        newBags = findBag(color)
        depthBagSearch(newBags)
        foundBags.extend(newBags)
    return (foundBags)

foundBags = ['shiny gold']
print(len(set(depthBagSearch(foundBags))) -1)

#part2


def findNumberOfBags(color) :
    numberOfBags = 0
    for i in range(len(puzzleInput)):
        line = puzzleInput[i].split(' bags contain ')
        if color in line[0]:
                allColorDescriptions = line[1].split(', ')
                numberOfBags = 0
                if allColorDescriptions[0] == 'no other bags.':
                    break
                for colorInfo in allColorDescriptions:
                    newColorInfo = colorInfo.split(' ')
                    foundBagColor = newColorInfo[1] + ' ' + newColorInfo[2]
                    childBagsNumber = findNumberOfBags(foundBagColor)
                    if childBagsNumber > 0:
                        numberOfBags += int(newColorInfo[0]) * findNumberOfBags(foundBagColor) + int(newColorInfo[0])
                    else:
                        numberOfBags += int(newColorInfo[0]) 
    return numberOfBags

print(findNumberOfBags('shiny gold'))


