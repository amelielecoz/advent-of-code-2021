with open("input-day-2.txt", "r") as fp:
    commands= fp.readlines()

# First problem
startingPosition = [0,0] #[x, depth]

def forward(x, position):
    position[0] += int(x)
    return position

def down(y, position):
    position[1] += int(y)
    return position

def up(y, position):
    position[1] -= int(y)
    return position

position = startingPosition


for command in commands:
    action, value = command.split(" ")
    if action == 'forward':
        position = forward(value, position)
    elif action == 'up':
        position = up(value, position)
    elif action == 'down':
        position = down(value, position)

solution = position[0] * position[1]
print(f"Solution 1: { solution}\n")



# Second problem
startingPosition = [0, 0, 0] #[x, depth, aim]

def forwardWithAim(x, position):
    position[0] += int(x)
    position[1] += int(position[2]) * int(x)
    return position

def downWithAim(y, position):
    position[2] += int(y)
    return position

def upWithAim(y, position):
    position[2] -= int(y)
    return position

position = startingPosition

for command in commands:
    action, value = command.split(" ")
    if action == 'forward':
        position = forwardWithAim(value, position)
    elif action == 'up':
        position = upWithAim(value, position)
    elif action == 'down':
        position = downWithAim(value, position)

solution = position[0] * position[1]

print(f"Solution 2: {solution}\n")