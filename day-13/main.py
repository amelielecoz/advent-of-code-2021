with open("input", "r") as fp:
    lines = fp.readlines()
rows = [i.split("\n")[0] for i in lines]

# print(rows)
# print(len(rows))

import numpy as np
matrice = []

stop = False

maxX = 0
maxY = 0
for row in rows :
    if row == '':
        stop = True
    if stop == False:
        x = int(row.split(',')[0])
        y = int(row.split(',')[1])
        if x>maxX:
            maxX = x
        if y>maxY:
            maxY = y


map = np.zeros((maxY+1, maxX+1))

instructions = []
stop = False
foldedOnce = False
for row in rows :
    if row == '':
        stop = True
    if stop == False:
#         print(row)
        x = int(row.split(',')[0])
        y = int(row.split(',')[1])
        map[y][x] += 1
#         print(map)
    if stop == True:
        if row != '':
            instruction = row.split('=')
            axis = instruction[0][-1]
            lineNumber = int(instruction[1])
            instructions.append([axis, lineNumber])

for index, instruction in enumerate(instructions):
    if 'y' == instruction[0] :
          first = map[0:instruction[1]]
          second = map[instruction[1]+1:]
          second_reversed = np.flip(second, axis=0)
          map = first + second_reversed
    elif 'x' == instruction[0] :
          first = map[0:, 0:instruction[1]]
          second = map[0:, instruction[1]+1:]
          second_reversed = np.flip(second, axis=1)
          map = first + second_reversed
    if index == 0:
        sum = np.count_nonzero(map)

print(f"Solution 1 : {sum}")
print("Solution 2 : ")
for y in range(6):
    for x in range(40):
        if map[y][x]!= 0:
            print('█', end="")
        else:
            print('.', end="")
    print()
