data = open("data/day6data.txt", "r").read()

def part_1(data):
    l, r = 0, 4
    for i in range(len(data)-3):
        if len(data[l:r]) == len(list(set(data[l:r]))):
            return r 
        else:
            l += 1
            r += 1

def part_2(data):
    l, r = 0, 14
    for i in range(len(data)-14):
        if len(data[l:r]) == len(list(set(data[l:r]))):
            return r 
        else:
            l += 1
            r += 1            

print(part_1(data))
print(part_2(data))