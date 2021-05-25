with open("aoc24.txt") as file1:
    puzzleInput = file1.read().splitlines()

row = ['w' for i in range(0,100)]
board = []
for i in range(0,100):
    board.append(row.copy())

#isBlack = {}

for command in puzzleInput:
    i = 0
    x = 51
    y = 51
    while i < len(command):
        if command[i] == 'e':
            x += 1
            i += 1
        elif command[i] == 'w':
            x -= 1
            i += 1 
        else:
            if y % 2 == 0:
                if command[i] == 's' and command[i+1] == 'e':
                    y += 1
                    i += 2
                elif command[i] == 's' and command[i+1] == 'w':
                    x -= 1
                    y += 1
                    i += 2
                elif command[i] == 'n' and command[i+1] == 'e':
                    y -= 1
                    i += 2
                elif command[i] == 'n' and command[i+1] == 'w':
                    x -= 1
                    y -= 1
                    i += 2
            else:
                if command[i] == 's' and command[i+1] == 'e':
                    y += 1
                    x += 1
                    i += 2
                elif command[i] == 's' and command[i+1] == 'w':
                    y += 1
                    i += 2
                elif command[i] == 'n' and command[i+1] == 'e':
                    y -= 1
                    x += 1
                    i += 2
                elif command[i] == 'n' and command[i+1] == 'w':
                    y -= 1
                    i += 2
    if board[x][y] == 'w':
        board[x][y] = 'b'
    else:
        board[x][y] = 'w'

blackCount = 0 
for x in board:
    for y in x:
        if y == 'b':
            blackCount += 1

print(blackCount)

for i in range(10):
    copy = board.copy()
    for y in range(len(board)-1):
        for x in range(len(board[y])-1):
            neigb = 0
            if board[x+1][y] == 'b':
                neigb += 1
            if board[x-1][y] == 'b':
                neigb += 1
            if board[x][y-1] == 'b':
                neigb += 1
            if board[x][y+1] == 'b':
                neigb += 1
            if x % 2 != 0:

                if board[x-1][y+1] == 'b':
                    neigb += 1
                if board[x-1][y-1] == 'b':
                    neigb += 1
            else:
                if board[x+1][y+1] == 'b':
                    neigb += 1
                if board[x+1][y-1] == 'b':
                    neigb += 1
            
            if board[x][y] == 'w' and neigb == 2:
                copy[x][y] = 'b'
                #print('turning black following x: ' + str(x) + ', y: ' + str(y) )
                #print(neigb)
            elif board[x][y] == 'b' and (neigb == 0 or neigb > 2):
                copy[x][y] = 'w'
    board = copy

    blackCount = 0 
    for x in copy:
        for y in x:
            if y == 'b':
                blackCount += 1

    print(blackCount)