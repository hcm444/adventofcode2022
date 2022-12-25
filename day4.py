# Jacobus Burger (2022)


class Solution:
    def parse(self, filename):
        # break into an array of ints (each pair of 4 is one line)
        # eg: 2-4,6-8 => 2 4 6 8
        with open(filename, 'r') as file:
            assignments = [
                int(num)
                for line in file.readlines()
                for pair in line.strip('\n').split(',')
                for num in pair.split('-')
            ]
            return assignments


    def part1(self, filename="day4.txt"):
        # the most straightforward approach is to create a range
        #   and then check for membership of all elements of one
        #   in the other.
        assignments = self.parse(filename)
        total = 0
        for i in range(0, len(assignments), 4):
            start_a, end_a, start_b, end_b = assignments[i:i+4]
            A = range(start_a, end_a)
            B = range(start_b, end_b)
            total += all(a in B for a in A) or all(b in A for b in B)
        return total


    def part2(self, filename="day4.txt"):
        pass





day4 = Solution()
solutions = [day4.part1(), day4.part2()]
print(solutions)



















# for show, not for use
class Alternative:
    def part1_logical(self, filename):
        # the alternative solution is mathematical range checking
        #   this can be expressed as a one-liner logical expression,
        #   but it's easier to read this way
        assignments = parse(filename)
        for assignment in assignments:
            # B falls within A
            if start_a <= start_b:
                total += end_b <= end_a
            # A falls within B
            if start_b <= start_a:
                total += end_a <= end_b
            # +0 if neither were the case
        return total
