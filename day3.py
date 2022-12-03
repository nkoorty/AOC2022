data = open("./AOC2022/data/day3data.txt", "r").read().split('\n')
print(data)
"""
sum = 0

for line in data:
    slice_1 = line[0:len(line)//2]
    slice_2 = line[len(line)//2:]

    set_1 = set(slice_1)
    set_2 = set(slice_2)

    common = set_1.intersection(set_2)

    if len(common) == 0:
        continue
    
    common = list(common)[0]

    temp_sum = 0

    if common.islower():
        temp_sum = ord(common) - ord('a') + 1
    elif common.isupper():
        temp_sum = ord(common) - ord('A') + 27

    sum += temp_sum
"""
sum = 0

for i in range(0,len(data)-2, 3):
    
    set_1 = set(data[i])
    set_2 = set(data[i+1])
    set_3 = set(data[i+2])

    common = set_1.intersection(set_2, set_3)

    if len(common) == 0:
        continue
    
    common = list(common)[0]

    print(common)

    temp_sum = 0

    if common.islower():
        temp_sum = ord(common) - ord('a') + 1
    elif common.isupper():
        temp_sum = ord(common) - ord('A') + 27

    sum += temp_sum

print(sum)