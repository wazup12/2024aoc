FILENAME = "input.txt"
IO_ERROR = -1

def get_file_contents(filename=FILENAME):
    with open(filename) as f:
        conts = f.read()
        return conts

def process_text(conts):
    import re

    lines = conts.split("\n")
    left = list()
    right = list()

    for line in lines:
        if not line: continue
        left_entry, right_entry = map(int, re.split("\\s+", line))
        left.append(left_entry)
        right.append(right_entry)

    return left, right

def get_sum_deltas(left, right):
    deltas = [abs(l-r) for l,r in zip(left, right)]
    return sum(deltas)

def get_similarity_score(left, right):
    similarity_score = 0
    left_set = list(set(left))

    for l in left_set:
        l_count_in_right = len([r for r in right if r == l])
        similarity_score += l*l_count_in_right
    
    return similarity_score

if __name__ == "__main__":
    conts = get_file_contents()
    if not conts: exit(IO_ERROR)
    left, right = process_text(conts)
    left.sort()
    right.sort()
    sum_deltas = get_sum_deltas(left, right)
    sim_score = get_similarity_score(left, right)
    print(sim_score)
