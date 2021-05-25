with open("aoc11.txt") as file1:
    puzzleInput = file1.read().splitlines()

updated = True
counter = 0
while updated:
    updated = False
    newBoard = []
    for i in range(len(puzzleInput)):
        row = list(puzzleInput[i])
        newRow = []
        for j in range(len(row)):
            seat = row[j]
            occupiedSeats = 0
            if i-1 >= 0:
                previousRow = puzzleInput[i-1]
                if previousRow[j] == '#':
                    occupiedSeats +=1
                if j-1 >= 0 and previousRow[j-1] == '#':
                    occupiedSeats +=1
                if j+1 < len(row) and previousRow[j+1] == '#':
                    occupiedSeats +=1
            if i + 1 < len(puzzleInput):
                nextRow = puzzleInput[i+1]
                if nextRow[j] == '#': 
                    occupiedSeats +=1
                if j-1 >= 0 and nextRow[j-1] == '#':
                    occupiedSeats +=1
                if j+1 < len(row) and nextRow[j+1] == '#':
                    occupiedSeats +=1
            if j-1 >= 0 and row[j-1] == '#':
                occupiedSeats +=1 
            if j+1 < len(row) and row[j+1] == '#':
                occupiedSeats += 1

            if occupiedSeats == 0 and seat == 'L':
                seat = '#'
                updated = True
            elif occupiedSeats >= 4 and seat == '#':
                seat = 'L'
                updated = True
            
            newRow.append(seat)
        newBoard.append(newRow)

    puzzleInput = newBoard
    print("new round")
    for i in range(len(puzzleInput)):
        print(puzzleInput[i])

for i in range(len(puzzleInput)):
    for el in puzzleInput[i]:
        if el == '#':
            counter += 1
print(counter)
