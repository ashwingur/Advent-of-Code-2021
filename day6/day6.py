def calculate_fish_population(initial_fish, days):
    count = [0 for x in range(9)]
    for f in initial_fish:
        count[f] += 1
    print(count)
    for day in range(days):
        new_fish = count[0]
        for i in range(1, 9, 1):
            count[i-1] = count[i]
        count[8] = new_fish
        count[6] += new_fish
    print(sum(count))


with open("input.txt") as f:
    fish = list(map(int, f.readline().strip().split(",")))
    calculate_fish_population(fish, 256)
