def calculate_fish_population(initial_fish, days):
    count = [0 for x in range(9)]
    for f in initial_fish:
        count[f] += 1
    for day in range(days):
        count.append(count.pop(0))
        count[6] += count[8]
    print(sum(count))


with open("input.txt") as f:
    fish = list(map(int, f.readline().strip().split(",")))
    calculate_fish_population(fish, 256)
