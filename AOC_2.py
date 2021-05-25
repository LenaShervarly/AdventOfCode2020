with open("aoc2.txt") as file1:
    passwordsList = file1.read().splitlines() 

validPasswordsCounter = 0
validPasswordsCounter2 = 0
for passValData in passwordsList:
    policy = passValData.split()
    appearenceFrequancy = policy[0].split('-')
    min = int(appearenceFrequancy[0]) -1
    max = int(appearenceFrequancy[1]) -1
    letter = policy[1].replace(':','')
    password = policy[2]

    letterCounter = 0
    for j in password:       
        if j == letter:
            letterCounter += 1
    if(letterCounter >= min and letterCounter <= max):
        validPasswordsCounter = validPasswordsCounter+1

#part2
    if (letter == password[min]) ^ (letter == password[max]) :
        validPasswordsCounter2 += 1 
print(validPasswordsCounter)
print(validPasswordsCounter2)

