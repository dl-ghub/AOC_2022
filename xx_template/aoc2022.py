import pathlib
import sys


def parse(puzzle_input):
    """Parse input into array of input strings"""
    data = puzzle_input.splitlines()
    return data

def part1(data):

    return -1

def part2(data):

    return -1

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