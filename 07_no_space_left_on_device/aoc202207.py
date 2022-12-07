import pathlib
import sys


def parse(puzzle_input):
    """Parse input into list of strings for each line"""
    data = puzzle_input.splitlines()
    return data

class Node(object):
    def __init__(self, name, isFile, size):
        self.name = name # name
        self.isFile = isFile # is file
        self.size = size # size of directory
        self.children = [] # list of nodes
        self.parent = None

    def add_child(self, child):
        self.child = child
        child.parent = self
        self.children.append(child)
    
    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

    def get_size(self):
        if self.isFile:
            return self.size
        else:
            size = 0
            for each in self.children:
                size += each.get_size()
            return size

    def print_tree(self):
        print("  "*self.get_level() + "|--", end="")
        if self.isFile:
            print(self.name, f"(file, size={self.size})")
        else:
            print(self.name, f"(dir, size={self.get_size()})")
        if self.children:
            for each in self.children:
                each.print_tree()

def part_one_traverse(node):
    """Iteravely traverse tree and sum directories that have a size of at most 100,000"""
    ans = 0
    stack = [node]
    while stack:
        current = stack.pop()
        if not current.isFile and current.get_size() <= 100000:
            ans += current.get_size()
        for each in current.children:
            stack.append(each)
    return ans

def part1(data):
    """Read terminal output (data) and return the sum of size of directories that have a size of at most 100,000"""

    # Represent directories as a tree
    root = Node("/", False, 0)
    current_dir = root

    for line in data:
        if line == "$ ls":
            pass

        elif line[0] == "d":
            # Found directory
            current_dir.add_child(Node(line.split()[1], False, 0))

        elif line[0].isdigit():
            # Found file
            current_dir.add_child(Node(line.split()[1], True, int(line.split()[0])))

        elif line[:7] == "$ cd ..":
            # Change directory (up)
            current_dir = current_dir.parent
            continue

        elif line[:4] == "$ cd":
            # Change directory (down)
            for each in current_dir.children:
                if each.name == line[5:]:
                    current_dir = each
                    break
            continue

    return part_one_traverse(root)

def part_two_traverse(node, current_size, target_size):
    """Iteravely traverse tree and find the smallest directory that can be deleted to free up enough space for the 70,000,000 byte update"""
    ans = target_size
    stack = [node]

    while stack:
        current = stack.pop()
        if not current.isFile and (current_size - current.get_size()) <= target_size:
            if current.get_size() < ans:
                ans = current.get_size()
        for each in current.children:
            stack.append(each)            
    return ans


def part2(data):
    """Find the smallest directory you could delete to free up enough space for the 70,000,000 byte update"""
    # Represent directories as a tree
    root = Node("/", False, 0)
    current_dir = root

    for line in data:
        if line == "$ ls":
            pass

        elif line[0] == "d":
            # Found directory
            current_dir.add_child(Node(line.split()[1], False, 0))

        elif line[0].isdigit():
            # Found file
            current_dir.add_child(Node(line.split()[1], True, int(line.split()[0])))

        elif line[:7] == "$ cd ..":
            # Change directory (up)
            current_dir = current_dir.parent
            continue

        elif line[:4] == "$ cd":
            # Change directory (down)
            for each in current_dir.children:
                if each.name == line[5:]:
                    current_dir = each
                    break
            continue
    
    # Find current size of root
    current_size = int(root.get_size())

    # Find smallest directory that can be deleted
    return part_two_traverse(root, current_size, target_size=40000000)
       

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