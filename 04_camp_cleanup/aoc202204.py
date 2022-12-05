import pathlib
import sys


def parse(puzzle_input):
    """Parse input into a list of lists of integers chunked by blank lines."""
    data = [i.split(",") for i in puzzle_input.splitlines()]
    return data


def part1(data):
    """Find the number of input pairs where one range is completely contained in the other"""
    total = 0

    for i in data:
        x1 = int(i[0].split("-")[0])
        x2 = int(i[0].split("-")[1])
        y1 = int(i[1].split("-")[0])
        y2 = int(i[1].split("-")[1])

        if x1 <= y1 and x2 >= y2:
            total += 1
        elif y1 <= x1 and y2 >= x2:
            total += 1

    return total


def part2(data):
    """Find the number of input pairs where one range overlaps with another"""
    total = 0

    for i in data:
        x1 = int(i[0].split("-")[0])
        x2 = int(i[0].split("-")[1])
        y1 = int(i[1].split("-")[0])
        y2 = int(i[1].split("-")[1])

        if x1 <= y1 <= x2:
            total += 1
        elif y1 <= x1 <= y2:
            total += 1

    return total


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