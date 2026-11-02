# pylint: disable=unused-import, unused-wildcard-import

from typing import List, Tuple, Optional, Callable, Dict, Deque, Union

from collections import deque, defaultdict, Counter

import operator as op
import functools as ft
import itertools as it

import math as ma

from aoc import * # pylint: disable=wildcard-import


from dataclasses import dataclass



##  ===================================================  help  ===================================================
##
##  def remove_newline(l: str) -> str
##  def remove_last_empty(l: List[str], empty: str | None = None) -> List[str]
##
##  def parenlr(s: str, lp: str, rp: str) -> bool
##  def paren(s: str, p: str) -> bool
##  def unparenlr(s: str, lp: str, rp: str) -> str
##  def unparen(s: str, p: str) -> str
##  def unstring(s: str) -> str
##
##  def translate(char: U1, t: Dict[U1, U2]) -> U2
##  def translate_to_str(s: List[P], t: Dict[P, str]) -> str
##  def translate_from_str(s: str, t: Dict[str, V]) -> List[V]
##  def translate_str(s: str, t: Dict[str, str]) -> str
##  def translate_list(s: List[M1], t: Dict[M1, M2]) -> List[M2]
##
##  def first(l: List[T]) -> Tuple[T, List[T]]
##
##  def split(s: str, sep: str | None = None) -> List[str]
##  def split_multi(s: str, seps: List[str]) -> List[str]
##
##  def splitn(s: str) -> List[str]
##  def splitnn(s: str) -> List[str]
##  def splitc(s: str) -> List[str]
##  def splits(s: str) -> List[str]
##  def splitns(s: str) -> List[str]
##
##  def cut_n(s: str, seps: List[str]) -> List[str] | None
##
##  def cut2(s: str, sep1: str) -> Tuple[str, str] | None
##  def cut3(s: str, sep1: str, sep2: str) -> Tuple[str, str, str] | None
##  def cut4(s: str, sep1: str, sep2: str, sep3: str) -> Tuple[str, str, str, str] | None
##  def cut5(s: str, sep1: str, sep2: str, sep3: str, sep4: str) -> Tuple[str, str, str, str, str] | None
##  def cut6(s: str, sep1: str, sep2: str, sep3: str, sep4: str, sep5: str) -> Tuple[str, str, str, str, str, str] | None
##
##  def cut2u(s: str, sep1: str) -> Tuple[str, str]
##  def cut3u(s: str, sep1: str, sep2: str) -> Tuple[str, str, str]
##  def cut4u(s: str, sep1: str, sep2: str, sep3: str) -> Tuple[str, str, str, str]
##  def cut5u(s: str, sep1: str, sep2: str, sep3: str, sep4: str) -> Tuple[str, str, str, str, str]
##  def cut6u(s: str, sep1: str, sep2: str, sep3: str, sep4: str, sep5: str) -> Tuple[str, str, str, str, str, str]
##
##  def cut2_map(s: str, sep: str, map_a: Callable[[str], N1], map_b: Callable[[str], N2]) -> Tuple[N1, N2] | None
##  def cut_n_map(s: str, seps: List[str], maps: List[Callable[[str], Any] | None]) -> List[Any] | None
##
##  def char_to_digit(c: str) -> int
##  def string_to_digits(s: str) -> List[int]
##  def digits_to_int(base: int, digits: List[int]) -> int
##  def string_to_int(base: int, s: str) -> int
##
##  def digit_to_char(digit: int) -> str
##  def digits_to_string(digits: List[int]) -> str
##  def int_to_digits(base: int, n: int) -> List[int]
##  def int_to_string(base: int, n: int) -> str
##
##  def in_range(mi: int, ma: int, x: int) -> bool
##
##  def lm(f: Callable[[S1], S2], i: Iterable[S1]) -> List[S2]
##  def lf(p: Callable[[L1], bool], i: Iterable[L1]) -> List[L1]:
##  def count(p: Callable[[K1], bool], i: Iterable[K1]) -> int
##
##  Point2 = Tuple[int, int]
##  P2 = Point2
##  DIRS4
##  DIRS8
##  def iter_xy(ax: int, ay: int, bx: int, by: int) -> Iterator[Point2]
##  def iter_wh(w: int, h: int) -> Iterator[Point2]
##  def iter_neigh(dirs: List[Tuple[int, int]], x: int, y: int, minx: int | None, miny: int | None, maxx: int | None, maxy: int | None) -> Iterator[Point2]
##  def iter_neigh4(x: int, y: int, minx: int | None, miny: int | None, maxx: int | None, maxy: int | None) -> Iterator[Tuple[int, int]]
##  def iter_neigh8(x: int, y: int, minx: int | None, miny: int | None, maxx: int | None, maxy: int | None) -> Iterator[Tuple[int, int]]
##  def iter_neigh_wh(dirs: List[Tuple[int, int]], x: int, y: int, w: int, h: int) -> Iterator[Point2]
##  def iter_neigh_wh4(x: int, y: int, w: int, h: int) -> Iterator[Point2]
##  def iter_neigh_wh8(x: int, y: int, w: int, h: int) -> Iterator[Point2]
##
##  APLHABET
##  APLHABETU
##  DIGITS
##
##
##
##  nth (op.itemgetter)
##  ft.reduce



@dataclass
class File:
    size: int

@dataclass
class Directory:
    childs: Dict[str, Union[File, 'Directory']]



def load_fs(cmds: List[str]) -> Directory:
    dir_stack = [Directory({})]

    cmd_index = 1
    while cmd_index < len(cmds):
        cmd_args = split(cmds[cmd_index][2:], ' ')
        cmd_name = cmd_args[0]
        cmd_index += 1

        match cmd_name:
            case 'ls':
                while cmd_index < len(cmds) and cmds[cmd_index][0] != '$':
                    line = cmds[cmd_index]
                    if len(line) >= 5 and line.startswith('dir '):
                        name = line[4:]
                        dir_stack[-1].childs[name] = Directory({})
                    else:
                        size, name = cut2u(line, ' ')
                        dir_stack[-1].childs[name] = File(int(size))
                    cmd_index += 1
            case 'cd':
                name = cmd_args[1]
                if name == '..':
                    dir_stack.pop()
                else:
                    next_dir = dir_stack[-1].childs[name]
                    assert(isinstance(next_dir, Directory))
                    dir_stack.append(next_dir)

    return dir_stack[0]


def gen_sizing_table(name: str, d: Directory, sizing_table: Dict[str, int]) -> int:
    size = 0
    for child_name, child in d.childs.items():
        if isinstance(child, File):
            size += child.size
        else:
            size += gen_sizing_table(f'{name}/{child_name}', child, sizing_table)
    
    sizing_table[name] = size
    return size



# AOCEl = str
AOCInput = Directory
AOCResult = int



def parse(s: str) -> AOCInput:
    return load_fs(remove_last_empty(splitn(s)))

def a(fs: AOCInput) -> AOCResult:
    sizing_table: Dict[str, int] = {}
    gen_sizing_table('', fs, sizing_table)

    return sum(filter(lambda size: size <= 100000, sizing_table.values()))

def b(fs: AOCInput) -> AOCResult:
    sizing_table: Dict[str, int] = {}
    total_size = gen_sizing_table('', fs, sizing_table)
    needed_size = 30000000 - (70000000 - total_size)
    
    return min(filter(lambda size: size >= needed_size, sizing_table.values()))



def main() -> None:
    import sys

    inp_file = 'inp.txt'

    args_len = len(sys.argv)
    if args_len >= 2 and sys.argv[1] == '-t':
        inp_file = 'test_inp.txt'
    elif args_len >= 3 and sys.argv[1] == '-i':
        inp_file = sys.argv[2]

    inp = parse(load_file(inp_file))
    print(a(inp))
    print(b(inp))

if __name__ == '__main__':
    main()