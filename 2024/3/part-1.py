# Imports
import re

# Open file and read input
with open("puzzle-input.txt") as file:
    sum_mul = 0
    result = re.findall(r"mul\(([0-9]*),([0-9]*)\)", file.read())
    for mul in result:
        sum_mul += int(mul[0])*int(mul[1])
    print(f"Result 1: {sum_mul}")
