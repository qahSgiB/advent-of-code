from typing import List, Tuple



def load_input(input_path: str) -> str:
    with open(input_path, 'r') as input_file: return input_file.read()


def input_to_buses(inp: str) -> List[Tuple[int, int]]:
    buses_strs = inp.split('\n')[1].split(',')

    buses: List[Tuple[int, int]] = []

    bus_off = 0
    for bus_str in buses_strs:
        if bus_str != 'x': buses.append((int(bus_str), bus_off))
        bus_off += 1

    return buses

def bus_to_mbus(bus: Tuple[int, int]) -> Tuple[int, int]:
    id_, off = bus
    
    return (id_, (-off)%id_)

def buses_to_mbuses(buses: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
    return list(map(bus_to_mbus, buses))


def modder(div: int, mod: int, step: int) -> int:
    x = 0
    while x%div != mod: x += step

    return x//step


def solve_b(inp: str) -> int:
    mbuses = buses_to_mbuses(input_to_buses(inp))

    c = 1
    a = 0

    for bus_id, bus_off in mbuses:
        x = modder(bus_id, (bus_off - a) % bus_id, c)
        a = c*x + a
        c *= bus_id

    return a

def solve_b1(inp: str) -> int:
    mbuses = input_to_buses(inp)

    t = 0

    while True:
        # if t % 10000 == 0: print(t)
        sol = True

        for bus_id, bus_off in mbuses:
            if (t + bus_off) % bus_id != 0: sol = False

        if sol: break

        t += 1

    return t



input_ = load_input('input.txt')
test_input = load_input('test_input.txt')