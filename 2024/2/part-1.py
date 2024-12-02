# Variables
safe_reports = 0

# Open the puzzle file and read per report
with open("puzzle-input.txt") as file:
    for report in file:
        prev_number = None
        incr_or_decr = set()
        unsafe_detected = False
        for i, level in enumerate(report.strip().split()):
            if prev_number and not unsafe_detected:
                distance = int(level) - prev_number
                if (4 > distance > 0) or (-4 < distance < 0):
                    incr_or_decr.add("incr" if 0 < distance else "decr")
                else:
                    unsafe_detected = True
            prev_number = int(level)
        if not unsafe_detected and len(incr_or_decr) == 1:
            safe_reports += 1
    file.close()
print(f"Outcome 1: {safe_reports}")