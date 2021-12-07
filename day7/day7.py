from numpy import *


def part_one(crabs):
    print(sum([abs(c) - median(crabs) for c in crabs]))


def part_two(crabs):
    avg_1 = floor(mean(crabs))
    avg_2 = ceil(mean(crabs))

    fuel_1 = 0
    fuel_2 = 0
    for c in crabs:
        n1 = abs(avg_2 - c)
        n2 = abs(avg_1 - c)
        fuel_1 += (n1*(n1 + 1)/2)
        fuel_2 += (n2*(n2 + 1)/2)
    print(min(fuel_1, fuel_2))


with open("input.txt") as f:
    crabs = list(map(int, f.readline().strip().split(',')))

    part_one(crabs)
    part_two(crabs)
