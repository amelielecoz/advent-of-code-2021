with open("input.txt", "r") as fp:
    lines = fp.readlines()
vents = [i.split("\n")[0] for i in lines]

maxX = 0
maxY = 0

import numpy as np

def findMaxX(maxX, startX, endX):
    if (startX > maxX or endX > maxX):
        maxX = startX if startX > endX else endX
    return maxX

def findMaxY(maxY, startY, endY):
    if (startY > maxY or endY > maxY):
        maxY = startY if startY > endY else endY
    return maxY

def findStart(line):
    start = line.split(' -> ')[0]
    return start

def findEnd(line):
    end = line.split(' -> ')[1]
    return end

def findPointX(point):
    pointX = int(point.split(',')[0])
    return pointX

def findPointY(point):
    pointY = int(point.split(',')[1])
    return pointY

for vent in vents :
    start = findStart(vent)
    end = findEnd(vent)
    startX = findPointX(start)
    startY = findPointY(start)
    endX = findPointX(end)
    endY = findPointY(end)

    maxX = findMaxX(maxX, startX, endX)
    maxY = findMaxY(maxY, startY, endY)

map = np.zeros([maxX+10, maxY+10])

for vent in vents:
    start = findStart(vent)
    end = findEnd(vent)
    startX = findPointX(start)
    startY = findPointY(start)
    endX = findPointX(end)
    endY = findPointY(end)
    if(startY == endY):
        if(startX < endX):
            for i in range(startX, endX +1):
                map[startY][i] += 1
        else:
            for i in range(endX, startX +1):
                map[startY][i] += 1
    elif(startX == endX):
        if(startY < endY):
            for i in range(startY, endY + 1):
                map[i][startX] += 1
        else:
            for i in range(endY, startY+1):
                map[i][startX] += 1

# print(map)

print(f'Solution 1 : {len(map[map >= 2])}')

# Be careful on how you create list of lists, they must not point to the same ref !