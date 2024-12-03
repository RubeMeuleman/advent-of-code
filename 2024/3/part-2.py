# Imports
import re

# Open file and read input
with open("puzzle-input.txt") as file:
    # Variables
    sum_mul = 0
    operators = []
    ignore_next_mul = False

    # Find all operators out of the input
    result = re.findall(r"(do\(\))|(don't\(\))|(mul\([0-9]*,[0-9]*\))", file.read())

    # Filter out the empty strings in the tupples
    for operator in result:
        operator_filter = lambda: [(operators.append(x) if x != "" else "") for x in operator]
        operator_filter()

    # Loop through each operator to apply the given condition
    for operator in operators:
        if "don't(" in operator:
            # Flag the next mul as ignored
            ignore_next_mul = True
        elif "do(" in operator and ignore_next_mul:
            # Flag the next mul as not ignored
            ignore_next_mul = False
        elif "mul(" in operator and not ignore_next_mul:
            # Don't ignore if the flag is negative
            mul_numbers = re.search(r"mul\(([0-9]*),([0-9]*)\)", operator)
            sum_mul += int(mul_numbers.group(1)) * int(mul_numbers.group(2))
            ignore_next_mul = False

    # Close the file and print the final result
    file.close()
    print(f"Result 2: {sum_mul}")
