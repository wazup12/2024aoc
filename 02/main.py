FILENAME = "input.txt"
IO_ERROR = -1

SAFE = 1
UNSAFE = 0
SAMPLE_DATA = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9"""

def get_file_contents(filename=FILENAME):
    with open(filename) as f:
        conts = f.read()
        return conts

def get_reports_from_file_conts(conts):
    import re
    reports = list()
    reports_strings = conts.split("\n")
    for string in reports_strings:
        if not string: continue
        report = [int(x) for x in re.split("\\s+", string)]
        reports.append(report)
    return reports

def get_num_safe_rows(conts, dampener=False):
    safe_count = 0
    reports = get_reports_from_file_conts(conts)
    safe_count = sum([process_report(report, dampener) for report in reports])
    return safe_count

def difference_invalid(difference, sum_report):
    return difference == 0 or difference < -3 or difference > 3 or sum_report * difference < 0

# difference: [-3,-1] U [1,3] is valid
def process_report(report, dampener):
    # skip levels: 0 if unskipped, 1 to skip, 2 if prior skipped
    UNSKIPPED = 0
    SKIP_NOW = 1
    SKIPPED = 2
    sum_report = 0
    skip_level = UNSKIPPED

    for i in range(len(report) - 1):
        if dampener and skip_level == SKIP_NOW:
            skip_level = SKIPPED
            continue

        difference = report[i] - report[i+1]
        # print(f"comparing {report[i]} and {report[i+1]}, {skip_level}")
        # input()

        if difference_invalid(difference, sum_report):
            if not dampener or skip_level == SKIPPED:
                return UNSAFE
            # if reached end, inherently safe
            if i+2 >= len(report):
                return SAFE

            skip_level = SKIP_NOW

            difference_left_invalid = difference_invalid(report[i] - report[i+2], sum_report)
            difference_right_invalid = difference_invalid(report[i+1] - report[i+2], sum_report)
            # print(f"comparing {report[i]} and {report[i+1]}, {skip_level}")
            # input()
            if difference_left_invalid and difference_right_invalid:
                return UNSAFE
            skip_level = SKIP_NOW

        sum_report += difference

    return SAFE

if __name__ == "__main__":
    conts = get_file_contents()
    if not conts: exit(IO_ERROR)

    num_safe_rows = get_num_safe_rows(conts, dampener=True)
    #num_safe_rows = get_num_safe_rows(SAMPLE_DATA, dampener=True)
    print(num_safe_rows)
