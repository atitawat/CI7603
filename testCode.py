lines = []
with open('in.txt', 'r') as f:
    for line in f:
        lines.append(line.rstrip())

print(lines)