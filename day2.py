# Jacobus Burger (2022)


class Solution:
    def parse(self, filename):
        with open(filename, 'r') as f:
            strategies = [
                line.strip('\n').split()
                for line in f.readlines()
            ]
            return strategies


    def score(self, a, x):
        # calculate shape score
        shape = ord(x) - ord('X') + 1
        opponent = ord(a) - ord('A') + 1
        
        # score according to play
        # rock (1), paper (2), scissors (3)
        # 1 wins 2 wins 3 wins 1
        if opponent - shape == 1 or (opponent == 3 and shape == 1):
            return shape + 6
        if shape == opponent:
            return shape + 3
        if opponent - shape == -1 or (opponent == 1 and shape == 3):
            return shape


    def part1(self, filename):
        strategies = self.parse(filename)
        total_score = 0
        for strategy in strategies:
            total_score += self.score(strategy[0], strategy[1])
        return total_score


    def part2(self, filename):
        pass
