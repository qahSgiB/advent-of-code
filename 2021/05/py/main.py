from typing import DefaultDict, List, Set, Tuple, Optional, Callable, Dict, Deque

from collections import defaultdict, deque

import operator as op
import functools as ft
import itertools as it

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
##
##  APLHABET
##  APLHABETU
##  DIGITS
##
##
##
##  nth (op.itemgetter)
##  ft.reduce



AOCInput = List[Tuple[Tuple[int, int], Tuple[int, int]]]
AOCResult = int



HOR = 0
VER = 1
JUJ = 2



def parse_el(s: str) -> Tuple[int, int]:
    (x, y) = cut2u(s, ',')
    return (int(x), int(y))

def parse_line(s: str) -> Tuple[Tuple[int, int], Tuple[int, int]]:
    (a, b) = cut2u(s, ' -> ')
    return (parse_el(a), parse_el(b))

def parse(s: str) -> AOCInput:
    return lm(parse_line, splitn(s))

def line_dir(l: Tuple[Tuple[int, int], Tuple[int, int]]) -> int:
    ((ax, ay), (bx, by)) = l
    
    if ax == bx:
        return VER
    elif ay == by:
        return HOR
    
    return JUJ

def overlap(a0: int, a1: int, b0: int, b1: int) -> Tuple[int, int] | None:
    if a0 > a1:
        (a0, a1) = (a1, a0)

    if b0 > b1:
        (b0, b1) = (b1, b0)

    if a1 < b0 or a0 > b1:
        return None

    [_, i1, i2, _] = sorted([a0, a1, b0, b1])
    return (i1, i2)

def step(a: int, b: int) -> int:
    if a == b:
        return 0
    
    return 1 if b > a else -1

def a(inp: AOCInput) -> AOCResult:
    st = list(filter(lambda x: line_dir(x) in [HOR, VER], inp))

    inter: Set[Tuple[int, int]] = set()

    for (oi, o) in enumerate(st):
        for (pi, p) in enumerate(st):
            if oi == pi:
                continue

            ((oax, oay), (obx, oby)) = o
            ((pax, pay), (pbx, pby)) = p
            
            o_dir = line_dir(o)
            p_dir = line_dir(p)

            if o_dir == p_dir:
                if o_dir == HOR and oay == pay and (i := overlap(oax, obx, pax, pbx)) is not None:
                    (i1, i2) = i
                    for x in range(i1, i2 + 1):
                        inter.add((x, oay))
                elif o_dir == VER and oax == pax and (i := overlap(oay, oby, pay, pby)) is not None:
                    (i1, i2) = i
                    for y in range(i1, i2 + 1):
                        inter.add((oax, y))
            else:
                if o_dir == VER:
                    (oax, oay, obx, oby, pax, pay, pbx, pby) = (pax, pay, pbx, pby, oax, oay, obx, oby)

                if (in_range(oax, obx, pax) or in_range(obx, oax, pax)) and (in_range(pay, pby, oay) or in_range(pby, pay, oay)):
                    inter.add((pax, oay))

    return len(inter)

def b(inp: AOCInput) -> AOCResult:
    grid: DefaultDict[Tuple[int, int], int] = defaultdict(lambda : 0)

    for l in inp:
        ((lax, lay), (lbx, lby)) = l
        l_dir = line_dir(l)

        if l_dir == HOR:
            for x in range(min(lax, lbx), max(lbx, lax) + 1):
                p = (x, lay)
                grid[p] = grid[p] + 1
        elif l_dir == VER:
            for y in range(min(lay, lby), max(lby, lay) + 1):
                p = (lax, y)
                grid[p] = grid[p] + 1
        else:
            sx = step(lax, lbx)
            sy = step(lay, lby)

            for p in zip(range(lax, lbx + sx, sx), range(lay, lby + sy, sy)):
                grid[p] = grid[p] + 1

    return len(list(filter(lambda x: x >= 2, grid.values())))



if __name__ == '__main__':
    inp = parse(load_file('inp.txt'))
    print(a(inp))
    print(b(inp))