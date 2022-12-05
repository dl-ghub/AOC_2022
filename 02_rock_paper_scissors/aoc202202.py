import pathlib
import sys

# Rock = A / X = 1 Point
# Paper = B / Y = 2 Points
# Scissors = C / Z = 3 Points

# Loss = 0 Points
# Draw = 3 Points
# Win = 6 Points

points_dict = {
    "X": 1,
    "Y": 2,
    "Z": 3,
}

mapping_dict = {
    "A": "i",
    "X": "i",
    "B": "j",
    "Y": "j",    
    "C": "k",
    "Z": "k",
}

def parse(puzzle_input):
    """Parse input into a list of lists of integers grouped by blank lines."""
    data = puzzle_input.splitlines()
    return data


def part1(data):
    """Calculate the amount of points you will have by following the input strategy"""
    total = 0
    for i in data:
        i = i.split()
        opp = mapping_dict[i[0]]
        you = mapping_dict[i[1]]
        
        if opp == you:
            total += 3
        elif opp == "i" and you == "j":
            total += 6
        elif opp == "i" and you == "k":
            total += 0
        elif opp == "j" and you == "i":
            total += 0
        elif opp == "j" and you == "k":
            total += 6
        elif opp == "k" and you == "i":
            total += 6
        elif opp == "k" and you == "j":
            total += 0
        
        total += points_dict[i[1]]

    return total


# X = Lose
# Y = Draw
# Z = Win

def part2(data):
    """Calculate the amount of points you will have by playing to create the given outcome"""
    total = 0
    for i in data:
        i = i.split()
        opp = mapping_dict[i[0]]
        final = i[1]
        if opp == "i" and final == "X":
            total += 0
            total += points_dict["Z"]
        elif opp == "i" and final == "Y":
            total += 3
            total += points_dict["X"]
        elif opp == "i" and final == "Z":
            total += 6
            total += points_dict["Y"]
            
        elif opp == "j" and final == "X":
            total += 0
            total += points_dict["X"]
        elif opp == "j" and final == "Y":
            total += 3
            total += points_dict["Y"]
        elif opp == "j" and final == "Z":
            total += 6
            total += points_dict["Z"]

        elif opp == "k" and final == "X":
            total += 0
            total += points_dict["Y"]
        elif opp == "k" and final == "Y":
            total += 3
            total += points_dict["Z"]
        elif opp == "k" and final == "Z":
            total += 6
            total += points_dict["X"]
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