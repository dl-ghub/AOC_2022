import pathlib
import sys


def parse(puzzle_input):
    """Parse input into array of input strings"""
    data = puzzle_input.splitlines()
    return data


def part1(data):
    """Given a list of processes, calculate the sum of the 20th, 60th, 100th, 140th, 180th and 220th signal strength (cycle number * X value) cycles."""
    X = 1
    # In an array, for each cycle, store a tuple (startingX, endingX)
    cycle_values = []

    tempX = 0

    for process in data:
        if process[0] == "n": # nothing happens, cycle number increases by 1
            cycle_values.append((X, X))
        else: # process addition (takes two full cycles)
            cycle_values.append((X, X)) # first addition cycle
            tempX = int(process.split()[1]) # second addition cycle
            cycle_values.append((X, X + tempX))
            X += tempX 

    
    # print(cycle_values)
    # Calculate the sum of the 20th, 60th, 100th, 140th, 180th and 220th signal strength
    return sum([cycle_values[19][0] * 20, cycle_values[59][0] * 60, cycle_values[99][0] * 100, cycle_values[139][0] * 140, cycle_values[179][0] * 180, cycle_values[219][0] * 220])


def part2(data):
    
    all_crt = [] # Array of all crt rows

    # Find all cycles and sprite positions
    X = 1
    # In an array, for each cycle, store a tuple (startingX, endingX)
    cycle_values = []

    tempX = 0

    for process in data:
        if process[0] == "n": # nothing happens, cycle number increases by 1
            cycle_values.append((X, X))
        else: # process addition (takes two full cycles)
            cycle_values.append((X, X)) # first addition cycle
            tempX = int(process.split()[1]) # second addition cycle
            cycle_values.append((X, X + tempX))
            X += tempX 

    # create all 6 crt rows
    index = 0
    for _ in range(6):
        crt_row = ""
        for col in range(40):
            X = cycle_values[index][0]
            sprite = [X-1, X, X+1]
            if col in sprite:
                crt_row += "#"
            else:
                crt_row += "."

            index += 1
        all_crt.append(crt_row)

    for row in all_crt:
        print(row)
       

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