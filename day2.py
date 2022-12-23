# Jacobus Burger (2022)



class Solution:
    def __doc__(self):
        return """
        # Advent of code, day 2 solutions.

        I realized that I could map each move (rock, paper, scissors) to an
        accompanying value (1, 2, 3) and then use some basic arithmetic to
        determine the score.



        ## Part 1

        ### Explanation

        We win when the opponent move is "behind" our move by 1 or by 2. In
        principle, the moves Rock, Paper, and Scissors can be seen as a cyclic
        directed graph with R < P < S < R as the relation between each move.
        Arithmetically, if opponent chooses Rock (1), then subtracting that
        from the winning move Paper (2) would result in a 1. This follows along
        the entire chain except when they play Scissors (3) and we play
        rock (1) in which case we get -2 instead.

        As a consequence, the three states (win, tie, lose) are determined
        by if `opponent - shape is -1 or 2`, `opponent is shape`, or
        if `opponent - shape is 1 or -2`.

        ### Pseudocode

        ```
        foreach round
            opponent = ascii value of opponent move offset by 'A'
            shape = ascii value of our move offset by 'X'

            if opponent - shape is -1 or 2 then
                score = shape + 6
            if opponent is shape then
                score = shape + 3
            if opponent - shape is 1 or -2 then
                score = shape + 0
        ```
    """
    def parse(self, filename):
        with open(filename, 'r') as f:
            strategies = [
                line.strip('\n').split()
                for line in f.readlines()
            ]
            return strategies


    def part1(self, filename="day2.txt"):
        strategies = self.parse(filename)
        total_score = 0
        for strategy in strategies:
            # get values for shapes (A = 1, B = 2, C = 3. X = 1, Y = 2, Z = 3)
            opponent = ord(strategy[0]) - ord('A') + 1
            shape = ord(strategy[1]) - ord('X') + 1

            # rock wins paper wins scissors wins rock
            if opponent - shape == -1 or opponent - shape == 2:
                total_score += shape + 6  # win
            if opponent == shape:
                total_score += shape + 3  # tie
            if opponent - shape == 1 or opponent - shape == -2:
                total_score += shape + 0  # lose
        return total_score


    def part2(self, filename="day2.txt"):
        pass


day2 = Solution()
solutions = [day2.part1(), day2.part2()]
print(solutions)
