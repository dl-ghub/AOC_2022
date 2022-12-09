import pathlib
import sys


def parse(puzzle_input):
    """Parse input into array of input strings"""
    data = puzzle_input.splitlines()
    return data

def move_knot(current_coords, target):
    """Checks if a move is required, then moves the knot towards target (knot). Returns new coordinates of the knot"""
    # If Euclidean distance is greater than 1, then a move is required
    manhattan = abs(target[0] - current_coords[0]) + abs(target[1] - current_coords[1])

    if manhattan <= 1: # Move not Required
        return current_coords
    
    elif manhattan == 2: # Potential Orthogonal Move
        if target[0] == current_coords[0] or target[1] == current_coords[1]: # Orthogonal Move
            if target[0] > current_coords[0]:
                return (current_coords[0] + 1, current_coords[1])
            if target[0] < current_coords[0]:
                return (current_coords[0] - 1, current_coords[1])
            if target[1] > current_coords[1]:
                return (current_coords[0], current_coords[1] + 1)
            if target[1] < current_coords[1]:
                return (current_coords[0], current_coords[1] - 1)
        else: # Immediate Diagonal. Don't Move
            return current_coords

    elif manhattan >= 3: # Diagonal Move
        if target[0] > current_coords[0] and target[1] > current_coords[1]:
            return (current_coords[0] + 1, current_coords[1] + 1)
        if target[0] > current_coords[0] and target[1] < current_coords[1]:
            return (current_coords[0] + 1, current_coords[1] - 1)
        if target[0] < current_coords[0] and target[1] > current_coords[1]:
            return (current_coords[0] - 1, current_coords[1] + 1)
        if target[0] < current_coords[0] and target[1] < current_coords[1]:
            return (current_coords[0] - 1, current_coords[1] - 1)

def part1(data):
    """Given a list of moves, calculate the number of grid positions visited by the tail at least once"""
    head_position, tail_position = (0, 0), (0, 0)

    tail_visited = {tail_position}

    for move in data:
        direction, distance = move.split()[0], int(move.split()[1])

        for _ in range(distance):
            # Move head
            if direction == "U":
                head_position = (head_position[0], head_position[1] + 1)
            if direction == "D":
                head_position = (head_position[0], head_position[1] - 1)
            if direction == "L":
                head_position = (head_position[0] - 1, head_position[1])
            if direction == "R":
                head_position = (head_position[0] + 1, head_position[1])

            # Move tail (if necessary)
            tail_position = move_knot(tail_position, head_position)
            tail_visited.add(tail_position)

    return len(tail_visited)


def part2(data):
    """The rope now has 10 knots (including the head). Calculate the number of positions visited by the final knot in the rope"""
    knots = [(0, 0) for _ in range(10)]
    
    nine_visited = {(0, 0)}

    for move in data:

        direction, distance = move.split()[0], int(move.split()[1])

        for _ in range(distance):
            # Move head
            if direction == "U":
                knots[0] = (knots[0][0], knots[0][1] + 1)
            if direction == "D":
                knots[0] = (knots[0][0], knots[0][1] - 1)
            if direction == "L":
                knots[0] = (knots[0][0] - 1, knots[0][1])
            if direction == "R":
                knots[0] = (knots[0][0] + 1, knots[0][1])

            # Move each knot towards the previous knot (if necessary)
            for i in range(1, 10):
                knots[i] = move_knot(knots[i], knots[i-1])
                if i == 9:
                    nine_visited.add(knots[i])


    return len(nine_visited)
       

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