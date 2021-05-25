with open("aoc14.txt") as file1:
    puzzleInput = file1.read().splitlines()

memory = {}
mask = []
for line in puzzleInput:
    command =  line.split(' = ')
    if 'mask' in line:
        mask.clear()
        for symbol in command[1]:
            mask.append(symbol)
        mask.reverse()
    else:
        newValue = int(command[1])
        for i in range(len(mask)):
            if mask[i] == '1':
                newValue |= (1<<i) 
            elif mask[i] == '0':
                newValue &= (~(1<<i))
        memory[command[0]] = int(newValue)

#print(sum(memory.values()))

#part 2

memory = {}
mask = []
for line in puzzleInput:
    command =  line.split(' = ')
    if 'mask' in line:
        mask.clear()
        for symbol in command[1]:
            mask.append(symbol)
        mask.reverse()
    else:
        newValue = int(command[1])
        address = int(command[0].replace('mem[', '').replace(']', ''))
        for i in range(len(mask)):
            if mask[i] == '1':
                address |= (1<<i) 
        for i in range(pow(2, mask.count('X'))):
            copyAddress = address
            j = 0
            for k in range(len(mask)):
                if mask[k] == 'X':
                    if (((i >> j) & 1)) == 1:
                        copyAddress |= (1<<k)
                    else:
                        copyAddress &= (~(1<<k))
                    j +=1
                    memory[copyAddress] = int(newValue)

#print(memory)
print(sum(memory.values()))
