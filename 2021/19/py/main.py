from typing import List, Tuple, Optional, Callable, Dict, Deque, Mapping, MutableMapping, Set, Iterable

from collections import deque, defaultdict, Counter

import operator as op
import functools as ft
import itertools as it

import heapq as hq

from copy import deepcopy

import math as ma
import random as rd

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



P3 = Tuple[int, int, int]
CoordsPerm = Tuple[int, int, int, int, int, int]

AOCEl = List[P3]
AOCInput = List['Scanner']
AOCResult = int



PERMS = [(x, y, z, mx, my, mz) for x, y, z in [(0, 1, 2), (0, 2, 1), (1, 0, 2), (1, 2, 0), (2, 0, 1), (2, 1, 0)] for mx in [-1, 1] for my in [-1, 1] for mz in [-1, 1]]



def parse_point(s: str) -> P3:
    x, y, z = cut3u(s, ',', ',')
    return int(x), int(y), int(z)

def parse_el(s: str) -> AOCEl:
    _, lines = first(remove_last_empty(split(s, '\n')))
    return lm(parse_point, lines)

def parse(s: str) -> AOCInput:
    inp = lm(parse_el, remove_last_empty(split(s, '\n\n')))
    scanners = [Scanner(report, f'{index:2}') for index, report in enumerate(inp)]
    solve_scanners(scanners)
    return scanners



class Scanner:
    def __init__(self, report: List[P3], name: str | None = None):
        self.beacons = set(report)
        self.name = '' if name is None else name
        self.pos = (0, 0, 0)

        self.beacons_perms: List[Set[P3]] = []

    def create_perms(self) -> None:
        if len(self.beacons_perms) > 0:
            return

        for cp in PERMS:
            self.beacons_perms.append({ transform(p, cp) for p in self.beacons })



def p3_add(a: P3, b: P3) -> P3:
    return (a[0] + b[0], a[1] + b[1], a[2] + b[2])

def p3_diff(a: P3, b: P3) -> P3:
    return (a[0] - b[0], a[1] - b[1], a[2] - b[2])

def p3_manh_dist(a: P3, b: P3) -> int:
    (dx, dy, dz) = p3_diff(a, b)
    return abs(dx) + abs(dy) + abs(dz)


def transform(pos: P3, cp: CoordsPerm) -> P3:
    x = pos[cp[0]] * cp[3]
    y = pos[cp[1]] * cp[4]
    z = pos[cp[2]] * cp[5]
    return x, y, z

# def get_inverse_transform(cp: CoordsPerm) -> CoordsPerm:
#     cpi = [0, 0, 0, 0, 0, 0]
#     cpi[cp[0]] = 0
#     cpi[cp[1]] = 1
#     cpi[cp[2]] = 2
#     cpi[cp[0] + 3] = cp[3]
#     cpi[cp[1] + 3] = cp[4]
#     cpi[cp[2] + 3] = cp[5]

#     return (cpi[0], cpi[1], cpi[2], cpi[3], cpi[4], cpi[5])


def pair_points(a: P3, b: P3, points_a: Set[P3], points_b: Set[P3]) -> P3 | None:
    off = p3_diff(a, b)
    point_b_t = { p3_add(b, off) for b in points_b }

    return off if len(points_a & point_b_t) >= 11 else None

def pair_scanners(scanner_a: Scanner, scanner_b: Scanner) -> bool:
    points_a = scanner_a.beacons.copy()
    scanner_b.create_perms()

    while len(points_a) >= 12:
        point_a = points_a.pop()

        for points_b in scanner_b.beacons_perms:
            for point_b in points_b:
                points_b.remove(point_b)
                off = pair_points(point_a, point_b, points_a, points_b)
                points_b.add(point_b)

                if off is not None:
                    scanner_b.pos = off
                    scanner_b.beacons = { p3_add(b, off) for b in points_b }
                    return True

    return False

def solve_scanners(scanners: List[Scanner]) -> None:
    todo_scanners: Dict[Scanner, Set[Scanner]] = { scanner: set() for scanner in scanners }
    scanners_map: List[List[Scanner]] = []

    start_scanner = scanners[0]
    todo_scanners.pop(start_scanner)
    scanners_map.append([start_scanner])

    while len(todo_scanners) > 0:
        print(f'  ===========  paired count : {len(scanners) - len(todo_scanners)}  ===========')

        scanner_group = scanners_map[-1]
        pop_scanners: Set[Scanner] = set()

        for scanner, ignore in todo_scanners.items():
            for p_scanner in scanner_group:
                if p_scanner in ignore:
                    continue

                print(p_scanner.name, scanner.name)
                if pair_scanners(p_scanner, scanner):
                    print(f'pairred {p_scanner.name} {scanner.name}')
                    pop_scanners.add(scanner)
                    break
                
                ignore.add(p_scanner)

        for pop_scanner in pop_scanners:
            todo_scanners.pop(pop_scanner)
            scanner_group.append(pop_scanner)

        if len(pop_scanners) == 0:
            scanners_map.append([todo_scanners.popitem()[0]])

def get_beacons(scanners: Iterable[Scanner]) -> Set[P3]:
    beacons: Set[P3] = set()
    for scanner in scanners:
        beacons.update(scanner.beacons)

    return beacons


def a(inp: AOCInput) -> AOCResult:
    scanners = inp
    beacons = get_beacons(scanners)

    return len(beacons)

def b(inp: AOCInput) -> AOCResult:
    scanners = inp

    dist = 0
    for a_index, a in enumerate(scanners):
        for b in it.islice(scanners, a_index + 1, len(scanners)):
            ab_dist = p3_manh_dist(a.pos, b.pos)
            if ab_dist > dist:
                dist = ab_dist

    return dist



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