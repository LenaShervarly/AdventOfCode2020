with open("aoc17.txt") as file1:
    inputData = file1.read().splitlines()

board = []
innerBoard = []
emptyBoard = []
inner3D = []
empty3D = []

for y in inputData:
    z = list(y)
    innerBoard.append(z)
n = 15

for i in range(n):
    for z in innerBoard:
        z.insert(0, '.')
        z.append('.')
    
emptyRow = []
for j in range(len(innerBoard[0])):
    emptyRow.append('.')

for i in range(n):
    innerBoard.insert(0, emptyRow.copy())
    innerBoard.append(emptyRow.copy())

inner3D.append(innerBoard)

for j in range(len(innerBoard)):
    emptyBoard.append(emptyRow.copy())

for i in range(n+1):
    inner3D.append(emptyBoard.copy())
    inner3D.insert(0, emptyBoard.copy())

board.append(inner3D)

for i in range(n+2):
    empty3D.append(emptyBoard.copy())
    empty3D.insert(0, emptyBoard.copy())

for i in range(n):
    board.append(empty3D.copy())
    board.insert(0, empty3D.copy())

cycleCounter = 0
while cycleCounter < 6:
    cycleCounter += 1
    newBoard = []
    for w in range(len(board)-2):
        newW = []
        for x in range(len(board[w]) -2):
            newX = []
            for y in range(len(board[w][x]) -2):
                newY = []
                for z in range(len(board[w][x][y])-2):
                    newZ = '.'
                    activeNeigbours = 0

                    XXL = [-1, 0, 1]
                    for wl in XXL:
                        for xl in XXL:
                            for yl in XXL:
                                for zl in XXL:
                                    if(xl == 0 and yl == 0 and zl == 0 and wl == 0):
                                        continue
                                    if board[w + wl][x + xl][y + yl][z + zl] == '#':
                                        activeNeigbours += 1
                    
                    if (activeNeigbours == 2 or activeNeigbours == 3) and board[w][x][y][z] == '#':
                        newZ = '#'
                    elif activeNeigbours == 3 and board[w][x][y][z] == '.':
                        newZ = '#'
                    newY.append(newZ)
                newX.append(newY)
            newW.append(newX)
        newBoard.append(newW)

    board = newBoard

counter = 0
for w in range(len(board)):
    for x in range(len(board[w])):
        for y in range(len(board[w][x])):
            for z in range(len(board[w][x][y])):
                if board[w][x][y][z] == '#':
                    counter += 1
print(counter)


 # if board[x][y][z-1] == '#':
                #     activeNeigbours +=1
                # if board[x][y][z+1] == '#':
                #     activeNeigbours +=1

                # if board[x][y-1][z] == '#':
                #     activeNeigbours +=1
                # if board[x][y-1][z-1] == '#':
                #     activeNeigbours +=1
                # if board[x][y-1][z+1] == '#':
                #     activeNeigbours +=1

                # if board[x][y+1][z] == '#':
                #     activeNeigbours +=1
                # if board[x][y+1][z-1] == '#':
                #     activeNeigbours +=1
                # if board[x][y+1][z+1] == '#':
                #     activeNeigbours +=1

                # if board[x+1][y+1][z] == '#':
                #     activeNeigbours +=1
                # if board[x+1][y+1][z-1] == '#':
                #     activeNeigbours +=1
                # if board[x+1][y+1][z+1] == '#':
                #     activeNeigbours +=1

                # if board[x+1][y-1][z] == '#':
                #     activeNeigbours +=1
                # if board[x+1][y-1][z-1] == '#':
                #     activeNeigbours +=1
                # if board[x+1][y-1][z+1] == '#':
                #     activeNeigbours +=1

                # if board[x+1][y][z] == '#':
                #     activeNeigbours +=1
                # if board[x+1][y][z-1] == '#':
                #     activeNeigbours +=1
                # if board[x+1][y][z+1] == '#':
                #     activeNeigbours +=1
                
                # if board[x-1][y+1][z] == '#':
                #     activeNeigbours +=1
                # if board[x-1][y+1][z-1] == '#':
                #     activeNeigbours +=1
                # if board[x-1][y+1][z+1] == '#':
                #     activeNeigbours +=1

                # if board[x-1][y-1][z] == '#':
                #     activeNeigbours +=1
                # if board[x-1][y-1][z-1] == '#':
                #     activeNeigbours +=1
                # if board[x-1][y-1][z+1] == '#':
                #     activeNeigbours +=1

                # if board[x-1][y][z] == '#':
                #     activeNeigbours +=1
                # if board[x-1][y][z-1] == '#':
                #     activeNeigbours +=1
                # if board[x-1][y][z+1] == '#':
                #     activeNeigbours +=1