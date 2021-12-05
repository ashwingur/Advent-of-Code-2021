def part_one(lines, max):
    grid = [[0 for cell in range(max + 1)] for row in range(max + 1)]
    for line in lines:
        a = line[0]
        b = line[1]
        if a[0] == b[0]:
            # Row is the same
            if a[1] - b[1] > 0:
                a = line[1]
                b = line[0]
            for i in range(b[1] - a[1] + 1):
                grid[a[0]][a[1] + i] += 1
        elif a[1] == b[1]:
            # Column is the same
            if a[0] - b[0] > 0:
                a = line[1]
                b = line[0]
            for i in range(b[0] - a[0] + 1):
                grid[a[0] + i][a[1]] += 1
    overlap = 0
    for row in grid:
        for cell in row:
            if cell > 1:
                overlap += 1
    return overlap


def part_two(lines, max):
    grid = [[0 for cell in range(max + 1)] for row in range(max + 1)]
    for line in lines:
        a = line[0]
        b = line[1]
        delta = [0, 0]
        r = 0
        if a[0] == b[0]:
            # Row is the same
            if a[1] - b[1] > 0:
                delta[1] = -1
            else:
                delta[1] = 1
            r = abs(b[1] - a[1]) + 1
        elif a[1] == b[1]:
            # Column is the same
            if a[0] - b[0] > 0:
                delta[0] = -1
            else:
                delta[0] = 1
            r = abs(b[0] - a[0]) + 1
        else:
            # Diagonal
            if a[0] - b[0] > 0:
                delta[0] = -1
            else:
                delta[0] = 1
            if a[1] - b[1] > 0:
                delta[1] = -1
            else:
                delta[1] = 1
            r = abs(a[0] - b[0]) + 1
        for i in range(r):
            grid[a[0] + delta[0] * i][a[1] + delta[1] * i] += 1

    overlap = 0
    for row in grid:
        for cell in row:
            if cell > 1:
                overlap += 1
    return overlap


with open("input.txt") as f:
    lines = []
    line = f.readline()
    max = 0
    while line:
        l = line.strip().split(" -> ")
        a = list(map(int, l[0].split(',')))
        if a[0] > max:
            max = a[0]
        if a[1] > max:
            max = a[1]
        b = list(map(int, l[1].split(',')))
        if b[0] > max:
            max = b[0]
        if b[1] > max:
            max = b[1]
        lines.append((a, b))
        line = f.readline()

    print(part_one(lines, max))
    print(part_two(lines, max))
