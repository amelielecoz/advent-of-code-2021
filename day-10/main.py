with open("input", "r") as fp:
    lines = fp.readlines()
rows = [i.split("\n")[0] for i in lines]

print(rows)

set1 = ['(', ')', 3, 1]
set2 = ['[', ']', 57, 2]
set3 = ['{', '}', 1197, 3]
set4 = ['<', '>', 25137, 4]

sum = 0
print(rows)
print(len(rows))
rowsToDiscard = []
for row in rows :
    setOfOpenings = []
    for x in row :
        if x == set1[0] or x == set2[0] or x == set3[0] or x == set4[0]:
#             print('opening tag :', x)
            setOfOpenings.append(x)
#             print(setOfOpenings)
        if x == set1[1]:

            if set1[0] == setOfOpenings[-1]:
                setOfOpenings.pop(-1)
#                 print(setOfOpenings)
            else :
                print('This has not opening ', x)
                sum += set1[2]
                rowsToDiscard.append(row)
                break

        if x == set2[1]:
            if set2[0] == setOfOpenings[-1]:
                setOfOpenings.pop(-1)
#                 print(setOfOpenings)
            else :
                print('This has not opening ', x)
                sum += set2[2]
                rowsToDiscard.append(row)
                break

        if x == set3[1]:
            if set3[0] == setOfOpenings[-1]:
                setOfOpenings.pop(-1)
#                 print(setOfOpenings)
            else :
                print('This has not opening ', x)
                sum += set3[2]
                rowsToDiscard.append(row)
                break

        if x == set4[1]:
            if set4[0] == setOfOpenings[-1]:
                setOfOpenings.pop(-1)
#                 print(setOfOpenings)
            else :
                print('This has not opening ', x)
                sum += set4[2]
                rowsToDiscard.append(row)
                break

rowsToDiscard
for row in rowsToDiscard:
    rows.remove(row)
print(rows)
print(sum)
arraySolution2 = []
missingCloses = []
for row in rows:
    setOfOpenings = []
    missing = []
    for x in row :
        if x == set1[0] or x == set2[0] or x == set3[0] or x == set4[0]:
            setOfOpenings.append(x)
        if x == set1[1]:
            if set1[0] == setOfOpenings[-1]:
                setOfOpenings.pop(-1)

        if x == set2[1]:
            if set2[0] == setOfOpenings[-1]:
                setOfOpenings.pop(-1)

        if x == set3[1]:
            if set3[0] == setOfOpenings[-1]:
                setOfOpenings.pop(-1)

        if x == set4[1]:
            if set4[0] == setOfOpenings[-1]:
                setOfOpenings.pop(-1)
    for opening in setOfOpenings:
        if(opening == set1[0]):
            missing.insert(0, set1[1])
        if(opening == set2[0]):
            missing.insert(0, set2[1])
        if(opening == set3[0]):
            missing.insert(0, set3[1])
        if(opening == set4[0]):
            missing.insert(0, set4[1])
    print(missing)
    sum = 0
    for x in missing:
        sum = (sum * 5)
        if(x == set1[1]):
            sum += set1[3]
        if(x == set2[1]):
            sum += set2[3]
        if(x == set3[1]):
            sum += set3[3]
        if(x == set4[1]):
            sum += set4[3]
    print(sum)
    arraySolution2.append(sum)

import statistics
median = statistics.median(arraySolution2)
print(median)
# solution 1: 45min
