import pathlib
import sys


def parse(puzzle_input):
    """Parse input"""
    data = puzzle_input
    return data


def part1(data):
    """Find the index of the first set of four unique characters in the input string"""
    for i in range(len(data) - 3):
        if len(set(data[i:i + 4])) == 4:
            return i + 4
    return -1
    


def part2(data):
    """Find the index of the first set of fourteen unique characters in the input string"""
    for i in range(len(data) - 13):
        if len(set(data[i:i + 14])) == 14:
            return i + 14
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