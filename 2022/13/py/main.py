# pylint: disable=unused-import, unused-wildcard-import

from typing import List, Tuple, Optional, Callable, Dict, Deque, Any

from collections import deque, defaultdict, Counter

import operator as op
import functools as ft
import itertools as it

import math as ma

import dataclasses as da

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
##
##  ft.reduce
##  ft.cmp_to_ket



LL = List[bool | int]
AOCEl = Tuple[LL, LL]
AOCInput = List[AOCEl]
AOCResult = int



def parse_l(s: str) -> LL:
    l: LL = []

    si = 0
    while si < len(s):
        c = s[si]
        if c == '[':
            l.append(True)
            si += 1
        elif c == ']':
            l.append(False)
            si += 1
        elif c == ',':
            si += 1
        else:
            d = char_to_digit(c)
            si += 1
            while s[si].isdigit():
                d *= 10
                d += char_to_digit(s[si])
                si += 1
            l.append(d)

    return l

def parse_el(s: str) -> AOCEl:
    l, r = cut2u(s, '\n')
    return (parse_l(l), parse_l(r))

def parse(s: str) -> AOCInput:
    s = s[:-1]

    return lm(parse_el, splitnn(s))

def cmp_int(x: int, y: int) -> int:
    if x < y:
        return -1
    if x > y:
        return 1
    return 0

def closing(l: LL, i: int) -> int:
    level = 1
    while level != 0:
        i += 1
        lc = l[i]
        if isinstance(lc, int):
            continue

        if lc:
            level += 1
        else:
            level -= 1

    return i

def cmp(l: LL, r: LL, l_start: int, r_start: int) -> Tuple[int, int, int]:
    il = l_start + 1
    ir = r_start + 1

    while True:
        lc = l[il]
        rc = r[ir]
        l_int = not isinstance(lc, bool)
        r_int = not isinstance(rc, bool)
        c = 0

        l_end = (not l_int) and (not lc)
        r_end = (not r_int) and (not rc)

        if l_end and r_end:
            return (0, il, ir)
        if l_end:
            return (-1, -1, -1)
        if r_end:
            return (1, -1, -1)

        if l_int:
            if r_int:
                c = cmp_int(lc, rc)
                il += 1
                ir += 1
            else:
                c, _, ir = cmp([True, lc, False], r, 0, ir)
                il += 1
                ir += 1
        else:
            if r_int:
                c, il, _ = cmp(l, [True, rc, False], il, 0)
                il += 1
                ir += 1
            else:
                c, il, ir = cmp(l, r, il, ir)
                il += 1
                ir += 1
        if c != 0:
            return (c, -1, -1)

def cmp_start(l: LL, r: LL) -> int:
    return cmp(l, r, 0, 0)[0]

def a(inp: AOCInput) -> AOCResult:
    s = 0
    for index, (l, r) in enumerate(inp):
        if cmp_start(l, r) == -1:
            s += index + 1

    return s

def b(inp: AOCInput) -> AOCResult:
    p2 = [True, 2, False]
    p6 = [True, 6, False]
    ps: List[LL] = [p2, p6]

    for l, r in inp:
        ps.append(l)
        ps.append(r)

    ps.sort(key = ft.cmp_to_key(cmp_start))

    return (ps.index(p2) + 1) * (ps.index(p6) + 1)



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