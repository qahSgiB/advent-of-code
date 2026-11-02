# pyright: reportUnusedImport=false

from typing import List, Tuple, Optional, Callable, Dict, Deque, Mapping, MutableMapping, Set, DefaultDict

from collections import deque, defaultdict, Counter

import operator as op
import functools as ft
import itertools as it

import heapq as hq

from copy import deepcopy

import math as ma
import random as ra

import time

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



AOCEl = Tuple[int, int, List[int], List[List[int]], List[int]] # count, target, buttons, buttons raw, target joltage
AOCInput = List[AOCEl]
AOCResult = int



def parse_el(s: str) -> AOCEl:
    a, b = cut2u(s, ']')
    
    a = a[1:]
    target = 0
    count = len(a)

    for c in a:
        target <<= 1
        if c == '#':
            target |= 1

    b = b[1:]
    d, e = cut2u(b, '{')
    
    d = d[:-1]
    buttons: List[int] = []
    buttons_raw: List[List[int]] = []

    for f in splits(d):
        g = f[1:-1]
        button = 0
        button_raw: List[int] = []

        for h in split(g, ','):
            i = int(h)
            button |= 1 << (count - i - 1)
            button_raw.append(i)

        buttons.append(button)
        buttons_raw.append(button_raw)

    e = e[:-1]
    target_j = lm(int, splitc(e))

    return (count, target, buttons, buttons_raw, target_j)

def parse(s: str) -> AOCInput:
    return lm(parse_el, remove_last_empty(split(s, '\n')))

def a(inp: AOCInput) -> AOCResult:
    s = 0
    for (_, target, buttons, _, _) in inp:
        mi = 1000

        for i in range(2 ** len(buttons)):
            j = i
            res = 0
            press = 0
            k = 0
            while j > 0:
                if j & 1 == 1:
                    res ^= buttons[k]
                    press += 1
                
                j >>= 1
                k += 1

            if res == target and press < mi:
                mi = press

        s += mi

    return s

def sub_add(a: List[int], b: List[int], c: int):
    for i in b:
        a[i] += c

def add(a: List[int], b: List[int]):
    for i in b:
        a[i] += 1

def f1(buttons: List[List[int]], have_to_finishs: List[List[int]], targets: List[int], button_index: int, rem_count: int) -> int:
    # print(button_index, buttons[button_index], targets)

    # all_zero = True
    # for target in targets:
    #     if target < 0:
    #         raise Exception('uh')
    #     elif target != 0:
    #         all_zero = False

    # if all_zero:
    #     return 0

    if all(target == 0 for target in targets):
        return 0
    
    if rem_count == 0:
        return 1001
    
    button = buttons[button_index]

    if button_index == len(buttons) - 1:
        t: int | None = None
        for (i, target) in enumerate(targets):
            if i in button:
                if target == 0:
                    return 1001
                elif t is None:
                    t = target
                elif target != t:
                    return 1001
            else:
                if target != 0:
                    return 1001

        assert t is not None

        if t > rem_count:
            return 1001

        # print('debug 1', button_index, t)
        return t

    have_to_finish = have_to_finishs[button_index]

    if len(have_to_finish) > 0:
        c = targets[have_to_finish[0]]
        for i in have_to_finish[1:]:
            if targets[i] != c:
                return 1001

        if c > rem_count:
            return 1001

        for i in button:
            if targets[i] < c:
                return 1001

        res = sub_add(targets, button, -c)

        res = f1(buttons, have_to_finishs, targets, button_index + 1, rem_count - c)
        if res != 1001:
            # print('debug 1', button_index, c)
            return res + c
        else:
            sub_add(targets, button, c)
            return 1001

    ma = 1000
    for i in button:
        ma = min(ma, targets[i])

    if ma > rem_count:
        return 1001

    sub_add(targets, button, -ma)
    next_button_index = button_index + 1

    for count in range(ma, -1, -1):
        res = f1(buttons, have_to_finishs, targets, next_button_index, rem_count - count)
        if res != 1001:
            # print('debug 1', button_index, count)
            return res + count

        if count > 0:
            add(targets, button)

    return 1001

def f2(buttons: List[List[int]], targets: List[int]) -> List[List[int]]:
    bms: List[Tuple[List[int], Tuple[int, int]]] = []
    for b in buttons:
        ma = 1000
        for i in b:
            ma = min(ma, targets[i])

        # bms.append((b.copy(), (ma, 1000 - len(b))))
        bms.append((b.copy(), (1000 - len(b), ma)))

    bms.sort(key = lambda b: b[1])
    # ra.shuffle(bms)

    return lm(nth(0), bms)

def f3(buttons: List[List[int]], count: int) -> List[List[int]]:
    last = [-1 for _ in range(count)]
    for i, button in enumerate(buttons):
        for j in button:
            last[j] = i

    have_to_finish: List[List[int]] = [[] for _ in range(len(buttons))]

    for i, l in enumerate(last):
        have_to_finish[l].append(i)

    return have_to_finish

def f4(buttons: List[List[int]], targets: List[int]) -> int:
    targets_orig = targets.copy()
    buttons = f2(buttons, targets)
    have_to_finish = f3(buttons, len(targets))

    print(buttons)

    # dumb_count = f5(buttons, targets.copy())
    # max_count = min(sum(targets) // len(buttons[-1]) + 1, dumb_count) + 1

    mi = 1000
    ma = 0
    for button in buttons:
        mi = min(mi, len(button))
        ma = max(ma, len(button))

    # min_count = max(min(targets), sum(targets) // ma)
    # max_count = sum(targets) // mi + 2
    test = 279
    print(f'!! real count: {test}')
    min_count = test - 69
    max_count = test - 69 + 2

    i = 0

    while True:
        if min_count + 1 == max_count:
            return min_count

        if i > 0:
            count = (min_count + max_count - 1) // 2
        else:
            count = min_count + (max_count - min_count - 1) * 1 // 2
        print(f'trying count {count} from <{min_count}, {max_count})')

        targets = targets_orig.copy()

        t = time.time()
        res = f1(buttons, have_to_finish, targets, 0, count)
        dur = time.time() - t

        if res != 1001:
            print(f'OK {dur:.2f}s {res}')
            max_count = res + 1
        else:
            print(f'NOK {dur:.2f}s')
            min_count = count + 1

        i += 1

def f5(buttons: List[List[int]], targets: List[int]) -> int:
    count = 0

    while any(t > 0 for t in targets):
        mbi = 1001
        mbc = 0
        for (bi, b) in enumerate(buttons):
            bc = sum(1 for i in b if targets[i] > 0)
            if bc > mbc:
                mbc = bc
                mbi = bi

        mb = buttons[mbi]

        print(mbi, mb, targets)

        c = min(targets[i] for i in mb if targets[i] > 0)
        sub_add(targets, mb, -c)
        count += c

    return count

# special solution for case 60
def f7(x9: int, x12: int, x13: int) -> int | None:
    x1 = 12 - x12 + x13
    x2 = 20 - 2 * x9 + 3 * x12 - 4 * x13
    x3 = 57 + 2* x9 - 6 * x12 + 5 * x13
    x4 = -1 - 2 * x9 + 4 * x12 - 4 * x13
    x5 = -9 + 3 * x12 - 3 * x13
    x6 = 4 - x9 + 2 * x12 - 2 * x13
    x7 = 109 + x9 - 3 * x12 + 3 * x13
    x8 = 36 + 2 * x9 - 5 * x12 + 5 * x13
    x10 = -3 + x12
    x11 = -32 + 2 * x12

    if any(x < 0 for x in [x1, x2, x3, x4, x5, x6, x7, x8, x10, x11]):
        return None
    
    return sum([x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13])

def f6() -> int:
    mic = 1000

    for x9 in range(61 + 1):
        for x12 in range(80 + 1):
            for x13 in range(59 + 1):
                c = f7(x9, x12, x13)
                if c is not None:
                    if c < mic:
                        mic = c

    return mic

def b(inp: AOCInput) -> AOCResult:
    s = 0
    # for (ii, (_, _, _, buttons, target_o)) in enumerate(inp):
    #     # if ii not in [60]:
    #     #     continue

    #     print(f'STARTING  {ii}')
    #     res = f4(buttons, target_o)
    #     s += res
    #     print(f'  ==>  count: {res} (total: {s})')
    #     print(f'FINISHED  {ii}')
    #     print()

    #     if res == 1001:
    #         print('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')

    s += f6() + 69

    return s

def b1(inp: AOCInput) -> AOCResult:
    # greedy
    s = 0

    for (ii, (_, _, _, buttons, target_o)) in enumerate(inp):
        target = target_o.copy()

        ls = 0
        done = [False for _ in range(len(target))]

        while True:
            best_t = 1000
            for i in range(len(target)):
                if target[i] > 0 and target[i] < best_t:
                    best_t = target[i]

            if best_t == 1000:
                break

            best_ti = 0
            best_bi = 0
            best_bc = 0

            for (ti, t) in enumerate(target):
                if t != best_t:
                    continue

                bis: List[int] = []
                for bi, button in enumerate(buttons):
                    if ti in button:
                        bis.append(bi)

                if len(bis) == 1:
                    best_ti = ti
                    best_bi = bis[0]
                    best_bc = 1000
                    break

                for bi in bis:
                    bc = 0
                    for i in buttons[bi]:
                        if target[i] > 0:
                            bc += 1
                        if target[i] == 0:
                            bc = 1000
                            break

                    if bc == 1000:
                        continue

                    if bc > best_bc:
                        best_ti = ti
                        best_bi = bi
                        best_bc = bc

            # print(best_bi, best_ti, best_bc)

            if best_bc == 0:
                # print('totola je velky problem')
                print(ii)
                # print(buttons, target)
                break

            t = target[best_ti]

            for i in buttons[best_bi]:
                target[i] -= t
                if target[i] == 0:
                    done[i] = True

            ls += t

        s += ls

    return s



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

# time: 22:05 / second part completed on 15.12 0:58
# greedy buttons order prerocessing
# dfs with limit
# binary serach on limit for dfs
# "heuristic" guess on min and max for limit
# have_to_finish "heuristic"
# last_button "heuristic"
# greedy pressing of buttons
# multiple simultaneous runs => summing in solution-counter.txt
# case 60 was too slow
# special solution used
# first manual solution was tried in excel, didn't work
# set of linear equations => guassian elimation => solution with 3 free variables => try all posiblle combinations with bounds manually derived in excel