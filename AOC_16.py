with open("aoc16.txt") as file1:
    puzzleInput = file1.read().splitlines()

validation = {}
i = 0
note = puzzleInput[i]
while note :
    validInfo = note.split(': ')
    validation[validInfo[0]] = validInfo[1].split(' or ')
    i += 1
    note = puzzleInput[i]


nearbySeats = []
while 'nearby tickets:' not in note:
    i += 1
    note = puzzleInput[i]

yourTicket = puzzleInput[i-2].split(',')

for neigbour in puzzleInput[i+1:]:
    newNeigbour = list(map(int, neigbour.split(',')))
    nearbySeats.append(newNeigbour)

invalidSeats = []
InvalidNeigbours = []

for seats in nearbySeats:
    for seat in seats:
        valid = False
        i = 0
        vvals =  list(validation.values())
        while not valid and i < (len(vvals)):
            condition = vvals[i]
            if (seat >= int(condition[0].split('-')[0]) and seat <= int(condition[0].split('-')[1])) \
                or (seat >= int(condition[1].split('-')[0]) and seat <= int(condition[1].split('-')[1])):
                valid = True
            else:
                valid = False
            i +=1
        if not valid:
            invalidSeats.append(seat)
            InvalidNeigbours.append(seats)

print(sum(invalidSeats))
for neigbour in InvalidNeigbours:
    nearbySeats.remove(neigbour)

print()

noteIndexes= {}
for seats in nearbySeats:
    for j in range(len(seats)):
        vvals =  list(validation.items())
        for info in vvals:
            condition = info[1]
            if (seats[j] >= int(condition[0].split('-')[0]) and seats[j] <= int(condition[0].split('-')[1]) ) \
                or (seats[j] >= int(condition[1].split('-')[0]) and seats[j] <= int(condition[1].split('-')[1])):
                
                if info[0] in noteIndexes.keys():
                    if j in noteIndexes[info[0]].keys():
                        counter = noteIndexes[info[0]][j]
                        if counter > 0:
                            noteIndexes[info[0]][j] = counter+1
                    else:
                        noteIndexes[info[0]][j] = 1
                else:
                    noteIndexes[info[0]] = {j : 1}
            else:
                if info[0] in noteIndexes.keys():
                    if j in noteIndexes[info[0]].keys():
                        noteIndexes[info[0]][j] = -1
                    else:
                        noteIndexes[info[0]][j] = -1
                else:
                    noteIndexes[info[0]] = {j : -1}

for noteKey in noteIndexes:
    options = noteIndexes[noteKey]
    optionsToRemove = []
    for opt in options:
        if -1 == options[opt]:
            optionsToRemove.append(opt)
    for item in optionsToRemove:
        options.pop(item)

k=0
fixedValues = {}
optionsToRemove = set()
while len(fixedValues) < 20:
    for noteKey in noteIndexes:
        options = noteIndexes[noteKey]
        if len(options) == 1:
            optionsToRemove.add(list(options.keys())[0])
            fixedValues[noteKey] = options
        else:
            for item in optionsToRemove:
                if item in options:
                    options.pop(item)
    k+=1

depValues = {k: v for k, v in fixedValues.items() if k.startswith('departure')}
indexes = []
for val in depValues.values():
    for res in val:
        indexes.append(res)
multiply = []
for i in range(len(yourTicket)):
    if i in indexes:
        multiply.append(yourTicket[i])
result = 1
for m in multiply:
    result *= int(m)

print(result)