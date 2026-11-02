from typing import Iterator, List, Tuple, Optional, Callable, Dict, Deque

from collections import deque, defaultdict, Counter

import operator as op
import functools as ft
import itertools as it

import math as ma

from aoc import *



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
##  APLHABET
##  APLHABETU
##  DIGITS
##
##
##
##  nth (op.itemgetter)
##  ft.reduce



AOCEl = List[int]
AOCInput = List[AOCEl]
AOCResult = int



DIRS = [(0, 1), (0, -1), (1, 0), (-1, 0)]



def parse_el(s: str) -> AOCEl:
    return lm(int, s)

def parse(s: str) -> AOCInput:
    return lm(parse_el, remove_last_empty(split(s, '\n')))


def iter_neigh(x: int, y: int, w: int, h: int, dirs: List[Tuple[int, int]]) -> Iterator[Tuple[int, int]]:
    for (dx, dy) in dirs:
        nx = x + dx
        ny = y + dy

        if in_range(0, w - 1, nx) and in_range(0, h - 1, ny):
            yield (nx, ny)

def get_low_points(inp: AOCInput) -> Iterator[Tuple[int, int]]:
    w = len(inp[0])
    h = len(inp)

    for x in range(w):
        for y in range(h):
            if all(inp[y][x] < inp[ny][nx] for (nx, ny) in iter_neigh(x, y, w, h, DIRS)):
                yield (x, y)

def a(inp: AOCInput) -> AOCResult:
    with open('out_samo.txt', 'w') as f:
        for (x, y) in get_low_points(inp):
            f.write(f'{x},{y}\n')

    return sum(inp[y][x] + 1 for (x, y) in get_low_points(inp))


def b_map_dfs(x: int, y: int, m: List[List[int]], b_map: List[List[bool]]) -> int:
    w = len(m[0])
    h = len(m)

    b_map[y][x] = True

    return 1 + sum(b_map_dfs(nx, ny, m, b_map) for (nx, ny) in iter_neigh(x, y, w, h, DIRS) if m[ny][nx] != 9 and not b_map[ny][nx])

def b(inp: AOCInput) -> AOCResult:
    w = len(inp[0])
    h = len(inp)
    
    b_map = [[False for _ in range(w)] for _ in range(h)]
    [a, b, c] = sorted(b_map_dfs(x, y, inp, b_map) for (x, y) in get_low_points(inp))[-3:]
    return a * b * c



if __name__ == '__main__':
    inp = parse(load_file('inp.txt'))
    print(a(inp))
    # print(b(inp))