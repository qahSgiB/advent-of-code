from typing import Tuple, Optional



SUBJECT = 7
MODDER = 20201227



def load_input(input_path: str) -> str:
    with open(input_path, 'r') as input_file: return input_file.read()


def str_to_keys(str_: str) -> Tuple[int, int]:
    newline_index = str_.index('\n')
    pkey_a, pkey_b = int(str_[:newline_index]), int(str_[newline_index+1:])

    return pkey_a, pkey_b


def solve_a(str_: str) -> int:
    pkey_a, pkey_b = str_to_keys(str_)

    value = SUBJECT
    loop_count_a: Optional[int] = None
    loop_count_b: Optional[int] = None
    
    loop_count = 1
    while loop_count_a is None or loop_count_b is None:
        if value == pkey_a: loop_count_a = loop_count
        if value == pkey_b: loop_count_b = loop_count

        value *= SUBJECT
        value %= MODDER
        loop_count += 1

    value = pkey_a
    for _ in range(loop_count_b-1):
        value *= pkey_a
        value %= MODDER

    return value



input_ = load_input('input.txt')
test_input = load_input('test_input.txt')