# pylint: disable=unused-import, unused-wildcard-import

from typing import List, Tuple, Optional, Callable, Dict, Deque

from collections import deque, defaultdict, Counter

import operator as op
import functools as ft
import itertools as it

import math as ma

from aoc import * # pylint: disable=wildcard-import



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



AOCEl = int
AOCInput = Tuple[List[List[str]], List[Tuple[int, int, int]]]
AOCResult = str



def parse_b_el(s: str) -> Tuple[int, int, int]:
    x = split(s, ' ')
    return (int(x[1]), int(x[3]) - 1, int(x[5]) - 1)

def parse_b(s: str) -> List[Tuple[int, int, int]]:
    return lm(parse_b_el, remove_last_empty(splitn(s)))

def parse_a(s: str) -> List[List[str]]:
    lines = splitn(s)
    c = (len(lines[-1]) + 1) // 4
    stacks: List[List[str]] = [[] for _ in range(c)]

    for line_index in range(len(lines) - 1):
        line = lines[line_index]
        for stack_index in range(c):
            crate = line[stack_index * 4 + 1]
            if crate != ' ':
                stacks[stack_index].append(crate)

    for stack in stacks:
        stack.reverse()

    return stacks

def parse(s: str) -> AOCInput:
    x, y = cut2u(s, '\n\n')
    return (parse_a(x), parse_b(y))

def a(inp: AOCInput) -> AOCResult:
    moves = inp[1]
    stacks = [stack.copy() for stack in inp[0]]

    for (c, f, t) in moves:
        for _ in range(c):
            stacks[t].append(stacks[f].pop())

    return ''.join(map(nth(-1), stacks))

def b(inp: AOCInput) -> AOCResult:
    moves = inp[1]
    stacks = [stack.copy() for stack in inp[0]]

    for (c, f, t) in moves:
        # print(c, f, t)
        # print(stacks)
        stacks[t].extend(stacks[f][crate_index] for crate_index in range(-c, 0))
        for _ in range(c):
            stacks[f].pop()

    return ''.join(map(nth(-1), stacks))



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