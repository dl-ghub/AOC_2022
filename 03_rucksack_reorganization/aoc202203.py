import pathlib
import sys


def parse(puzzle_input):
    """Parse input into a list of lists of integers chunked by blank lines."""
    data = puzzle_input.splitlines()
    return data


def part1(data):
    """Calculate the sum of the values of the shared character in both strings"""
    total = 0

    for s in data:
        x1  = s[:len(s)//2]
        x2 = s[len(s)//2:]

        for char in x1:
            if char in x2:
                if char.isupper():
                    total += ord(char) - 38
                else:
                    total += ord(char) - 96
                break


    return total


def part2(data):
    """Calculate the sum of the values of the shared character in three strings"""
    total = 0

    for i in range(0, len(data), 3):
        chunk = data[i:i+3]

        # find common character in chunk
        for char in chunk[0]:
            if char in chunk[1] and char in chunk[2]:
                if char.isupper():
                    total += ord(char) - 38
                else:
                    total += ord(char) - 96
                break


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