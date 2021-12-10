
def part_one(lines):
    count = 0
    segments = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]

    for line in lines:
        for word in line[1]:
            l = len(word)
            if l == segments[1] or l == segments[4] or l == segments[7] or l == segments[8]:
                count += 1

    print(count)


def part_two(lines):
    segments = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]
    sum = 0
    for line in lines:
        line_sum = 0
        for index, word in enumerate(line[1]):
            multiplier = 10**(3 - index)
            # Do the easy cases first
            l = len(word)
            if l == segments[1]:
                line_sum += 1 * multiplier
            elif l == segments[4]:
                line_sum += 4 * multiplier
            elif l == segments[7]:
                line_sum += 7 * multiplier
            elif l == segments[8]:
                line_sum += 8 * multiplier

            # Case between 0, 6 and 9 , the 0/9 must contain the same segments used in 1
            elif l == 6:
                for pattern in line[0]:
                    if len(pattern) == 2:
                        # Found the 1, now check if word contains the same letters
                        if pattern[0] in word and pattern[1] in word:
                            # It is a 0 or 9
                            # 4 must have all of its segments in 9
                            for w in line[0]:
                                if len(w) == 4:
                                    nine = True
                                    for letter in word:
                                        if letter not in w:
                                            # It is a 0
                                            nine = False
                                            break
                                    if not nine:
                                        line_sum += 9 * multiplier
                                    break
                        else:
                            # It is a 6
                            line_sum += 6 * multiplier
            # Case between 2, 3, 5 which all have 5 segments
            else:
                # The segments in 1 is in 3, but not in 2 or 5
                for pattern in line[0]:
                    if len(pattern) == 2:
                        if pattern[0] in word and pattern[1] in word:
                            line_sum += 3 * multiplier
                        else:
                            # It is a 2 or 5
                            # A 5 shares all of its segments with 6
                            for w in line[0]:
                                if len(w) == 6:
                                    found = False
                                    # Ignore if it's a 0 or 9
                                    if pattern[0] in w and pattern[1] in w:
                                        # It is a 0
                                        found = True
                                    else:
                                        # We found the 6
                                        five = True
                                        for letter in word:
                                            if letter not in w:
                                                # It is a 2
                                                line_sum += 2 * multiplier
                                                five = False
                                                found = True
                                        if five:
                                            line_sum += 5 * multiplier
                                            break
        sum += line_sum
    print(f"{sum}")


with open("input.txt") as f:
    lines = [[word.split(" ") for word in line.split(" | ")]
             for line in list(map(str.strip, f.readlines()))]

    # part_one(lines)
    part_two(lines)
