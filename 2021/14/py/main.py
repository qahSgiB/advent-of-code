from typing import List, Tuple, Optional, Callable, Dict, Deque, Mapping, MutableMapping, Set

from collections import deque, defaultdict, Counter

import operator as op
import functools as ft
import itertools as it

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



AOCInput = Tuple[str, List[Tuple[str, str]]]
AOCResult = int



def parse_rule(s: str) -> Tuple[str, str]:
    return cut2u(s, ' -> ')

def parse(s: str) -> AOCInput:
    (a, b) = cut2u(s, '\n\n')
    return (a, lm(parse_rule, remove_last_empty(split(b, '\n'))))


def create_pair_map(ps: List[Tuple[str, str]]) -> Dict[str, str]:
    return { f: t for (f, t) in ps }

def step(t: str, pm: Mapping[str, str]) -> str:
    nt = ''
    for i in range(len(t) - 1):
        l = t[i]
        p = l + t[i + 1]

        nt += l
        if p in pm:
            nt += pm[p]
    nt += t[-1]

    return nt


def a(inp: AOCInput) -> AOCResult:
    t = inp[0]
    pm = create_pair_map(inp[1])

    for _ in range(10):
        t = step(t, pm)

    c = Counter(t)
    v = c.values()

    return max(v) - min(v)


def step_pairs(pm: Mapping[str, str], ps: Counter[str]) -> Counter[str]:
    psn: Counter[str] = Counter()

    for p in ps:
        c = ps[p]
        
        if c == 0:
            continue
        if p not in pm:
            psn[p] += c
            continue

        l = p[0]
        r = p[1]
        m = pm[p]
        psn[l + m] += c
        psn[m + r] += c

    return psn


def b(inp: AOCInput) -> AOCResult:
    t = inp[0]
    pm = create_pair_map(inp[1])
    ps = Counter((t[i] + t[i + 1]) for i in range(len(t) - 1))
    print(ps)

    for _ in range(40):
        ps = step_pairs(pm, ps)

    print(ps)

    c: Counter[str] = Counter()

    for (p, pc) in ps.items():
        if pc > 0:
            c[p[0]] += pc
            c[p[1]] += pc

    c[t[0]] += 1
    c[t[-1]] += 1

    v = c.values()
    return (max(v) - min(v)) // 2



# class StringBuilder:
#     def __init__(self) -> None:
#         self.s = ''

#     def add(self, s: str) -> None:
#         self.s += s

#     def get(self) -> str:
#         return self.s


# def multi_step_rec(pm: Mapping[str, str], s: StringBuilder, l: str, r: str, steps: int) -> None:
#     p = l + r

#     if steps == 0 or p not in pm:
#         # s.add(l)
#         return

#     m = pm[p]
#     multi_step_rec(pm, s, l, m, steps - 1)
#     multi_step_rec(pm, s, m, r, steps - 1)

# def multi_step(pm: Mapping[str, str], t: str, steps: int) -> str:
#     s = StringBuilder()

#     for i in range(len(t) - 1):
#         multi_step_rec(pm, s, t[i], t[i + 1], steps)

#     s.add(t[-1])
#     return s.get()


# def b(inp: AOCInput) -> AOCResult:
#     t = inp[0]
#     pm = create_pair_map(inp[1])

#     t = multi_step(pm, t, 40)
#     # print(t)
#     c = Counter(t)
#     v = c.values()

#     return max(v) - min(v)



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