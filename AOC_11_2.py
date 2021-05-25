with open("aoc11.txt") as file1:
    puzzleInput = file1.read().splitlines()

data = []
for line in puzzleInput:
    data.append(list(line))

updated = True
counter = 0
while updated:
    updated = False
    newBoard = []
    for i in range(len(data)):
        newRow = []
        for j in range(len(data[i])):
            occupiedSeats = 0
            #right
            pointer = j+1
            while pointer <  len(data[i]) and data[i][pointer] == '.': 
                pointer += 1
            if pointer <  len(data[i]) and data[i][pointer] == '#':
                occupiedSeats += 1

            #left
            pointer = j-1
            while pointer >= 0 and data[i][pointer] == '.': 
                pointer -= 1
            if pointer >= 0 and data[i][pointer] == '#':
                occupiedSeats += 1

            #down
            pointer = i+1
            while pointer <  len(data) and data[pointer][j] == '.': 
                pointer += 1
            if pointer <  len(data) and data[pointer][j] == '#':
                occupiedSeats += 1

            #up
            pointer = i-1
            while pointer >= 0 and data[pointer][j] == '.': 
                pointer -= 1
            if pointer >= 0 and data[pointer][j] == '#':
                occupiedSeats += 1

            #up-left
            pointerI = i-1
            pointerJ = j-1
            while pointerI >= 0 and pointerJ >= 0 and data[pointerI][pointerJ] == '.': 
                pointerI -= 1
                pointerJ -= 1
            if pointerI >= 0 and pointerJ >= 0 and data[pointerI][pointerJ] == '#':
                occupiedSeats += 1

            #down-right
            pointerI = i+1
            pointerJ = j+1
            while pointerI <  len(data) and pointerJ <  len(data[i]) and data[pointerI][pointerJ] == '.': 
                pointerI += 1
                pointerJ += 1
            if pointerI <  len(data) and pointerJ <  len(data[i]) and data[pointerI][pointerJ] == '#':
                occupiedSeats += 1

                        #up-left
            pointerI = i+1
            pointerJ = j-1
            while pointerI < len(data) and pointerJ >= 0 and data[pointerI][pointerJ] == '.': 
                pointerI += 1
                pointerJ -= 1
            if pointerI < len(data) and pointerJ >= 0 and data[pointerI][pointerJ] == '#':
                occupiedSeats += 1

            #down-right
            pointerI = i-1
            pointerJ = j+1
            while pointerI >= 0 and pointerJ <  len(data[i]) and data[pointerI][pointerJ] == '.': 
                pointerI -= 1
                pointerJ += 1
            if pointerI >= 0 and pointerJ <  len(data[i])  and data[pointerI][pointerJ] == '#':
                occupiedSeats += 1

            if occupiedSeats == 0 and data[i][j] == 'L':
                newRow.append( '#')
                updated = True
            elif occupiedSeats >= 5 and data[i][j] == '#':
                newRow.append('L')
                updated = True
            else: 
                newRow.append(data[i][j])
        newBoard.append(newRow)

    data = newBoard

for i in range(len(data)):
    for el in data[i]:
        if el == '#':
            counter += 1
print(counter)
