with open("aoc22.txt") as file1:
    puzzleInput = file1.read().splitlines()

pla1 = []
i = 1
while puzzleInput[i]:
    pla1.append(int(puzzleInput[i]))
    i += 1

pla2 = []
i += 2
while i < len(puzzleInput):
    pla2.append(int(puzzleInput[i]))
    i += 1




def play(player1, player2):
    roundPrintScreens = set()
    counter = 1
    while len(player1) > 0 and len(player2) > 0:
        prScreen = ''.join(str(player1) + str(player2))
        if prScreen in roundPrintScreens:
            return (True, player1)
        roundPrintScreens.add(prScreen)

        topCard1 = player1[0]
        topCard2 = player2[0]

        firstWon = False
        subgamePlayed = False
        if len(player1) > topCard1 and len(player2) > topCard2:
            # print('playing subgame')
            # print(player1[1:topCard1 +1])
            # print(player2[1:topCard2+1])
            # print()
            subgamePlayed = True
            firstWon = play(player1[1:topCard1+1].copy(), player2[1:topCard2+1].copy())[0]
        player1.pop(0)
        player2.pop(0)
        
        winnerIs1 = False
        if subgamePlayed:
            winnerIs1 = firstWon
        else:
            winnerIs1 = topCard1 > topCard2

        if winnerIs1:
            player1.append(topCard1)
            player1.append(topCard2)
        else:
            player2.append(topCard2)
            player2.append(topCard1)

        counter +=1
        # print('## next round ## ' + str(counter))
        # print(player1)
        # print(player2)
        # print()
    if len(player1) > 0:
        return (True, player1)
    return (False, player2)

multiplier = 1
sum = 0
winner = []
res = play(pla1, pla2)

winner = res[1]
winner.reverse()
for el in winner:
    sum += int(el) * multiplier
    multiplier +=1
print(sum)