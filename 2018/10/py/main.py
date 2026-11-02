from typing import List, Tuple, Optional, Callable, Dict, Deque

from collections import deque

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
##  APLHABET
##  APLHABETU
##  DIGITS
##
##
##
##  op.itemgetter
##  ft.reduce



AOCInput = List[Tuple[Tuple[int, int], Tuple[int, int]]]
AOCResult = int



def parse_point(s: str) -> Tuple[int, int]:
    print(s)
    (x, y) = cut2u(unparenlr(s, '<', '>'), ', ')
    return (int(x), int(y))

def parse_line(line: str) -> Tuple[Tuple[int, int], Tuple[int, int]]:
    print(line)
    (_, p, v) = cut3u(line, 'position=', ' velocity=')
    return (parse_point(p), parse_point(v))

def parse(s: str) -> AOCInput:
    return list(map(parse_line, remove_last_empty(splitn(s))))

# def draw(poss: List[Tuple[int, int]]) -> None:
    

def ab(inp: AOCInput) -> AOCResult:
    poss = list(map(op.itemgetter(0), inp))
    vels = list(map(op.itemgetter(1), inp))

    second = 0

    while True:
        (minx, miny) = (min(map(op.itemgetter(0), poss)), min(map(op.itemgetter(1), poss)))
        (maxx, maxy) = (max(map(op.itemgetter(0), poss)), max(map(op.itemgetter(1), poss)))

        print(f' second : {second}')
        print(f' size : {maxx - minx} x {maxy - miny}')
        d = input(' draw ? ')
        if d == 'y':
            for y in range(miny, maxy + 1):
                line = ''
                for x in range(minx, maxx + 1):
                    line += '#' if (x, y) in poss else '.'
                
                print(line)
        
        steps = 1 if d == '' or d == 'y' else 10 ** int(d)

        for _ in range(steps):
            for (i, (pos, vel)) in enumerate(zip(poss, vels)):
                poss[i] = (pos[0] + vel[0], pos[1] + vel[1])

        second += steps



if __name__ == '__main__':
    inp = parse(load_file('inp.txt'))
    print(ab(inp))