# pyright: reportUnusedImport=false

from typing import List, Tuple, Optional, Callable, Dict, Deque, Mapping, MutableMapping, Set, DefaultDict

from collections import deque, defaultdict, Counter

import operator as op
import functools as ft
import itertools as it

import heapq as hq

from copy import deepcopy

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
##  def get_wh(l: List[List[A]]) -> Tuple[int, int]
##
##  APLHABET
##  APLHABETU
##  DIGITS
##
##
##
##  nth (op.itemgetter)
##  ft.reduce



AOCEl = Tuple[int, int, int]
AOCInput = List[AOCEl]
AOCResult = int



def parse_el(s: str) -> AOCEl:
    a, b, c = cut3u(s, ',', ',')
    return int(a), int(b), int(c)

def parse(s: str) -> AOCInput:
    return lm(parse_el, remove_last_empty(split(s, '\n')))

def a(inp: AOCInput) -> AOCResult:
    dists: List[Tuple[int, int, float]] = []

    for ai in range(1, len(inp)):
        a = inp[ai]

        for bi in range(ai):
            b = inp[bi]

            dx = a[0] - b[0]
            dy = a[1] - b[1]
            dz = a[2] - b[2]
            dists.append((ai, bi, ma.sqrt(dx * dx + dy * dy + dz * dz)))

    dists.sort(key=lambda e: e[2])

    dj = [i for i in range(len(inp))]

    # for (ai, bi, _dist) in dists:
    for i in range(1000):
        (ai, bi, _dist) = dists[i]

        # find ai parent
        nai = ai
        while nai != dj[nai]:
            nai = dj[nai]

        nbi = bi
        while nbi != dj[nbi]:
            nbi = dj[nbi]

        if nai != nbi:
            dj[nai] = nbi

    # rebubble
    for i in range(len(inp)):
        repair: List[int] = []
        ni = i
        while ni != dj[ni]:
            repair.append(ni)
            ni = dj[ni]

        for ri in repair:
            dj[ri] = ni

    c = Counter(dj)

    m = 1
    for (_, cc) in c.most_common(3):
        m *= cc

    return m

def b(inp: AOCInput) -> AOCResult:
    dists: List[Tuple[int, int, float]] = []

    for ai in range(1, len(inp)):
        a = inp[ai]

        for bi in range(ai):
            b = inp[bi]

            dx = a[0] - b[0]
            dy = a[1] - b[1]
            dz = a[2] - b[2]
            dists.append((ai, bi, ma.sqrt(dx * dx + dy * dy + dz * dz)))

    dists.sort(key=lambda e: e[2])

    dj = [(i, 1) for i in range(len(inp))]

    lai = 0
    lbi = 0
    for (ai, bi, _dist) in dists:
        # find ai parent
        nai = ai
        while nai != dj[nai][0]:
            nai = dj[nai][0]

        nbi = bi
        while nbi != dj[nbi][0]:
            nbi = dj[nbi][0]

        if nai != nbi:
            dj[nai] = (nbi, dj[nai][1])
            total = dj[nai][1] + dj[nbi][1]
            dj[nbi] = (nbi, total)

            if total == 1000:
                lai = ai
                lbi = bi
                break

    return inp[lai][0] * inp[lbi][0]



if __name__ == '__main__':
    import sys

    inp_file = 'inp.txt'

    args_len = len(sys.argv)
    if args_len >= 2:
        if sys.argv[1] == '-t':
            inp_file = 'test_inp.txt'
        elif sys.argv[1] == '-i' and args_len >= 3:
            inp_file = sys.argv[2]

    inp = parse(load_file(inp_file))
    print(a(inp))
    print(b(inp))

# time: 21:30 / 24:30