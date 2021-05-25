with open("aoc25.txt") as file1:
    puzzleInput = [int(i) for i in file1.read().splitlines()]

subjNu = 7
loopSize = 0
res =  1
while res != puzzleInput[0]:
    res = (res * subjNu) % 20201227
    loopSize += 1

res2 = 1
while loopSize  > 0:
    res2 = (res2 * puzzleInput[1]) % 20201227
    loopSize -=1

print(res2)

print('#checking reverse order')

subjNu = 7
loopSize = 0
res =  1
while res != puzzleInput[1]:
    res = (res * subjNu) % 20201227
    loopSize += 1

res2 = 1
while loopSize  > 0:
    res2 = (res2 * puzzleInput[0]) % 20201227
    loopSize -=1

print(res2)