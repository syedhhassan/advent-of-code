with open("data.txt", "r") as f:
    data = f.read().strip()

floor = 0
basement = None
for i, char in enumerate(data):
    if char == '(':
        floor += 1
    elif char == ')':
        floor -= 1
    else:
        raise ValueError(f"Invalid character: {char}")
    if floor == -1 and basement is None:
            basement = i + 1    

print(floor)
print(basement)
