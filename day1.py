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
        # parse the items into a nested list of inventories
        # sum them together
        # then choose the greatest of all the groups with max
        return max(
            [
                sum(map(int, items.strip().split('\n')))
                for items in open(file, 'r').read().split("\n\n")
            ]
        )


    def part2(self, file="day1.txt"):
        # parse the items into a nexted list of inventories
        # then we take a slice of the biggest 3 and get the total
        calories = [
            sum(map(int, items.strip().split('\n')))
            for items in open(file, 'r').read().split("\n\n")
        ]
        calories.sort(reverse=True)
        return sum(calories[:3])


# less efficient in practice but maybe easier to read and understand
class ReadableSolution:
    def parse(self, file="day1.txt"):
        inventories = []
        with open(file, 'r') as f:
            for inventory in f.read().split("\n\n"):
                inventory = [
                    int(item)
                    for item in inventory.strip().split('\n')
                ]
                inventories.append(inventory)
        return inventories


    def part1(self, file="day1.txt"):
        inventories = ReadableSolutions.parse(file)
        calories = 0
        for inventory in inventories:
            inventory_calories = sum(inventory)
            if inventory_calories >= calories:
                calories = inventory_calories
        return calories


    def part2(self, file="day1.txt"):
        inventories = ReadableSolutions.parse(file)
        calories = [sum(inventory) for inventory in inventories]
        calories.sort(reverse=True)
        return sum(calories[:3])
