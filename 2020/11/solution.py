from typing import List, Tuple, Callable



FLOOR, EMPTY, OCC = 0, 1, 2

DIRS = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]



def load_input(input_path: str) -> str:
    with open(input_path, 'r') as input_file: return input_file.read()


def seat_str_to_seat(seat_str: str) -> int:
    seat = -1

    if seat_str == '.': seat = FLOOR
    elif seat_str == 'L': seat = EMPTY
    elif seat_str == '#': seat = OCC

    return seat

def input_row_to_row(inp_row: str) -> List[int]:
    return list(map(seat_str_to_seat, list(inp_row)))

def input_to_layout(inp: str) -> List[List[int]]:
    return list(map(input_row_to_row, inp.split('\n')))


def get_see_occ_count(layout: List[List[int]], x: int, y: int) -> int:
    x_size, y_size = len(layout[0]), len(layout)

    adj_occ_count = 0
    for dir_x, dir_y in DIRS:
        see_seat = FLOOR

        see_x = x + dir_x
        see_y = y + dir_y

        while see_x >= 0 and see_x < x_size and see_y >= 0 and see_y < y_size:
            seat = layout[see_y][see_x]

            if seat == EMPTY or seat == OCC:
                see_seat = seat
                break

            see_x += dir_x
            see_y += dir_y

        if see_seat == OCC: adj_occ_count += 1

    return adj_occ_count

def get_adj_occ_count(layout: List[List[int]], x: int, y: int) -> int:
    x_size, y_size = len(layout[0]), len(layout)

    adj_occ_count = 0
    for off_x, off_y in DIRS:
        adj_x, adj_y = x + off_x, y + off_y

        if adj_x >= 0 and adj_x < x_size and adj_y >= 0 and adj_y < y_size:
            adj_seat = layout[adj_y][adj_x]

            if adj_seat == OCC: adj_occ_count += 1

    return adj_occ_count


def update(layout: List[List[int]], get_occ_count: Callable[[List[List[int]], int, int], int], min_to_empty: int) -> Tuple[List[List[int]], bool]:
    x_size, y_size = len(layout[0]), len(layout)

    new_layout = [[FLOOR for _ in range(x_size)] for _ in range(y_size)]
    change = False

    for y in range(y_size):
        for x in range(x_size):
            seat = layout[y][x]

            adj_occ_count = get_occ_count(layout, x, y)

            new_seat = seat

            if seat == EMPTY and adj_occ_count == 0: new_seat = OCC
            elif seat == OCC and adj_occ_count >= min_to_empty: new_seat = EMPTY

            if seat != new_seat: change = True

            new_layout[y][x] = new_seat

    return new_layout, change


def solve_a(inp: str) -> int:
    layout = input_to_layout(inp)
    change = True

    while change: layout, change = update(layout, get_adj_occ_count, 4)

    occ_count = 0

    for row in layout:
        for seat in row:
            if seat == OCC: occ_count += 1

    return occ_count

def solve_b(inp: str) -> int:
    layout = input_to_layout(inp)
    change = True

    while change: layout, change = update(layout, get_see_occ_count, 5)

    occ_count = 0

    for row in layout:
        for seat in row:
            if seat == OCC: occ_count += 1

    return occ_count



input_ = load_input('input.txt')
test_input = load_input('test_input.txt')