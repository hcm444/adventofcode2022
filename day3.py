from collections import defaultdict
from functools import reduce
from itertools import islice
from string import ascii_letters

class Solution:
    def parse(self, filename="day3.txt"):
        with open(filename, 'r') as file:
            while True:
                lines = list(islice(file, 1000))
                if not lines:
                    break
                yield ''.join(lines).strip()

    def part1(self, filename="day3.txt"):
        counts = defaultdict(int)
        for sack in self.parse(filename):
            A = set(sack[:len(sack) // 2])  # compartment 1
            B = set(sack[len(sack) // 2:])  # compartment 2
            item = next(iter(A.intersection(B)))  # common item
            counts[item] += 1
        return sum(counts[item] * (ascii_letters.index(item) + 1) for item in counts)

    def part2(self, filename="day3.txt"):
        counts = defaultdict(int)
        for group in zip(*(self.parse(filename),) * 3):
            badge = next(iter(reduce(set.intersection, map(set, group))))
            counts[badge] += 1
        return sum(counts[item] * (ascii_letters.index(item) + 1) for item in counts)

day3 = Solution()
solutions = [day3.part1(), day3.part2()]
print(solutions)
