with open("input.txt", "r") as fp:
    lines = fp.readlines()
lines = [i.split("\n")[0] for i in lines]
school = lines[0].split(',')

ocean = [0] * 9

for individual in school:
    ocean[int(individual)] +=1

newborn = 0
for day in range(256):
    newborn = ocean[0]
    for x in range(len(ocean)):
        if(x > 0):
            ocean[x-1] = ocean[x]
    ocean[6] += newborn
    ocean[8] = newborn
    newborn = 0
print(sum(ocean))

def sum(array):
    sum = 0
    for item in array:
        sum += int(item)
    return sum

#Main concept : linearisation into a size-9 array instead of counting ALL the fishes
#Spent time : 2h+