puzzleInput = [int(i) for i in '389547612']
print(puzzleInput)

i = 0
current = 0
previousCup = puzzleInput[0]
while i < 100:
    i +=1
    print('## move ' + str(i))

    curCup = puzzleInput[current]
    
    print('cur cup is ' + str(curCup))
    print(puzzleInput)
    
    destCup = curCup - 1
    cupsToMove = []
    for j in range(1, 4):
        cupsToMove.append(puzzleInput[(current +j) % len(puzzleInput)])
    
    while destCup in cupsToMove or destCup < 1:
        destCup -=1
        if destCup < 1:
            destCup = 9
    
    print(cupsToMove)
    print(destCup)
    print()
    for cup in cupsToMove:
        puzzleInput.remove(cup)

    destIndex = puzzleInput.index(destCup)
    cupsToMove.reverse()
    insertInto = (destIndex+1) % len(puzzleInput)
    for cup in cupsToMove:
        puzzleInput.insert(insertInto, cup)

    previousCup = curCup
    current =  (puzzleInput.index(previousCup) +1) % len(puzzleInput) 



oneIndex = puzzleInput.index(1) +1
res = ''
for i in range(len(puzzleInput) -1):
    res += str(puzzleInput[oneIndex % len(puzzleInput)])
    oneIndex += 1

print(puzzleInput)
print(res)