with open("aoc1.txt") as file1:
    expenceReport = file1.read().splitlines() 
    print(expenceReport)
    
for i in range(len(expenceReport)):
    for j in range(1, len(expenceReport)):
        for k in range(2, len(expenceReport)):
            if int(expenceReport[i]) + int(expenceReport[j]) + int(expenceReport[k]) == 2020:
                print (int(expenceReport[i]) * int(expenceReport[j]) * int(expenceReport[k]))