import pathlib
import sys


def parse(puzzle_input):
    """Parse input into array of input strings"""
    data = puzzle_input.splitlines()
    return data

class Tree(object):
    def __init__(self, value, coord, isEdge):
        self.value = value
        self.coord = coord
        self.isEdge = isEdge

        self.above = None
        self.below = None
        self.left = None
        self.right = None

    def find_neighbours(self, map, map_height, map_width):
        # Find the trees above, below, to the left, and to the right of the current tree (ordered as if looking inwards out)
        self.above = [map[(x, self.coord[1])].value for x in range(self.coord[0])][::-1]
        self.below = [map[(x, self.coord[1])].value for x in range(self.coord[0] + 1, map_height)]
        self.left = [map[(self.coord[0], x)].value for x in range(self.coord[1])][::-1]
        self.right = [map[(self.coord[0], x)].value for x in range(self.coord[1] + 1, map_width)]


    def print_tree_info(self):
        print(f"Tree Coordinates: {self.coord} \nTree Value: {self.value} \nisEdge: {self.isEdge} \n")

    def print_tree_neighbours(self):
        self.print_tree_info()
        print(f"Trees above: {self.above} \nTrees below: {self.below} \nTrees to the left: {self.left} \nTrees to the right: {self.right} \n")


    def find_scenic_score(self):
        return 0

def input_to_map(data):
    """Given 2D array of trees, return dictionary of Tree objects"""
    # Get dimensions of array
    height = len(data)
    width = len(data[0])

    # Create map of trees
    M = {}

    for i in range(len(data)):
        for j in range(len(data[i])):
                # Check if tree is on edge of map
                edge_flag = False
                if i == 0 or j == 0 or i == height - 1 or j == width - 1:
                    edge_flag = True

                M[(i, j)] = Tree(int(data[i][j]), (i, j), edge_flag)

    # Find neighbours of each tree
    for i in range(len(data)):
        for j in range(len(data[i])):
            M[(i, j)].find_neighbours(M, height, width)
            # M[(i, j)].print_tree_neighbours()
    
    # Print Map
    # print([(coord, value.print_tree_info()) for (coord, value) in M.items()])

    return M

def part1(data):
    """Given 2D array of trees, return number of inner trees that is visible from at least one side of the map (given height)"""
    count = 0

    M = input_to_map(data)

    # Ignoring the outside ring, for each tree in map check if it is visible from at least one side. If it is, add to count
    for tree in M.values():
        val = tree.value
        if tree.isEdge:
            count += 1
            continue
        else:
            if val > max(tree.above) or val > max(tree.below) or val > max(tree.left) or val > max(tree.right):
                count += 1

    return count

def part2(data):
    """Calculate scenic score of each tree and return the max"""
    ans = 0

    M = input_to_map(data)

    # Calculate scenic score of each tree and retain maximum as ans
    for tree in M.values():
        val = tree.value

        above_idx = 0
        below_idx = 0
        left_idx = 0
        right_idx = 0

        if tree.isEdge:
            continue
        else:
            for i in range(len(tree.above)):
                above_idx += 1
                if tree.above[i] >= val:
                    break

            for i in range(len(tree.below)):
                below_idx += 1
                if tree.below[i] >= val:
                    break

            for i in range(len(tree.left)):
                left_idx += 1
                if tree.left[i] >= val:
                    break
            
            for i in range(len(tree.right)):
                right_idx += 1
                if tree.right[i] >= val:
                    break

            # multiple all indices together
            score = above_idx * below_idx * left_idx * right_idx

            if score > ans:
                ans = score

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