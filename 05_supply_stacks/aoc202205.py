import pathlib
import sys


def parse(puzzle_input):
    """Parse input into """
    data = puzzle_input.splitlines()
    return data


def part1(data):
    """Find out the sequence of blocks at the top of each stack after all moves are completed"""

    # # Extract starting stacks from input
    # stacks = []
    # for line in data:

    stacks = data[0].split()
    print(stacks)

    for line in data[1:]:
        moves = [int(i) for i in line.split() if i.isdigit()]  # [Quantity, From Stack, To Stack]
        for _ in range(moves[0]):

            # move last character from string at index moves[1] to string at index moves[2]
            stacks[(moves[2]-1)] += (stacks[(moves[1]-1)])[-1]

            # remove last character from string at index moves[1]
            stacks[(moves[1]-1)] = (stacks[(moves[1]-1)])[:-1]

    ans = ""

    for stack in stacks:
        ans += stack[-1]

    return ans


def part2(data):
    """Find out the sequence of blocks at the top of each stack after all moves are completed (moves are not completed one by one but all at once)"""
    
    stacks = data[0].split()
    print(stacks)

    for line in data[1:]:
        moves = [int(i) for i in line.split() if i.isdigit()]  # [Quantity, From Stack, To Stack]

        # move copy characters (moves[0]) from string at index moves[1] to string at index moves[2]
        stacks[(moves[2]-1)] += (stacks[(moves[1]-1)])[-moves[0]:]

        # remove characters (moves[0]) from string at index moves[1]
        stacks[(moves[1]-1)] = (stacks[(moves[1]-1)])[:-moves[0]]
        
    ans = ""

    for stack in stacks:
        ans += stack[-1]

    return ans

def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()
        solutions = solve(puzzle_input)
        print("\n".join(str(solution) for solution in solutions))