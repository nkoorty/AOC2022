data = open("./AOC2022/data/day2data.txt", "r").read().split('\n')

total = 0

outcomes = {
    "A X":4, "A Y":8, "A Z":3,
    "B X":1, "B Y":5, "B Z":9,
    "C X":7, "C Y":2, "C Z":6
}
        
for line in data:
    total += outcomes[line]

total2 = 0

outcomes2 = {
    "A X":3, "A Y":4, "A Z":8,
    "B X":1, "B Y":5, "B Z":9,
    "C X":2, "C Y":6, "C Z":7
}    

for line in data:
    total2 += outcomes2[line]

print(f"The total for Part 1 is: {total}")
print(f"The total for Part 2 is: {total2}")
