with open("aoc5.txt") as file1:
    puzzleInput = file1.read().splitlines()

def findCoord(low, high, directions, pointer):
    mid = (high + low) // 2
    if pointer == len(directions) -1:
        if directions[pointer] == 'B' or directions[pointer] == 'R':
            return mid + 1
        return mid
    if directions[pointer] == 'F' or directions[pointer] == 'L':
        return findCoord(low, mid, directions, pointer +1)
    else:
        return findCoord(mid +1, high, directions, pointer +1)

seatIds = []
for bpass in puzzleInput:
    row = findCoord(0, 127, bpass[0:7], 0)
    column = findCoord(0, 7, bpass[7:10], 0)
    seatIds.append(row * 8 + column)

sortedSeats = sorted(seatIds)
for j in range(len(sortedSeats)):
    if sortedSeats[j] + 1 not in sortedSeats:
        print(sortedSeats[j] + 1)

print(max(seatIds))