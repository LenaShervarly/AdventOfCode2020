with open("aoc3.txt") as file1:
    surfaceMap = file1.read().splitlines() 

def countTrees(right, down):
    treeCounter = 0
    pointer = 0
    for i in range(0, len(surfaceMap)-down, down):
        row = surfaceMap[i+down]
        pointer = (pointer + right) % len(row)
        if row[pointer] == '#':
            treeCounter += 1
    return treeCounter

print(countTrees(1, 1) * countTrees(3, 1) * countTrees(5, 1) * countTrees(7, 1) * countTrees(1, 2))
