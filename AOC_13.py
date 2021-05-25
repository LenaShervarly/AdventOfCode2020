with open("aoc13.txt") as file1:
    puzzleInput = file1.read().splitlines() 

eDep = int(puzzleInput[0]) 
buses = puzzleInput[1].split(',')

minWaiting =  1000000000
result = 0
for bus in buses:
    if bus != 'x':
        waiting = int(bus) - (eDep % int(bus) )  
        if minWaiting > waiting:
            minWaiting = waiting
            result = int(bus) * waiting

print(result)

#part 2
i =  int(100000000000000 / 95060173) * 95060173 - 29
# buses coming at the same time
#95060173 = 577  *29 *13 *19 *23 
#15499189 = 601 *37 *17 *41

run = True
while run:
    if (i+60) % 15499189 == 0:
        run = False
        print(i)
    i += 95060173

