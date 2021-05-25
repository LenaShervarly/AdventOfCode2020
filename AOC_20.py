with open("aoc20.txt") as file1:
    inp = file1.read().splitlines()

i = 0
tiles = {}
matching = {}
while i < len(inp)-12: 
    if 'Tile' in inp[i]:
        key = inp[i].split(' ')[1].replace(':', '')
        tiles[key] = [str(inp[i+1])]
        matching[key] = []
    b1 = ''
    b2 = ''
    for j in range(1, 11):
        b1 += inp[i + j][0]
        b2 += inp[i + j][len(inp[i]) - 1]
    a2 = inp[i + 10]
    tiles[key].append(b1)
    tiles[key].append(a2)
    tiles[key].append(b2)

    i +=12

for t in tiles:
    for i in range(4):
        l = list(tiles[t][i])
        l.reverse()
        reversedSide = ''.join(l)
        tiles[t].append(reversedSide)

for key1 in tiles:
    for ke2 in tiles:
        if key1 == ke2:
            continue
        match = [val for val in tiles[key1] if val in tiles[ke2]]
        if len(match) > 0:
            for el in match:
                matching[key1].append(el)

res = []
for el in matching:
    if len(set(matching[el])) == 4:
        res.append(el)
print(res)

mult = 1
for i in res:
    mult *= int(i)
print(mult)

count = 0
for i in range(len(inp)):
    if inp[i] != '' and 'Tile' not in inp[i]:
        for j in inp[i]:
            if j == '#':
                count += 1

rem = 0
for sides in tiles.values():
    for s in sides:
        for i in s:
            if i == '#':
                rem += 1
#   print(count)

i = 0
borders = 0
while i < len(inp)-12: 
    if 'Tile' in inp[i]:
        borders += len([t for t in inp[i+1] if t == '#'])

    for j in range(2, 10):
        if inp[i + j][0] == '#':
            borders += 1
        if inp[i + j][len(inp[i]) - 1] == '#':
            borders += 1
    borders += len([t for t in inp[i+10] if t == '#'])
    i +=12
    
print(count - borders - 34*15)
#4928
#2346 - 303
       #- 2

