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



Cube = Tuple[int, int, int, int, int, int]
CubeOn = Tuple[bool, Cube]

AOCEl = CubeOn
AOCInput = List[AOCEl]
AOCResult = int



def parse_el(s: str) -> AOCEl:
    tons, s = cut2u(s, ' ')
    ton = tons == 'on'

    xs, ys, zs = cut3u(s, ',', ',')
    xmin, xmax = cut2u(xs[2:], '..')
    ymin, ymax = cut2u(ys[2:], '..')
    zmin, zmax = cut2u(zs[2:], '..')

    return (ton, (int(xmin), int(xmax), int(ymin), int(ymax), int(zmin), int(zmax)))

def parse(s: str) -> AOCInput:
    return lm(parse_el, remove_last_empty(split(s, '\n')))

def a(inp: AOCInput) -> AOCResult:
    cubes: List[CubeOn] = []
    for ton, (xmin, xmax, ymin, ymax, zmin, zmax) in inp:
        xmin = max(xmin, -50)
        ymin = max(ymin, -50)
        zmin = max(zmin, -50)
        xmax = min(xmax + 1, 51)
        ymax = min(ymax + 1, 51)
        zmax = min(zmax + 1, 51)
        cubes.append((ton, (xmin, xmax, ymin, ymax, zmin, zmax)))

    on: DefaultDict[Tuple[int, int, int], bool] = defaultdict(lambda : True)

    for ton, (xmin, xmax, ymin, ymax, zmin, zmax) in cubes:
        for x in range(xmin, xmax):
            for y in range(ymin, ymax):
                for z in range(zmin, zmax):
                    on[(x, y, z)] = ton

    return count(lambda x : x, on.values())

def get_intersection_1(amin: int, amax: int, bmin: int, bmax: int) -> Tuple[int, int] | None:
    if amax < bmin and amin < bmin:
        return None

    if bmax < amin and bmax < amax:
        return None

    _, mmin, mmax, _ = sorted([amin, amax, bmin, bmax])
    return mmin, mmax

def get_intersection_3(ca: Cube, cb: Cube) -> Cube | None:
    xm = get_intersection_1(ca[0], ca[1], cb[0], cb[1])
    if xm is None:
        return None

    ym = get_intersection_1(ca[2], ca[3], cb[2], cb[3])
    if ym is None:
        return None

    zm = get_intersection_1(ca[4], ca[5], cb[4], cb[5])
    if zm is None:
        return None

    return (xm[0], xm[1], ym[0], ym[1], zm[0], zm[1])

def calculate_volume_3(ca: Cube) -> int:
    return (ca[1] - ca[0] + 1) * (ca[3] - ca[2] + 1) * (ca[5] - ca[4] + 1)

def clamp_cube(clamp: Cube, c: Cube) -> Cube | None:
    xmin = max(c[0], clamp[0])
    ymin = max(c[2], clamp[2])
    zmin = max(c[4], clamp[4])
    xmax = min(c[1], clamp[1])
    ymax = min(c[3], clamp[3])
    zmax = min(c[5], clamp[5])

    if xmax < xmin or ymax < ymin or zmax < zmin:
        return None

    return (xmin, xmax, ymin, ymax, zmin, zmax)

def b(inp: AOCInput) -> AOCResult:
    cubes: List[Cube] = lm(nth(1), inp)
    count = 0
    
    ign: List[List[Tuple[Cube, Set[int]]]] = []

    for ci, (ton, c) in enumerate(reversed(inp)):
        if ton:
            vol = calculate_volume_3(c)

            sign = -1
            for ign_cs in ign:
                for ign_c, _ in ign_cs:
                    ci_cl = clamp_cube(c, ign_c)
                    if ci_cl is None:
                        continue

                    vol += sign * calculate_volume_3(ci_cl)

                sign *= - 1

            count += vol

        addigns = [(c, {ci})]
        ign_level = 0
        while len(addigns) > 0:
            naddigns: List[Tuple[Cube, Set[int]]] = []

            if ign_level < len(ign):
                for ign_c, ign_cis in ign[ign_level]:
                    if ci in ign_cis:
                        continue
                    
                    inter = get_intersection_3(c, ign_c)
                    if inter is None:
                        continue

                    naddigns.append((inter, ign_cis | {ci}))

            if len(ign) <= ign_level:
                ign.append([])

            ign[ign_level].extend(addigns.copy())
            addigns = naddigns
            ign_level += 1

    return count



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