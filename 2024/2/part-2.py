# Variables
safe_reports = 0


# Check the validation of records
def check_valid(record: list) -> list:
    direction = None
    previous_level = None
    valid_levels = []
    for level in record:
        if previous_level:
            # Calculate the difference between the previous level and the current one
            difference = int(level) - previous_level

            # Check if the level is not between 1 and 3, negative or positive
            if not (1 <= difference <= 3 or -3 <= difference <= -1):
                valid_levels.append(False)
            else:
                # Check if the direction is increasing or decreasing
                if direction is not None:
                    current_direction = "increasing" if difference > 0 else "decreasing"
                    if current_direction == direction:
                        valid_levels.append(True)
                    else:
                        valid_levels.append(False)
            direction = "increasing" if difference > 0 else "decreasing"
        previous_level = int(level)
    return valid_levels


# Check the record
def check_record(record: list) -> bool:
    # Check if the direction will change
    if all(check_valid(record)):
        return True
    else:
        for i in range(0, len(record)):
            if all(check_valid(record[:i] + record[i+1:])):
                return True
    return False


# Open file and read all records
with open("puzzle-input.txt", "r") as file:
    for record in file:
        safe_reports += 1 if check_record(record.strip().split()) else 0
    file.close()

print(f"Outcome 2: {safe_reports}")
