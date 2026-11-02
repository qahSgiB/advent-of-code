# pylint: disable=unused-import, unused-wildcard-import

from typing import List, Tuple, Optional, Callable, Dict, Deque, Any, Set

from collections import deque, defaultdict, Counter

import operator as op
import functools as ft
import itertools as it

import math as ma

import dataclasses as da

import enum as en


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



@da.dataclass
class WInt:
    n: int = 0

    def maxxer(self, o: int) -> bool:
        if o > self.n:
            self.n = o
            return True

        return False



Blueprint = Tuple[Tuple[int, int, int, int], Tuple[int, int, int, int], Tuple[int, int, int, int], Tuple[int, int, int, int]]
BlueprintWID = Tuple[int, Blueprint]



AOCEl = BlueprintWID
AOCInput = List[AOCEl]
AOCResult = int



def parse_el(s: str) -> AOCEl:
    ints = string_parse_ints(10, s)
    return (ints[0], ((ints[1], 0, 0, 0), (ints[2], 0, 0, 0), (ints[3], ints[4], 0, 0), (ints[5], 0, ints[6], 0)))

def parse(s: str) -> AOCInput:
    return lm(parse_el, remove_last_empty(splitn(s)))

def do(bp: Blueprint, rocks: Tuple[int, int, int, int], robots: Tuple[int, int, int, int], time: int, s: WInt) -> None:
    if time == 0:
        if s.maxxer(rocks[3]):
            print(rocks[3])
        return

    n_rocks = (rocks[0] + robots[0], rocks[1] + robots[1], rocks[2] + robots[2], rocks[3] + robots[3])

    robot_bp = bp[3]
    if robot_bp[0] <= rocks[0] and robot_bp[2] <= rocks[2]:
        do(bp, (n_rocks[0] - robot_bp[0], n_rocks[1], n_rocks[2] - robot_bp[2], n_rocks[3]), (robots[0], robots[1], robots[2], robots[3] + 1), time - 1, s)

    robot_bp = bp[2]
    if robot_bp[0] <= rocks[0] and robot_bp[1] <= rocks[1]:
        do(bp, (n_rocks[0] - robot_bp[0], n_rocks[1] - robot_bp[1], n_rocks[2], n_rocks[3]), (robots[0], robots[1], robots[2] + 2, robots[3]), time - 1, s)

    robot_bp = bp[1]
    if robot_bp[0] <= rocks[0]:
        do(bp, (n_rocks[0] - robot_bp[0], n_rocks[1], n_rocks[2], n_rocks[3]), (robots[0], robots[1] + 1, robots[2], robots[3]), time - 1, s)

    robot_bp = bp[0]
    if robot_bp[0] <= rocks[0]:
        do(bp, (n_rocks[0] - robot_bp[0], n_rocks[1], n_rocks[2], n_rocks[3]), (robots[0] + 1, robots[1], robots[2], robots[3]), time - 1, s)

    do(bp, n_rocks, robots, time - 1, s)

def a(inp: AOCInput) -> AOCResult:
    s = 0

    for (bid, bp) in inp:
        bs = WInt()
        do(bp, (0, 0, 0, 0), (1, 0, 0, 0), 24, bs)
        s += bs.n * bid

    return s

def b(inp: AOCInput) -> AOCResult:
    return 0



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