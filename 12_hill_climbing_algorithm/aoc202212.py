import pathlib
import sys
from pandas import *

def parse(puzzle_input):
    """Parse input into array of input strings"""
    data = puzzle_input.splitlines()
    return data

def print_grid(grid):
    print("Grid: ")
    print (DataFrame(grid), "\n")

def find_shortest_path_length(data, start, end):
    # Create a blank grid of the map to be filled in with the distances from each point to the start
    grid = [[-1 for _ in range(len(data[0]))] for _ in range(len(data))]
    
    # Create a list of points to be checked
    points_to_check = [start]

    # Iterate through points_to_check, adding the distance to grid, and then adding the adjacent points to the list of points to check
    while len(points_to_check) > 0:
        # Get the next point to check
        point = points_to_check.pop(0)
        x, y = point[0], point[1]
        distance = grid[y][x] # Distance of current grid point from start point
        current_altitude = data[y][x] # Altitude of current grid point

        # If the point is the start, set the distance to 0, and current altitude to "a"
        if point == start:
            distance = 0
            current_altitude = "a"
            grid[y][x] = distance

        # If the point is the end, return the distance
        if point == end:
            return distance

        # Add the points around the point to the list of points to check, and set the distance of those points in the grid
        adj = [(x, y-1), (x, y+1), (x-1, y), (x+1, y)] # above, below, left, right
        for a in adj:
            # Check if the point is in the grid
            if a[0] >= 0 and a[0] < len(grid[0]) and a[1] >= 0 and a[1] < len(grid):
                target_altitude = data[a[1]][a[0]]

                # If it's comparing to end then set target_altitude to "z"
                if a == end:
                    target_altitude = "z"

                # Check if the altitude of the point is more than 2 higher than the current altitude
                if ord(target_altitude) - ord(current_altitude) >= 2:
                    continue

                # Check if the point has already been checked
                if grid[a[1]][a[0]] != -1:
                    continue

                # Add the point to the list of points to check
                points_to_check.append(a)

                # Set the distance of the point in the grid
                grid[a[1]][a[0]] = distance + 1 

def part1(data):
    """Find the fewest number of steps to go from S to E, given the input map of altitudes (represented by a - z). Use A*"""
    
    # Find the start and end points
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] == "S":
                start = (j, i)
            elif data[i][j] == "E":
                end = (j, i)

    return find_shortest_path_length(data, start, end)
   
def part2(data):
    """Same as part 1, except you can start from any point with altitude a (including the point S). Return the fewest number of steps to go from any point with altitude a to E"""

    starting_points = []

    # Find the end point
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] == "E":
                end = (j, i)

    # Find all the starting points
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] == "a" or data[i][j] == "S":
                starting_points.append((j, i))

    path_lengths = [find_shortest_path_length(data, start, end) for start in starting_points]

    # Remove all None from path_lengths
    path_lengths = [x for x in path_lengths if x is not None]

    return min(path_lengths)

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