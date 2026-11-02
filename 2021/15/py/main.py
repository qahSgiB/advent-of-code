from typing import Generic, List, Tuple, Optional, Callable, Dict, Deque, Mapping, MutableMapping, Set, TypeVar

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



AOCEl = List[int]
AOCInput = List[AOCEl]
AOCResult = int



HK = TypeVar('HK')
HV = TypeVar('HV')
class HeHeHeap(Generic[HK, HV]):
    def __init__(self, cmp: Callable[[HV, HV], bool]):
        self.l: List[Tuple[HK, HV]] = []
        self.index_map: Dict[HK, int] = {}
        self.cmp = cmp

    def get_parent_index(self, i: int) -> int: return (i - 1) // 2
    def get_left_index(self, i: int) -> int: return i * 2 + 1
    def get_right_index(self, i: int) -> int: return i * 2 + 2

    def repair_index_map(self, i: int) -> None:
        self.index_map[self.l[i][0]] = i

    def swap(self, ia: int, ib: int) -> None:
        self.l[ia], self.l[ib] = self.l[ib], self.l[ia]
        self.repair_index_map(ia)
        self.repair_index_map(ib)

    def down_heap(self, i: int) -> None:
        while True:
            li = self.get_left_index(i)
            if li >= len(self.l):
                break

            ri = self.get_right_index(i)
            if ri >= len(self.l):
                if self.cmp(self.l[i][1], self.l[li][1]):
                    self.swap(i, li)
                    i = li
                    continue
                break

            e = self.l[i][1]
            le = self.l[li][1]
            re = self.l[ri][1]

            lok = self.cmp(le, e)
            rok = self.cmp(re, e)
            if lok and rok: break

            ni = li if rok or ((not lok) and (not rok) and (not self.cmp(le, re))) else ri
            self.swap(i, ni)
            i = ni

    def up_heap(self, i: int) -> None:
        pi = self.get_parent_index(i)
        while i != 0 and self.cmp(self.l[pi][1], self.l[i][1]):
            self.swap(i, pi)
            i = pi
            pi = self.get_parent_index(i)

    def get_max(self) -> Tuple[HK, HV]:
        return self.l[0]

    def pop_max(self) -> Tuple[HK, HV]:
        n = self.l[0]

        if len(self.l) == 1:
            self.l.pop()
            return n
        
        self.l[0] = self.l.pop()
        self.repair_index_map(0)
        self.index_map.pop(n[0])

        self.down_heap(0)

        return n

    def insert(self, k: HK, e: HV) -> None:
        self.l.append((k, e))

        i = len(self.l) - 1
        self.repair_index_map(i)
        self.up_heap(i)

    def decrease_key(self, k: HK, e: HV) -> None:
        i = self.index_map[k]
        self.l[i] = (k, e)
        self.down_heap(i)

    def increase_key(self, k: HK, e: HV) -> None:
        i = self.index_map[k]
        self.l[i] = (k, e)
        self.up_heap(i)

    def set_key(self, k: HK, e: HV) -> None:
        if self.cmp(self.l[self.index_map[k]][1], e):
            self.increase_key(k, e)
        else:
            self.decrease_key(k, e)



def parse_el(s: str) -> AOCEl:
    return lm(int, s)

def parse(s: str) -> AOCInput:
    return lm(parse_el, remove_last_empty(split(s, '\n')))

def a(inp: AOCInput) -> AOCResult:
    risk_map = inp
    w = len(risk_map[0])
    h = len(risk_map)

    visited = [[False for _ in range(w)] for _ in range(h)]
    dist = [[-1 for _ in range(w)] for _ in range(h)]
    unvisited_dist: HeHeHeap[Tuple[int, int], int] = HeHeHeap(lambda a, b: a > b)

    visited[0][0] = True
    dist[0][0] = 0
    unvisited_dist.insert((0, 0), 0)

    while not visited[h - 1][w - 1]:
        ((cur_x, cur_y), cur_dist) = unvisited_dist.pop_max()

        for (nx, ny) in iter_neigh_wh4(cur_x, cur_y, w, h):
            if not visited[ny][nx]:
                n_dist = dist[ny][nx]
                n_cur_dist = cur_dist + risk_map[ny][nx]

                if n_dist == -1:
                    unvisited_dist.insert((nx, ny), n_cur_dist)
                    dist[ny][nx] = n_cur_dist
                elif n_cur_dist < n_dist:
                    unvisited_dist.increase_key((nx, ny), n_cur_dist)
                    dist[ny][nx] = n_cur_dist

        visited[cur_y][cur_x] = True

    return dist[h - 1][w - 1]

def b(inp: AOCInput) -> AOCResult:
    risk_map = inp
    w = len(risk_map[0])
    h = len(risk_map)
    w5 = w * 5
    h5 = h * 5

    visited = [[False for _ in range(w5)] for _ in range(h5)]
    dist = [[-1 for _ in range(w5)] for _ in range(h5)]
    unvisited_dist: HeHeHeap[Tuple[int, int], int] = HeHeHeap(lambda a, b: a > b)

    visited[0][0] = True
    dist[0][0] = 0
    unvisited_dist.insert((0, 0), 0)

    while not visited[h5 - 1][w5 - 1]:
        ((cur_x, cur_y), cur_dist) = unvisited_dist.pop_max()

        for (nx, ny) in iter_neigh_wh4(cur_x, cur_y, w5, h5):
            if not visited[ny][nx]:
                n_dist = dist[ny][nx]
                
                tile_x = nx // w
                tile_y = ny // h
                tile_inc = tile_x + tile_y
                risk = (risk_map[ny % h][nx % w] + tile_inc - 1) % 9 + 1
                n_cur_dist = cur_dist + risk

                if n_dist == -1:
                    unvisited_dist.insert((nx, ny), n_cur_dist)
                    dist[ny][nx] = n_cur_dist
                elif n_cur_dist < n_dist:
                    unvisited_dist.increase_key((nx, ny), n_cur_dist)
                    dist[ny][nx] = n_cur_dist

        visited[cur_y][cur_x] = True

    return dist[h5 - 1][w5 - 1]



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