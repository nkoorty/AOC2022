data = open("./AOC2022/data/day1data.txt", "r").read().split('\n')
# Part 1
maxi = 0
add = 0

for line in data:

    if line != '':
        add += int(line)
    
    else:
        maxi = max(maxi, add)
        add = 0


print(maxi)

# Part 2
maxi = 0
add = 0

arr = []

for line in data:

    if line != '':
        add += int(line)
    
    else:
        arr.append(add)
        add = 0

arr.sort(reverse=True)

print(sum(arr[0:3]))

