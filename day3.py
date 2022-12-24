# Jacobus Burger (2022)


class Solution:
    def __doc__(self):
        return """
        # Day 3

        ## Part 1

        ### Explanation

        Given a rucksack (string), I need to split it into two
        compartments (strings) and determine what item (character)
        they have in common, then get the priority value of that
        item, and add that together to get the total priority of all.

        To do this I just wrote a function to calculate the correct
        priority levels (a-z == 1-26, A-Z == 27-52). Then, iterating
        through every string, I use python's set intersection to find
        the common item, use the priority function to calculate the
        value, and then add it to a running total.
    """


    def parse(self, filename="day3.txt"):
        with open(filename, 'r') as file:
            return [
                rucksack.strip('\n')
                for rucksack in file.readlines()
            ]


    # calculate priority level (a to z is 1 to 26, A to Z is 27 to 52)
    def priority(self, char):
        priority_level = ord(char) - ord('A') + 27
        if priority_level > 52:
            return priority_level - 52 - 6
        return priority_level


    def part1(self, filename="day3.txt"):
        rucksacks = self.parse()
        total = 0
        for rucksack in rucksacks:
            # find common character (item type) in both compartments
            A = set(rucksack[:len(rucksack) // 2])
            B = set(rucksack[len(rucksack) // 2:])
            item = A.intersection(B).pop()

            # calculate priority of the common item type
            total += self.priority(item)
        return total


    def part2(self):
        pass





day3 = Solution()
solutions = [day3.part1(), day3.part2()]
print(solutions)
