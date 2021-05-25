with open("aoc18.txt") as file1:
    puzzleInput = file1.read().splitlines()

def intTryParse(value):
    try:
        int(value)
        return  True
    except:
        return  False


def calculate(equazion):
    if intTryParse(equazion):
        return int(equazion)
    else: 
        braceCounter = equazion.count('(')
        if braceCounter >= 1:
            innerEquasion = ''
            i = 0
            while equazion[i] != '(':
                i += 1
            start = i
            i += 1
            while equazion[i] != ')':
                if equazion[i] == '(':
                    start = i
                    innerEquasion = ''
                else:
                    innerEquasion += equazion[i]
                i += 1
            return calculate(equazion[:start] + str(calculate(innerEquasion)) + equazion[i+1:])
        
        nEq = equazion.split(' ')
        res = int(nEq[0])
        currentOperator = nEq[1]
        j = 2
        while j < len(nEq):
            if nEq[j].isdigit():
                if currentOperator == '*':
                    res *= int(nEq[j])
                elif currentOperator == '+':
                    res += int(nEq[j])
            else:
                currentOperator = nEq[j]
            j+=1
        return res


def calculatePart2(equazion):
    if intTryParse(equazion):
        return int(equazion)
    else: 
        if equazion.count('(') >= 1:
            innerEquasion = ''
            i = 0
            while equazion[i] != '(':
                i += 1
            start = i
            i += 1
            while equazion[i] != ')':
                if equazion[i] == '(':
                    start = i
                    innerEquasion = ''
                else:
                    innerEquasion += equazion[i]
                i += 1
            return calculatePart2(equazion[:start] + str(calculatePart2(innerEquasion)) + equazion[i+1:])
        
        nEq = equazion.split(' ')
        i = 0
        while nEq.count('+') > 0:
            while nEq[i] != '+':
                i += 1
            additionRes = int(nEq[i-1]) + int(nEq[i+1])
            nEq.pop(i+1)
            nEq.pop(i)
            nEq.pop(i-1)
            nEq.insert(i-1, additionRes)

        res = int(nEq[0])
        j = 2
        while j < len(nEq):
            res *= int(nEq[j])
            j+=2
        return res

totalSum = 0
for equazion in puzzleInput:
    totalSum += calculatePart2(equazion)
print(totalSum)