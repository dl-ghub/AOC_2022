import pathlib
import sys
import math


def parse(puzzle_input):
    """Parse input into array of input strings"""
    data = puzzle_input.split("\n\n")
    # print(data)
    return data

class Monkey(object):
    def __init__(self, monkey_number, items, operation, test, to_true_monkey, to_false_monkey, part1=True):
        self.monkey_number = monkey_number # Int (monkey number)
        self.items = items # Array of ints (item worry numbers)
        self.operation = operation # Array of 2 strings (operation and number (or operation, if "old")))
        self.test_divisor = test # Int (number to divide by)
        self.to_true_monkey = to_true_monkey # Int (monkey number to throw to if test is true)
        self.to_false_monkey = to_false_monkey # Int (monkey number to throw to if test is false)
        self.part1 = part1 # Bool (part 1 or part 2)

        self.items_tested = 0

    def add_item(self, item):
        self.items.append(item)

    def test_items(self, divisor):
        """Returns an array of ints, indicating other monkeys (monkey number) to throw to"""
        new_item_values = []
        results = []

        for item in self.items:
            # Inspection
            operator = self.operation[0]
            value = self.operation[1]
            if value == "old":
                value = item
            if operator == "+":
                item += int(value)
            elif operator == "-":
                item -= int(value)
            elif operator == "*":
                item *= int(value)
            elif operator == "/":
                item /= int(value)

            # Part 1 divide by 3    
            if self.part1:
                # Boredom (divide by 3 and round down to nearest int)
                item = int(item / 3)

            # Test
            if item % self.test_divisor == 0:
                results.append(self.to_true_monkey)
            else:
                results.append(self.to_false_monkey)

            # Divide by the product of all monkeys' test divisors, to keep numbers small (Necessary in Part 2)
            new_item_values.append(item % divisor)
            self.items_tested += 1
        
        self.items = new_item_values

        return results

    def print_monkey_info(self):
        print(f"""
        Monkey {self.monkey_number}:
            Items: {self.items}
            Operation: new = old {self.operation[0]} {self.operation[1]}
            Test: divisible by {self.test}
                If true: throw to monkey {self.to_true_monkey}
                If false: throw to monkey {self.to_false_monkey}
        """)

def data_to_monkeys(data, part1=True):
    """Converts list of strings into monkey objects. Returns array of monkey objects."""
    monkeys = []
    for i in range(len(data)):
        monkey = data[i].split("\n")
        monkey_number = i
        monkey_items = [int(x.replace(",", "")) for x in monkey[1].split(" ")[4:]]
        monkey_operation = monkey[2].split(" ")[-2:]
        monkey_test = int(monkey[3].split(" ")[-1])
        to_true_monkey = monkey[4].split(" ")[-1]
        to_false_monkey = monkey[5].split(" ")[-1]

        monkeys.append(Monkey(monkey_number, monkey_items, monkey_operation, monkey_test, to_true_monkey, to_false_monkey, part1=part1))

    return monkeys

def part1(data):
    """Find the two monkeys that inspect the most items. Return the product of their inspected items tally."""
    # Convert data to monkey objects
    monkeys = data_to_monkeys(data)

    # Calculate divisor by multiplying all monkeys' test divisors (monkey_test)
    divisor = math.prod([monkey.test_divisor for monkey in monkeys])

    # Play through 20 rounds of monkey throwing
    for _ in range(20):
        for monkey in monkeys:
            # Test all items
            results = monkey.test_items(divisor) # array of ints (monkey numbers)
            # Get resulting items values after testing
            items = monkey.items
            # Throw items to other monkeys
            for j in range(len(items)):
                monkeys[int(results[j])].add_item(items[j])
            # Clear items
            monkey.items = []

    # Sort list of monkeys by items_tested
    monkeys.sort(key=lambda monkey: monkey.items_tested, reverse=True)

    # Calculate monkey business (product of items_tested of top two monkeys)
    monkey_business = monkeys[0].items_tested * monkeys[1].items_tested

    return monkey_business


def part2(data):
    """Same as part 1, but no more division by 3 and there are 10000 rounds."""
    # Convert data to monkey objects
    monkeys = data_to_monkeys(data, part1=False)

    # Calculate divisor by multiplying all monkeys' test divisors (monkey_test)
    divisor = math.prod([monkey.test_divisor for monkey in monkeys])

    # Play through 10,000 rounds of monkey throwing
    for _ in range(10000):
        for monkey in monkeys:
            results = monkey.test_items(divisor)
            items = monkey.items
            for j in range(len(items)):
                monkeys[int(results[j])].add_item(items[j])
            monkey.items = []

    # Sort
    monkeys.sort(key=lambda monkey: monkey.items_tested, reverse=True)

    return monkeys[0].items_tested * monkeys[1].items_tested
       

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