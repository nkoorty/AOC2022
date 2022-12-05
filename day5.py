data = open("./AOC2022/data/day5data.txt", "r").read().split('\n')

crates = []

# Load data
for i in range(1, 37, 4):
    temp = ""
    for j in range(7, -1, -1):
        if data[j][i] != ' ':
            temp += data[j][i]
    crates.append(temp)

def part_1(data):
    for i in range(10, len(data)):
        words = data[i].split(' ')
        count, fr, to  =  int(words[1]), int(words[3])-1, int(words[5])-1
        crates[to] += crates[fr][-count:][::-1]
        crates[fr] = crates[fr][:-count]

    ans = ""
    for crate in crates:
        ans += crate[-1]
    return ans

def part_2(data):
    for i in range(10, len(data)):
        words = data[i].split(' ')
        count, fr, to  =  int(words[1]), int(words[3])-1, int(words[5])-1
        crates[to] += crates[fr][-count:]
        crates[fr] = crates[fr][:-count]

    ans = ""
    for crate in crates:
        ans += crate[-1]
    return ans

print(part_1(data))
print(part_2(data))