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



EMPTY = 0
TILE = 1


ROCKS = [[[1, 1, 1, 1]], [[0, 1, 0], [1, 1, 1], [0, 1, 0]], [[1, 1, 1], [0, 0, 1], [0, 0, 1]], [[1], [1], [1], [1]], [[1, 1], [1, 1]]]



AOCInput = str
AOCResult = int



def parse(s: str) -> AOCInput:
    return s[:(-1)]


def cc(chamber: List[List[int]], width: int, rock: List[List[int]], x: int, y: int) -> bool:
    height = len(chamber)

    max_x = width - len(rock[0])

    if y < 0 or x < 0 or x > max_x:
        return True

    for dy, tiles in enumerate(rock):
        ry = y + dy
        if ry >= height:
            break

        for dx, tile in enumerate(tiles):
            rx = x + dx
            if tile == 1 and chamber[ry][rx] == 1:
                return True
    
    return False

def a(jets: AOCInput) -> AOCResult:
    width = 7

    chamber: List[List[int]] = []

    jet_index = 0

    for rock_index in range(2022):
        # print('-' * (width + 2))
        # print('\n'.join(map(lambda tiles: ' ' + ''.join(map(lambda tile: '.' if tile == 0 else '#', tiles)), reversed(chamber))))
        rock_id = rock_index % len(ROCKS)
        rock = ROCKS[rock_id]

        height = len(chamber)

        x = 2
        y = height + 3

        while True:
            jet = jets[jet_index]
            jet_index = (jet_index + 1) % len(jets)

            jet_dir = 1 if jet == '>' else -1
            if not cc(chamber, width, rock, x + jet_dir, y):
                x += jet_dir

            if cc(chamber, width, rock, x, y - 1):
                for dy, tiles in enumerate(rock):
                    ry = y + dy
                    if ry >= height:
                        chamber.append([0 for _ in range(width)])

                    for dx, tile in enumerate(tiles):
                        rx = x + dx
                        if tile == 1:
                            chamber[ry][rx] = 1

                break

            y -= 1

    return len(chamber)

def cc_b(chamber_b: List[int], width: int, rock_bs: Tuple[List[int], int], x: int, y: int) -> bool:
    rock_b, rock_width = rock_bs

    height = len(chamber_b)
    max_x = width - rock_width

    if y < 0 or x < 0 or x > max_x:
        return True

    for dy, row_b in enumerate(rock_b):
        ry = y + dy
        if ry >= height:
            break

        if chamber_b[ry] & (row_b << x) > 0:
            return True
    
    return False

def b(jets: AOCInput) -> AOCResult:
    total_count = 1000000000000
    # total_count = 2022
    width = 7

    rocks_b = [([sum((1 << x if tile == 1 else 0) for x, tile in enumerate(row)) for row in rock], len(rock[0])) for rock in ROCKS]

    # for rock in rocks_b:
    #     for row in reversed(rock[0]):
    #         print(bin(row))
    #     print('')

    chamber_b: List[int] = []

    jet_index = 0
    rock_index = 0

    starts: Dict[Tuple[int, int], Tuple[int, int]] = {}
    skip = True

    height_add = 0

    while True:
        # print('-' * (width + 2))
        # print('\n'.join(map(lambda row_b: f' {row_b:0>7b}', reversed(chamber_b))))
        rock_id = rock_index % len(ROCKS)
        rock_bs = rocks_b[rock_id]

        height = len(chamber_b)

        if skip:
            if (rock_id, jet_index) in starts:
                # print('-' * (width + 2))
                # print('\n'.join(map(lambda row_b: f' {row_b:0>7b}', reversed(chamber_b))))
                last_rock_index, last_height = starts[(rock_id, jet_index)]
                rock_count = rock_index - last_rock_index
                height_diff = height - last_height
                # print(last_rock_index, rock_index)

                repeat = (total_count - rock_index) // rock_count
                if rock_count * repeat + rock_index == total_count: ## wtf
                    height_add += height_diff * repeat
                    rock_index += rock_count * repeat

                    skip = False
            else:
                starts[(rock_id, jet_index)] = (rock_index, height)

        if rock_index == total_count:
            return height + height_add

        x = 2
        y = height + 3

        while True:
            jet = jets[jet_index]
            jet_index = (jet_index + 1) % len(jets)

            jet_dir = 1 if jet == '>' else -1
            if not cc_b(chamber_b, width, rock_bs, x + jet_dir, y):
                x += jet_dir

            if cc_b(chamber_b, width, rock_bs, x, y - 1):
                for dy, row_b in enumerate(rock_bs[0]):
                    ry = y + dy
                    if ry >= height:
                        chamber_b.append((row_b) << x)
                    else:
                        chamber_b[ry] |= row_b << x

                break

            y -= 1

        rock_index += 1



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