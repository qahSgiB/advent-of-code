from typing import List, Optional, Tuple, Callable

from aoc import *



def parse_line(line_: str) -> List[int]:
    return [int(line_[i:i+2]) for i in range(0, len(line_), 3)]

def parse_board(board_: str) -> List[List[int]]:
    return list(map(parse_line, board_.split('\n')))

def parse_inp(inp: str) -> Tuple[List[int], List[List[List[int]]]]:
    (ns_, boards_) = first(inp.split('\n\n'))
    ns = list(map(int, ns_.split(',')))
    boards = list(map(parse_board, boards_))

    return (ns, boards)


def check_board(board: List[List[int]]) -> bool:
    for line in board:
        if all(map(lambda x: x == -1, line)):
            return True

    for i in range(len(board[0])):
        if all(map(lambda x: x == -1, map(lambda x: x[i], board))):
            return True

    return False

def update_board(n: int, board: List[List[int]]) -> bool:
    for line in board:
        for (i, x) in enumerate(line):
            if x == n:
                line[i] = -1

    return check_board(board)

def board_score(board: List[List[int]]) -> int:
    return sum(sum(filter(lambda x: x != -1, line)) for line in board)

def play(ns: List[int], boards: List[List[List[int]]], end: Callable[[List[bool]], bool]) -> int:
    w = -1
    winned = [False for _ in range(len(boards))]

    nsi = iter(ns)
    while not end(winned):
        n = next(nsi)
        for (j, board) in enumerate(boards):
            if not winned[j]:
                if update_board(n, board):
                    w = j
                    winned[j] = True

    return n * board_score(boards[w])


def a(inp_file_path: str) -> int:
    (ns, boards) = parse_inp(load_file(inp_file_path))
    return play(ns, boards, any)

def b(inp_file_path: str) -> int:
    (ns, boards) = parse_inp(load_file(inp_file_path))
    return play(ns, boards, all)



if __name__ == '__main__':
    print(a('inp.txt'))
    print(b('inp.txt'))