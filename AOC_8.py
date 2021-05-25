with open("aoc8.txt") as file1:
    initialInputData = file1.read().splitlines()


def play(inputData):
    acc = 0
    visited = []
    pointer = 0
    run = True
    while run:
        if pointer >= len(inputData):
            print('Terminated')
            print(acc)
            run = False
            return 'Terminated'
        if pointer in visited:
            return 'Infinite'
        command = inputData[pointer]
        if 'nop' in command:
            pointer += 1
        elif 'acc' in command:
            if pointer in visited:
                run = False
                return 'Infinite'
            else:
                acc += int(command.split(' ')[1])
                visited.append(pointer)
                pointer += 1
        elif 'jmp' in command:
            visited.append(pointer)
            pointer += int(command.split(' ')[1])
    return 'Infinite'

play(initialInputData)

keepTrying = True
tried = []
pointer = 0
while keepTrying:
    if pointer not in tried and pointer < len(initialInputData):
        entry = initialInputData[pointer]
        if 'nop' in entry:
            newInput = initialInputData.copy()
            newInput[pointer] = newInput[pointer].replace('nop', 'jmp')
            runnedGame = play(newInput)
            if runnedGame == 'Terminated':
                keepTrying = False
            else:
                tried.append(pointer)
                pointer += 1
        elif 'jmp' in entry:
            newInput = initialInputData.copy()
            newInput[pointer] = newInput[pointer].replace('jmp', 'nop')
            if play(newInput) == 'Terminated':
                keepTrying = False
            else:
                tried.append(pointer)
                pointer += 1
        else:
            pointer += 1
    else:
        keepTrying = False
