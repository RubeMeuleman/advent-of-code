# Variables
collection = [[], []]
outcome_1 = 0
outcome_2 = 0

# Open file
with open('lists.txt') as file:
    # Read each line and put in collection list
    for line in file:
        line = line.strip()
        collection[0].append(line.split()[0])
        collection[1].append(line.split()[1])
    file.close()

# Sort each list
for item in collection:
    item.sort()

# Calculate the outcome for both lists
for i, item in enumerate(zip(collection[0], collection[1])):
    outcome_2 += int(item[0]) * collection[1].count(item[0])
    if int(item[0]) > int(item[1]):
        outcome_1 += int(item[0]) - int(item[1])
    else:
        outcome_1 += int(item[1]) - int(item[0])

# Print the result
print(f"Outcome 1: {outcome_1}")
print(f"Outcome 2: {outcome_2}")