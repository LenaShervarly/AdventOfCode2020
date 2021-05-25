with open("aoc19.txt") as file1:
    puzzleInput = file1.read().splitlines()

rules = {}
i = 0
while puzzleInput[i]:
    rule = puzzleInput[i].split(':')
    rules[rule[0]] = rule[1]
    i += 1

messages = []
i += 1
while i < len(puzzleInput):
    messages.append(puzzleInput[i])
    i += 1

replaceToA = 0
replaceToB = 0
notValid = ['|', 'a', 'b']

possibleOptions = {}
def generateValidResults(rulesInput):

    if rulesInput in notValid:
        return
    subrules = rules[rulesInput].split(' ')[1:]
    generatedOptions = []

    for i in range(len(subrules)):
        if subrules[i]  != '|':
            if 'a' in rules[subrules[i]]: 
                possibleOptions[subrules[i]] = ['a']
            elif 'b' in rules[subrules[i]]:
                possibleOptions[subrules[i]] = ['b']

    if '|' in subrules:
        i= 0
        while subrules[i] != '|':
            i +=1
        generatedOptions.append(subrules[:i])
        generatedOptions.append(subrules[i+1:])
    else:
        generatedOptions.append(subrules)

    copyGeneratedOptions = []
    for i in range(len(generatedOptions)):
        option = generatedOptions[i] 
        if len(option) == 1:
            if option[0].isdigit() and option[0] not in possibleOptions:
                generateValidResults(option[0])
            for o in possibleOptions[option[0]]:
                copyGeneratedOptions.append(o)
        else:
            if option[0].isdigit() and option[0] not in possibleOptions:
                generateValidResults(option[0])
            if option[1].isdigit() and option[1] not in possibleOptions:
                generateValidResults(option[1])
        
            for suboptionJ in possibleOptions[option[0]]:
                for suboptionK in possibleOptions[option[1]]:
                    copyOption = option.copy()
                    copyOption[0] = suboptionJ
                    copyOption[1] = suboptionK
                    for m in range(len(copyOption)):
                        if copyOption[m].isdigit():
                            if 'a' in possibleOptions[copyOption[m]] :         
                                copyOption[m] = 'a'
                            elif 'b' in possibleOptions[copyOption[m]]:
                                copyOption[m] = 'b'

                    copyGeneratedOptions.append(''.join(copyOption))
    generatedOptions = copyGeneratedOptions
    possibleOptions[rulesInput] = set(generatedOptions)

#part 1
#generateValidResults('0')

def intersection(lst1, lst2): 
    lst3 = [value for value in lst1 if value in lst2] 
    return lst3 

#print(len(intersection(messages, possibleOptions['0'])))

#part 2
generateValidResults('42')
generateValidResults('31')
N = len(list(possibleOptions['31'])[0])
#print(N)
#print(possibleOptions['31'])

valid = 0
for m in messages:
    pointer = N*2
    if m[:N] not in possibleOptions['42']:
        continue
    if m[N:N*2] not in possibleOptions['42']:
        continue
    if m[-N:] not in possibleOptions['31']:
        continue
    if len(m) %N != 0:
        continue
    if len(m) < N*3:
        continue
    else:
        am42 = 2
        am31 = 1
        found31 = False
        isValid = True
        while pointer < (len(m)-N):
            if m[pointer:pointer+N] in possibleOptions['42']:
                am42 += 1
                if found31:
                    isValid = False
            elif m[pointer:pointer+N] in possibleOptions['31']:
                am31 += 1
                found31 = True
            else:
                isValid = False
            pointer +=8
        if am42 > am31 and isValid:
            valid +=1
print(valid)