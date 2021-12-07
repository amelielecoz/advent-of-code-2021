with open("input", "r") as fp:
    lines = fp.readlines()
lines = [i.split("\n")[0] for i in lines]
crabs = lines[0].split(',')

crabs = [int(i) for i in crabs]
import statistics
median = statistics.median(crabs)

sum = 0

for crab in crabs:
    if crab > median:
        sum += (crab - median)
    else:
        sum += (median - crab)
# print(median)
print(f"Solution 1: {sum}")

mean = statistics.mean(crabs)
print(mean)

mean = 483
print(mean)

mean_sum = 0
for crab in crabs:
    if crab > mean:
        for i in range(crab - mean + 1):
            mean_sum += i
    else:
        for i in range(mean - crab + 1):
            mean_sum += i

print(f"Solution 2: {mean_sum}")

#Time : 35 min