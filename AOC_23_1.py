puzzleInput = [int(i) for i in '389547612']

n = 1000_000
for i in range(10, n +1):
   puzzleInput.append(i)

dic = {}
for i in range(len(puzzleInput)):
    if i == len(puzzleInput) -1:
        dic[puzzleInput[i]] = puzzleInput[0]
    else:
        dic[puzzleInput[i]] = puzzleInput[i+1]

i = 0
previousCup = n 
while i < n*10:
    i +=1

    curCup = dic[previousCup]
    destCup = curCup - 1
    cupsToMove = []
    
    next = curCup
    for j in range(1, 4):
        next = dic[next]
        cupsToMove.append(next)
    
    while destCup in cupsToMove or destCup < 1:
        destCup -=1
        if destCup < 1:
            destCup = len(puzzleInput)
    
    # print('## move ' + str(i))
    # print('cur cup is ' + str(curCup))
    # print(dic)
    # print(cupsToMove)
    # print(destCup)
    # print()

    dic[curCup] = dic[cupsToMove[2]]
    previousCup = curCup

    temp = dic[destCup]
    dic[destCup] = cupsToMove[0]
    dic[cupsToMove[2]] = temp


finalArray = []
next = dic[1]
# for i in range(len(puzzleInput)-1):
#     finalArray.append(next)
#     next = dic[next]
# print(''.join(str(x) for x in finalArray))

print(dic[1] * dic[dic[1]])