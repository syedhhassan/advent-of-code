with open("data.txt", "r") as f:
    data = f.read().strip()

positions = {(0, 0)}
combined_positions = {(0, 0)}
og_position, santa, robo_santa = (0, 0), (0, 0), (0, 0)

def move(position, direction):
    x, y = position
    return (x + (direction == ">") - (direction == "<"), y + (direction == "^") - (direction == "v"))

for i, direction in enumerate(data):
    og_position = move(og_position, direction)
    positions.add(og_position)
    if i % 2 == 0:
        santa = move(santa, direction)
        combined_positions.add(santa)
    else:
        robo_santa = move(robo_santa, direction)
        combined_positions.add(robo_santa)

print(len(positions))
print(len(combined_positions))