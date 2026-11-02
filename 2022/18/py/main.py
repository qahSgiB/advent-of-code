# pylint: disable=unused-import, unused-wildcard-import

from typing import List, Tuple, Optional, Callable, Dict, Deque, Any, Set

from collections import deque, defaultdict, Counter

import operator as op
import functools as ft
import itertools as it

import math as ma

import dataclasses as da

from aoc import * # pylint: disable=wildcard-import

from itree import ITree



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



DIRS6 = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]



AOCEl = Tuple[int, int, int]
AOCInput = Set[AOCEl]
AOCResult = int



def parse_el(s: str) -> AOCEl:
    x, y, z = cut3u(s, ',', ',')
    return (int(x), int(y), int(z))

def parse(s: str) -> AOCInput:
    return set(map(parse_el, remove_last_empty(splitn(s))))

def a(inp: AOCInput) -> AOCResult:
    sa = 0

    for (x, y, z) in inp:
        for (dx, dy, dz) in DIRS6:
            if not (x + dx, y + dy, z + dz) in inp:
                sa += 1

    return sa

def b(inp: AOCInput) -> AOCResult:
    p0 = next(iter(inp))

    min_x = p0[0]
    max_x = p0[0]
    min_y = p0[1]
    max_y = p0[1]
    min_z = p0[2]
    max_z = p0[2]

    for (x, y, z) in inp:
        min_x = min(min_x, x)
        max_x = max(max_x, x)
        min_y = min(min_y, y)
        max_y = max(max_y, y)
        min_z = min(min_z, z)
        max_z = max(max_z, z)

    min_x -= 1
    min_y -= 1
    min_z -= 1
    max_x += 1
    max_y += 1
    max_z += 1

    sp = [[[(1 if (x, y, z) in inp else 0) for x in range(min_x, max_x + 1)] for y in range(min_y, max_y + 1)] for z in range(min_z, max_z + 1)]

    print(len(sp) * len(sp[0]) * len(sp[0][0]))

    d: Deque[Tuple[int, int, int]] = deque()
    d.append((0, 0, 0))

    sp[0][0][0] = -1

    while len(d) > 0:
        (x, y, z) = d.popleft()
        print(x, y, z)

        for (dx, dy, dz) in DIRS6:
            nx = x + dx
            ny = y + dy
            nz = z + dz

            if in_range(min_x, max_x, nx) and in_range(min_y, max_y, ny) and in_range(min_z, max_z, nz) and sp[nz - min_z][ny - min_y][nx - min_x] == 0:
                sp[nz - min_z][ny - min_y][nx - min_x] = -1
                d.append((nx, ny, nz))

    # print('done')

    sa = 0

    for (x, y, z) in inp:
        for (dx, dy, dz) in DIRS6:
            if sp[z + dz - min_z][y + dy - min_y][x + dx - min_x] == -1:
                sa += 1

    return sa



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