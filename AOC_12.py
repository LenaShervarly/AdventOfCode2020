import math

with open("aoc12.txt") as file1:
    puzzleInput = file1.read().splitlines() 

coordinates = []
for line in puzzleInput:
    direction = line[0:1]
    value = int(line[1:])
    coordinate = [direction, value]
    coordinates.append(list(coordinate))

NS = 0
EW = 0
facing = 180
for coordinate in coordinates:
    if coordinate[0] == 'N':
        NS += coordinate[1]
    elif coordinate[0] == 'S':
        NS -= coordinate[1]
    elif coordinate[0] == 'E':
        EW += coordinate[1]
    elif coordinate[0] == 'W':
        EW -= coordinate[1]
    elif coordinate[0] == 'L':
        facing -= coordinate[1]
    elif coordinate[0] == 'R':
        facing += coordinate[1]
    elif coordinate[0] == 'F':
        if facing % 360 == 0: # 'W':
            EW -= coordinate[1]
        elif facing % 360 == 180: # 'E':
            EW += coordinate[1]
        elif facing % 360 == 270: #'S':
            NS -= coordinate[1]
        elif facing % 360 == 90: #'N':
            NS += coordinate[1]

print(abs(NS) + abs(EW))

#part 2

NS = 1
EW = 10
ShipNS = 0
ShipEW = 0
facing = 180
for coordinate in coordinates:
    if coordinate[0] == 'N':
        NS += coordinate[1]
    elif coordinate[0] == 'S':
        NS -= coordinate[1]
    elif coordinate[0] == 'E':
        EW += coordinate[1]
    elif coordinate[0] == 'W':
        EW -= coordinate[1]
    elif coordinate[0] == 'L': 
        angle = math.pi / 180 * (360- coordinate[1])
        tmpE = EW
        EW = round(EW * math.cos(angle) + NS * math.sin(angle))
        NS = - round(tmpE * math.sin(angle) - NS * math.cos(angle))

    elif coordinate[0] == 'R':
        angle = math.pi / 180 * coordinate[1]
        tmpE = EW
        EW = round(EW * math.cos(angle) + NS * math.sin(angle))
        NS = - round(tmpE * math.sin(angle) - NS * math.cos(angle))

    elif coordinate[0] == 'F':
        ShipEW += coordinate[1]*EW
        ShipNS += coordinate[1]*NS

print(abs(ShipNS) + abs(ShipEW))