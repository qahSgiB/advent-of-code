from typing import DefaultDict, List, Tuple, Optional, Callable, Dict, Deque, Set

from collections import deque, defaultdict, Counter

import operator as op
import functools as ft
import itertools as it

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
##  APLHABET
##  APLHABETU
##  DIGITS
##
##
##
##  nth (op.itemgetter)
##  ft.reduce



AOCEl = Tuple[List[Set[str]], List[Set[str]]]
AOCInput = List[AOCEl]
AOCResult = int



def parse_el(s: str) -> AOCEl:
    l, r = cut2u(s, ' | ')
    return (lm(set, split(l, ' ')), lm(set, split(r, ' ')))

def parse(s: str) -> AOCInput:
    return lm(parse_el, split(s, '\n'))

def is_basic(d: Set[str]) -> bool:
    return len(d) in [2, 3, 4, 7]

def count_basic(ds: List[Set[str]]) -> int:
    return sum(1 for d in ds if is_basic(d))

def a(inp: AOCInput) -> AOCResult:
    return sum(count_basic(r) for (_, r) in inp)

# 2: 1
# 3: 7
# 4: 4
# 5: 2, 3, 5
# 6: 0, 6, 9
# 7: 8

def get_digit(d: Set[str], m: Dict[str, str]) -> int:
    ld = len(d)

    if ld == 2:
        return 1
    elif ld == 3:
        return 7
    elif ld == 4:
        return 4
    elif ld == 5:
        if m['b'] in d:
            return 5
        elif m['e'] in d:
            return 2
        return 3
    elif ld == 6:
        if m['d'] not in d:
            return 0
        if m['c'] not in d:
            return 6
        return 9
    
    return 8

def b(inp: AOCInput) -> AOCResult:
    s = 0
    for (l, r) in inp:
        m: Dict[str, Set[str]] = { k: set() for k in 'abcdefg' }

        dl: DefaultDict[int, List[Set[str]]] = defaultdict(list)
        for d in l:
            dl[len(d)].append(d)

        m['a'] = dl[3][0] - dl[2][0]
        m['c'] = dl[2][0].copy()
        m['f'] = dl[2][0].copy()
        m['b'] = (dl[4][0] - dl[2][0]).copy()
        m['d'] = (dl[4][0] - dl[2][0]).copy()

        ms6: Set[str] = set((set('abcdefg') - d).pop() for d in dl[6])

        m['c'] &= ms6
        m['f'] -= m['c']
        m['d'] &= ms6
        m['b'] -= m['d']
        m['e'] = ms6 - (m['c'] | m['d'])
        m['g'] = set('abcdefg') - (m['a'] | m['b'] | m['c'] | m['d'] | m['e'] | m['f'])

        rm = { f: t.pop() for (f, t) in m.items() }
        s += sum((10 ** (3 - i)) * get_digit(r[i], rm) for i in range(4))

    return s



if __name__ == '__main__':
    inp = parse(load_file('inp.txt'))
    print(a(inp))
    print(b(inp))