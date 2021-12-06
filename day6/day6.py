def calculate_fish_population(initial_fish, days):
    count = [initial_fish.count(x) for x in range(9)]
    for day in range(days):
        count.append(count.pop(0))
        count[6] += count[8]
    print(sum(count))


with open("input.txt") as f:
    fish = list(map(int, f.readline().strip().split(",")))
    calculate_fish_population(fish, 256)
