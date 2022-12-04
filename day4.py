import re

data = open("./AOC2022/data/day4data.txt", "r").read().split('\n')

sum = 0

def part_1(input):
    sum = 0
    for line in input:
        points = re.split(",|-", line)
        s1, e1, s2, e2 = [int(x) for x in points]
        if s1 <= s2 and e1 >= e2 or s2 <= s1 and e2 >= e1:
            sum += 1
    return sum

def part_2(input):
    sum = 0
    for line in input:
        points = re.split(",|-", line)
        s1, e1, s2, e2 = [int(x) for x in points]
        if s2 <= e1 and s1 <= e2:
            sum += 1
    return sum

print(part_1(data))
print(part_2(data))