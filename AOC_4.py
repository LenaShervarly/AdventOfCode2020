import re

with open("aoc4.txt") as file1:
    puzzleInput = file1.read().splitlines() 

passp = {}
valid = 0
validationFields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
def yearVal(year, min, max):
    return len(year) == 4 and (int(year) >= min) and (int(year) <= max)

def heightVal(height):
    validHeight = re.split("(cm$)|(in$)", height)
    if validHeight is not None and len(validHeight) > 1:
        return (validHeight[1] == 'cm' and int(validHeight[0]) >= 150 and int(validHeight[0]) <= 193) or (validHeight[2] == 'in' and int(validHeight[0]) >= 59 and int(validHeight[0]) <= 76) 
    return False

def hairColVal(color):
    return re.search("^#[0-9a-f]{6}$", color) is not None

def eyeVal(color):
    return color in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

def pidVal(pid):
    return re.search("^[0-9]{9}$", pid) is not None

for input in puzzleInput:
    line = input.split()
    if line:
        for j in range(len(line)):
            field = line[j].split(':')
            passp[field[0]] = field[1]
    else :
        if not set(validationFields) - passp.keys() :
            if yearVal(passp["byr"], 1920, 2002) and yearVal(passp["iyr"], 2010, 2020) and yearVal(passp["eyr"], 2020, 2030) and heightVal(passp["hgt"]) and hairColVal(passp["hcl"]) and eyeVal(passp["ecl"]) and pidVal(passp["pid"]):
                valid += 1
        passp.clear()
print(valid)
