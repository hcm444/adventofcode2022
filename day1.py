# Jacobus Burger (2022)


class Solution:
    def __doc__(self):
        return """
        # Day 1

        ## Part 1 and 2

        This entire day was trivial. In both part 1 and 2 we just
        get the max calories from the list after summing all the
        calories for each elf. Finally, we return either the greatest
        number of calories or the sum of the three greatest.
    """


    def part1(self, file="day1.txt"):
        # return the max calories
        return max(
            [
                # sum all calories in each inventory
                sum(map(int, inventory.strip().split('\n')))
                # parse inventories
                for inventory in open(file, 'r').read().split("\n\n")
            ]
        )


    def part2(self, file="day1.txt"):
        # parse the inventories into a nexted list of inventories
        calories = [
            sum(map(int, inventories.strip().split('\n')))
            for inventories in open(file, 'r').read().split("\n\n")
        ]
        # then we take a slice of the biggest 3 and get the total
        calories.sort(reverse=True)
        return sum(calories[:3])
