data = open("./AOC2022/data/day2data.txt", "r").read().split('\n')

"""
Part 1

for line in data:
    if line[0] == "A":
        if line[-1] == "X":
            sum += 1
            sum += 3
        elif line[-1] == "Y":
            sum += 2
            sum += 6
        elif line[-1] == "Z":
            sum += 3

    elif line[0] == "B":
        if line[-1] == "X":
            sum += 1
        elif line[-1] == "Y":
            sum += 2
            sum += 3
        elif line[-1] == "Z":
            sum += 3
            sum += 6

    elif line[0] == "C":
        if line[-1] == "X":
            sum += 1
            sum += 6
        elif line[-1] == "Y":
            sum += 2
        elif line[-1] == "Z":
            sum += 3
            sum += 3
"""
# Part 3

sum = 0

for line in data:
    if line[0] == "A":
        if line[-1] == "X":
            sum += 3
        elif line[-1] == "Y":
            sum += 1
            sum += 3
        elif line[-1] == "Z":
            sum += 2
            sum += 6

    elif line[0] == "B":
        if line[-1] == "X":
            sum += 1
        elif line[-1] == "Y":
            sum += 2
            sum += 3
        elif line[-1] == "Z":
            sum += 3
            sum += 6

    elif line[0] == "C":
        if line[-1] == "X":
            sum += 2
        elif line[-1] == "Y":
            sum += 3
            sum += 3
        elif line[-1] == "Z":
            sum += 1
            sum += 6
        
print(sum)

sum = 0
