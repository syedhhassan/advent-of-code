wrapper = 0
ribbon = 0

with open("data.txt", "r") as f:
    for line in f:
        line = line.strip()    
        length, width, height = sorted(list(map(int, line.split("x"))))
        wrapper += 2 * (length * width + width * height + height * length) + length * width
        ribbon += 2 * (length + width) + length * width * height 

print(wrapper)
print(ribbon)