# Jacobus Burger (2022)


class Solution:
    def parse(self, filename):
        pass


    def part1(self, filename="day3.txt"):
        # the most straightforward approach is to create a range
        #   and then check for membership of all elements of one
        #   in the other.
        assignments = parse(filename)
        for assignment in assignments:
            A = range(start_a, end_a)
            B = range(start_b, end_b)
            total += all(a in B for a in A) or all(b in A for b in B)
        return total


    def part2(self, filename="day3.txt"):
        pass





day4 = Solution()
solutions = [day4.part1(), day4.part2()]
print(solutions)



















class Alternative:
    def part1_logical(self, filename):
        

    def part1_alt(self, filename="day3.txt"):
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
