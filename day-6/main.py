with open("input.txt", "r") as fp:
    lines = fp.readlines()
lines = [i.split("\n")[0] for i in lines]
school = lines[0].split(',')

class Fish:
    def __init__(self, timer):
        self.timer = timer
        self.hasBaby = False

    def live(self):
        if(self.timer == 0):
            self.hasBaby = True
            self.initTimer()
        else:
            self.timer -= 1

    def initTimer(self):
        self.timer = 6

    def resetHasBaby(self):
        self.hasBaby = False

fishes = []
for individual in school:
    fish = Fish(int(individual))
    fishes.append(fish)

for day in range(256):
    for fish in fishes:
        fish.live()
        if (fish.hasBaby == True):
            fishes.append(Fish(9))
            fish.resetHasBaby()

print(f'Solution 1 : {len(fishes)}')