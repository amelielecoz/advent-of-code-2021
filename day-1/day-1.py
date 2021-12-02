with open("input-day-1.txt", "r") as fp:
    lineInput = fp.readlines()
lineInput = [int(i.split("\n")[0]) for i in lineInput]

# First problem
total = 0
for i in range(len(lineInput) -1):
    if lineInput[i] < lineInput[i+1]:
        total+=1
print(f"Solution 1:{total}\n")


# Second problem
total2 = 0
for i in range(len(lineInput)-3):
    if lineInput[i] != 0:
        sumA = lineInput[i] + lineInput[i+1] + lineInput[i+2]
        sumB = lineInput[i+1] + lineInput[i+2] + lineInput[i+3]
        if sumB > sumA:
            total2+=1

print(f"Solution 2:{total2}")