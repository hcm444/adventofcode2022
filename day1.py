# Jacobus Burger (2022)


# the solutions I used
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


# less efficient in practice but maybe easier to read and understand
class ReadableSolution:
    def parse(file="day1.txt"):
        inventories = []
        with open(file, 'r') as f:
            for inventory in f.read().split("\n\n"):
                inventory = [
                    int(item)
                    for item in inventory.strip().split('\n')
                ]
                inventories.append(inventory)
        return inventories


    def part1(file="day1.txt"):
        inventories = ReadableSolutions.parse(file)
        calories = 0
        for inventory in inventories:
            inventory_calories = sum(inventory)
            if inventory_calories >= calories:
                calories = inventory_calories
        return calories


    def part2(file="day1.txt"):
        inventories = ReadableSolutions.parse(file)
        calories = [sum(inventory) for inventory in inventories]
        calories.sort(reverse=True)
        return sum(calories[:3])
