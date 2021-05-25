with open("aoc15.txt") as file1:
    inputData = list(map(int, file1.read().split(',')))


game = {}
index = 1
for number in inputData:
    game[number] = [index]
    index +=1
print(game)

lastNumber = inputData[2]
i = 7
while i != 30000001:
    if len(game[lastNumber]) > 1:
        lastNumber = game[lastNumber][-1] - game[lastNumber][-2]
    else:
        lastNumber = 0
    
    if lastNumber in game.keys():
        game[lastNumber].append(i)
    else:
        game[lastNumber] = [i]
    i +=1

print(lastNumber)