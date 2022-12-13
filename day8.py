data = open("AOC2022/data/day8data.txt", "r").read().split('\n')


def checker(i, j, data):
    main = data[i][j]
    dir_count = 0
    # Check top
    for k in range(i):
        if data[i][k] >= main:
            break
        dir_count += 1
    # Check left 
    for k in range(j):
        if data[k][j] >= main:
            break
        dir_count += 1
    # Check right
    for k in range(len(data[0])-1, i, -1):
        if data[k][j] >= main:
            break
        dir_count += 1
    # Check bottom
    for k in range(j, len(data)):
        if data[i][k] >= main:
            break
        dir_count += 1

    if dir_count < 4:
        return True
    else:
        return False


def part_1(data):
    sum = 2*len(data)+ (2*len(data[0])-4)
    for i in range(1, len(data[0])-1):
        for j in range(1, len(data)-1):
            if checker(i,j,data) == True:
                sum += 1
    return sum


print(part_1(data))