with open("aoc21.txt") as file1:
    puzzleInput = file1.read().splitlines()

allergentsDic = {}
possibleOptions = {}

for i in range(len(puzzleInput)):
    descriptionI = puzzleInput[i].split('(contains ')
    allergentsI = descriptionI[1].replace(',', '').replace(')', '').split(' ')
    transI = [el for el in descriptionI[0].strip().split(' ') if el not in allergentsDic.values()]
    
    for j in range(len(puzzleInput)):
        if j == i:
            continue
        descriptionJ = puzzleInput[j].split('(contains ')
        allergentsJ = descriptionJ[1].replace(',', '').replace(')', '').split(' ')
        transJ = [el for el in descriptionJ[0].strip().split(' ') if el not in allergentsDic.values()]
        
        for allergent in allergentsI:
            if allergent in allergentsDic:
                continue
            if allergent in allergentsJ:
                dictionary = [el for el in transI if el in transJ and el not in allergentsDic.values()]

                if len(dictionary) == 1:
                    allergentsDic[allergent] = dictionary[0]
                elif allergent in possibleOptions:
                    crossMatch = [el for el in dictionary if el in possibleOptions[allergent]]
                    
                    if len(crossMatch) == 1:
                        allergentsDic[allergent] = crossMatch[0]
                    else:
                        possibleOptions[allergent] = crossMatch
                else:
                    possibleOptions[allergent] = dictionary
            else:
                if len(transI) == 1:
                    allergentsDic[allergent] = transI[0]
                
healthy = []
for i in range(len(puzzleInput)):
    ingredients = puzzleInput[i].split('(contains ')[0].strip().split(' ')
    healthy.extend([el for el in ingredients if el not in allergentsDic.values()])

print(len(healthy))

res2 = ''
for el in dict(sorted(allergentsDic.items(), key=lambda item: item[0])).values():
    res2 += str(el) + ','
print(res2)