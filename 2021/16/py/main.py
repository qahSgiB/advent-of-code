from typing import List, Tuple, Optional, Callable, Dict, Deque, Mapping, MutableMapping, Set, Iterable

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



AOCInput = str
AOCResult = int



class BitStream:
    def __init__(self, ba: bytearray) -> None:
        self.ba = ba
        self.index = 0

    def get(self) -> int:
        byte_index, bit_index = divmod(self.index, 8)
        bit = (self.ba[byte_index] >> (7 - bit_index)) & 1
        self.index += 1

        return bit

    def getn(self, n: int) -> int:
        byte_index, bit_index = divmod(self.index, 8)
        bit_rem = 8 - bit_index

        if bit_rem >= n:
            bits: int = (self.ba[byte_index] >> (bit_rem - n)) & (2 ** n - 1)
            self.index += n
            return bits

        bits = self.ba[byte_index] & (2 ** bit_rem - 1)
        n -= bit_rem
        byte_index += 1

        while n >= 8:
            bits <<= 8
            bits += self.ba[byte_index]
            byte_index += 1
            n -= 8

        bits <<= n
        bits += (self.ba[byte_index] >> (8 - n)) & (2 ** n - 1)

        self.index = 8 * byte_index + n
        return bits

    def skip(self, n: int) -> None:
        self.index += n

    def get_index(self) -> int:
        return self.index

    def set_index(self, i: int) -> None:
        self.index = i

    
    @staticmethod
    def from_hex(s: str) -> 'BitStream':
        return BitStream(bytearray.fromhex(s))



def packet_version_sum(ps: BitStream) -> int:
    v = ps.getn(3)
    t = ps.getn(3)

    if t == 4:
        while ps.get() == 1:
            ps.skip(4)
        ps.skip(4)
    else:
        lt = ps.get()
        if lt == 1:
            pn = ps.getn(11)
            for _ in range(pn):
                v += packet_version_sum(ps)
        else:
            pl = ps.getn(15)
            end = ps.get_index() + pl

            while ps.get_index() < end:
                v += packet_version_sum(ps)

    return v

def packet_value(ps: BitStream) -> int:
    v = ps.getn(3)
    t = ps.getn(3)


    if t == 4:
        x = 0
        while ps.get() == 1:
            x += ps.getn(4)
            x <<= 4
        x += ps.getn(4)

        return x

    pop: Callable[[List[int]], int] | None = None

    if t == 0:
        pop = sum
    elif t == 1:
        pop = lambda x: ft.reduce(op.mul, x)
    elif t == 2:
        pop = min
    elif t == 3:
        pop = max
    elif t == 5:
        pop = lambda x: 1 if x[0] > x[1] else 0
    elif t == 6:
        pop = lambda x: 1 if x[0] < x[1] else 0
    elif t == 7:
        pop = lambda x: 1 if x[0] == x[1] else 0

    if pop is None:
        return 0

    pas: List[int] = []

    lt = ps.get()
    if lt == 1:
        pn = ps.getn(11)
        for _ in range(pn):
            pas.append(packet_value(ps))
    else:
        pl = ps.getn(15)
        end = ps.get_index() + pl

        while ps.get_index() < end:
            pas.append(packet_value(ps))

    return pop(pas)


def parse(s: str) -> AOCInput:
    return s

def a(inp: AOCInput) -> AOCResult:
    return packet_version_sum(BitStream.from_hex(inp))

def b(inp: AOCInput) -> AOCResult:
    return packet_value(BitStream.from_hex(inp))



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