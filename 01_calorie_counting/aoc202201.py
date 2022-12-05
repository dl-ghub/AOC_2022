import pathlib
import sys


def parse(puzzle_input):
    """Parse input into a list of lists of integers grouped by blank lines."""
    data = [sum([int(x) for x in i.split("\n")])for i in puzzle_input.split("\n\n")]
    return data


def part1(data):
    """Return the largest subsum of the data"""
    return max(data)


def part2(data):
    """Return the sum of the three largest subsums of the data"""
    data.sort()
    return data[-1] + data[-2] + data[-3]


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