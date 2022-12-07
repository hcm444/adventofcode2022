# Jacobus Burger (2022)


class Solution:
    def part1(file="day1.txt"):
        # parse the items into a nested list of inventories
        # sum them together
        # then choose the greatest of all the groups with max
        return max(
            [
                sum(map(int, items.strip().split('\n')))
                for items in open(file, 'r').read().split("\n\n")
            ]
        )


    def part2(file="day1.txt"):
        # parse the items into a nexted list of inventories
        # then we take a slice of the biggest 3 and get the total
        calories = [
            sum(map(int, items.strip().split('\n')))
            for items in open(file, 'r').read().split("\n\n")
        ]
        calories.sort(reverse=True)
        return sum(calories[:3])
