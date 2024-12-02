# Variables
safe_reports = 0


# List the distances per report
def check_distances(listed_report):
    prev_number = None
    distances = []
    for level in listed_report:
        if prev_number is not None:
            distance = int(level) - prev_number
            distances.append({
                "distance": distance,
                "valid": 1 <= abs(distance) <= 3
            })
        prev_number = int(level)
    return distances


# Check if the given report is safe
def is_report_safe(report):
    distances = check_distances(report)
    is_increasing = all(d["distance"] > 0 for d in distances)
    is_decreasing = all(d["distance"] < 0 for d in distances)
    all_valid = all(d["valid"] for d in distances)

    return (is_increasing or is_decreasing) and all_valid


# Check per item removed from report if report is safe
def try_with_dampener(report):
    for i in range(len(report)):
        modified_report = report[:i] + report[i+1:]
        if is_report_safe(modified_report):
            return True
    return False


# Open the puzzle file and read per report
with open("puzzle-input.txt") as file:
    for report in file:
        listed_report = report.strip().split()
        if is_report_safe(listed_report):
            safe_reports += 1
        elif try_with_dampener(listed_report):
            safe_reports += 1

print(f"Total safe reports: {safe_reports}")
