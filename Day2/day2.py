import sys

valid = 0
for line in sys.stdin:
    line.strip()
    parts = line.split(" ")
    ranges = parts[0]
    ranges = ranges.split("-")

    # subtract 1 for 0 indexing
    pos1 = int(ranges[0]) - 1
    pos2 = int(ranges[1]) - 1
    character = parts[1][:-1]
    password = parts[2]

    count = 0
    for (i, c) in enumerate(password):
        if c == character and (i == pos1 or i == pos2):
            count += 1

    if count == 1:
        valid += 1

print(valid)
