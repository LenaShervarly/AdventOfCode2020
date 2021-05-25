import copy

with open("aoc24.txt") as file1:
    puzzleInput = file1.read().splitlines()

row = ['w' for i in range(0,250)]
board = []
for i in range(0,250):
    board.append(row.copy())

for command in puzzleInput:
    i = 0
    x = 125
    y = 125
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
    if board[y][x] == 'w':
        board[y][x] = 'b'
    else:
        board[y][x] = 'w'

blackCount = 0 
for y in board:
    for x in y:
        if x == 'b':
            blackCount += 1

print(blackCount)

for r in range(100):
    copyB = copy.deepcopy(board)
    blackCount = 0 
    for i in range(len(board)-1):
        for j in range(len(board)-1):
            neigb = 0
            
            if board[i+1][j] == 'b':
                neigb += 1
            if board[i-1][j] == 'b':
                neigb += 1
            if board[i][j-1] == 'b':
                neigb += 1
            if board[i][j+1] == 'b':
                neigb += 1
            
            if i % 2 != 0:
                if board[i-1][j+1] == 'b':
                    neigb += 1
                if board[i+1][j+1] == 'b':
                    neigb += 1
            else:
                if board[i-1][j-1] == 'b':
                    neigb += 1
                if board[i+1][j-1] == 'b':
                    neigb += 1
            
            if board[i][j] == 'w' and neigb == 2:
                copyB[i][j] = 'b'
            if board[i][j] == 'b' and (neigb == 0 or neigb > 2):
                copyB[i][j] = 'w'

    board = copyB

blackCount = 0 
for yI in board:
    for xj in yI:
        if xj == 'b':
            blackCount += 1
print(blackCount)
