FILENAME = "input.txt"
IO_ERROR = -1

SAMPLE = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"

def get_file_contents(filename=FILENAME):
    with open(filename) as f:
        conts = f.read()
        return conts

def get_valid_muls(conts):
    import re
    return re.findall(r"mul\(\d{1,3},\d{1,3}\)", conts)

def get_valid_muls_and_others(conts):
    import re
    return re.findall(r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)", conts)

def init_mul():
    def mul_default(a, b):
        return int(a) * int(b)

    def mul_disabled(a,b):
        return 0

    mul = mul_default

    def do():
        nonlocal mul
        mul = mul_default
        return 0

    def dont():
        nonlocal mul
        mul = mul_disabled
        return 0

    return lambda *args, **kwargs: mul(*args, **kwargs), do, dont

def sanitize(x: str):
    return x.replace("'", "")
    
if __name__ == "__main__":
    conts = get_file_contents()
    if not conts: exit(IO_ERROR)
    mul, do, dont = init_mul()

    # valid_muls = get_valid_muls(conts)
    valid_muls = [sanitize(x) for x in get_valid_muls_and_others(conts)]

    mul_sum = sum([eval(x) for x in valid_muls])
    print(mul_sum)
