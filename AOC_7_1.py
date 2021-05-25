with open("aoc7.txt") as file1:
    puzzleInput = file1.read().splitlines()


foundBags = ['shiny gold']
run = True
while run:
    run = False
    size = len(foundBags)
    for i in range(len(puzzleInput)):
        line = puzzleInput[i].split(' bags contain')
        for color in foundBags:
            if color in line[1] and line[0].strip() not in foundBags:
                foundBags.append(line[0].strip())
                run = True
    print(size)

print(len(set(foundBags)) -1)



