# Jacobus Burger (2022)


# get the max number of calories from all the items of all the elves
def part1(file="day1.txt"):
    # we split the groups of items for each elf by \n\n
    # then we split the items of each elf by \n
    # then we convert that list of strings into ints and get their total
    # then we choose the greatest of all the groups with max
    return max(
        [
            sum(map(int, items.strip().split('\n')))
            for items in open(file, 'r').read().split("\n\n")
        ]
    )


def part2(file="day1.txt"):
    # we just sort the list comprehension from part 1
    calories = [
        sum(map(int, items.strip().split('\n')))
        for items in open(file, 'r').read().split("\n\n")
    ]
    calories.sort(reverse=True)
    # then we take a slice of the biggest 3 and get the total
    return sum(calories[:3])

