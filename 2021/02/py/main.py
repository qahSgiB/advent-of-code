from typing import Tuple, List
from aoc import split_two_map, load_file_lines



def load_instrs(inp_file_path: str) -> List[Tuple[str, int]]:
    return list(map(lambda line: split_two_map(line, ' ', str, int), load_file_lines(inp_file_path)))

def a(inp_file_path: str) -> int:
    x = 0
    y = 0
    for (dir_, size) in load_instrs(inp_file_path):
        match dir_:
            case "forward":
                x += size
            case "up":
                y -= size
            case "down":
                y += size

    return x * y

def b(inp_file_path: str) -> int:
    x = 0
    y = 0
    aim = 0
    for (dir_, size) in load_instrs(inp_file_path):
        match dir_:
            case "forward":
                x += size
                y += aim * size
            case "up":
                aim -= size
            case "down":
                aim += size

    print(x, y, aim)

    return x * y



if __name__ == '__main__':
    print(a('inp.txt'))
    print(b('inp.txt'))