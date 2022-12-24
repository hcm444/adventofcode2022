# Jacobus Burger (2022)
from functools import reduce
from string import ascii_letters


class Solution:
    def __doc__(self):
        return """
        # Day 3

        ## Part 1

        ### Explanation

        Given a sack (string), I need to split it into two
        compartments (strings) and determine what item (character)
        they have in common, then get the priority value of that
        item, and add that together to get the total priority of all.

        To do this I just wrote a function to calculate the correct
        priority levels (a-z == 1-26, A-Z == 27-52). Then, iterating
        through every string, I use python's set intersection to find
        the common item, use the priority function to calculate the
        value, and then add it to a running total then return that total.

        ## Part 2

        ### Explanation

        To solve this, I take groups of 3 sacks at a time and
        find the intersection between all three of them with
        a reduce. Then add the priority value of the answer to the
        running total and return that running total.
    """


    def parse(self, filename="day3.txt"):
        with open(filename, 'r') as file:
            return [
                sack.strip('\n')
                for sack in file.readlines()
            ]


    def part1(self, filename="day3.txt"):
        sacks = self.parse(filename)
        total = 0
        for sack in sacks:
            # find common character (item type) in both compartments
            A = set(sack[:len(sack) // 2])  # compartment 1
            B = set(sack[len(sack) // 2:])  # compartment 2
            item = A.intersection(B).pop()  # common item

            # add common item type priority to total
            total += ascii_letters.index(item) + 1
        return total


    def part2(self, filename="day3.txt"):
        sacks = self.parse(filename)
        total = 0
        # iterate 3 sacks at a time (one group at a time)
        for i in range(0, len(sacks), 3):
            group = sacks[i:i + 3]
            badge = reduce(set.intersection, map(set, group)).pop()
            total += ascii_letters.index(badge) + 1
        return total





day3 = Solution()
solutions = [day3.part1(), day3.part2()]
print(solutions)
