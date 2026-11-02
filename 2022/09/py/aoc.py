from typing import Any, Callable, Dict, Iterable, Iterator, List, Tuple, TypeVar

import operator as op



##  ===================================================  read file  ===================================================

def load_file(file_path: str | None = None) -> str:
    if file_path is None:
        file_path = 'inp.txt'

    with open(file_path, 'r', encoding='utf-8') as file_:
        return file_.read()

def load_file_lines(file_path: str | None = None) -> List[str]:
    if file_path is None:
        file_path = 'inp.txt'

    with open(file_path, 'r', encoding='utf-8') as file_:
        return remove_last_empty(list(map(remove_newline, iter(file_))))


##  ===================================================  file contents removes  ===================================================

def remove_newline(l: str) -> str:
    return l[:-1] if l[-1] == '\n' else l

def remove_last_empty(l: List[str], empty: str | None = None) -> List[str]:
    if empty is None:
        empty = ''
    
    return l[:-1] if len(l) > 0 and l[-1] == empty else l


##  ===================================================  parentheses  ===================================================

def parenlr(s: str, lp: str, rp: str) -> bool:
    return len(s) > 1 and s[0] == lp and s[-1] == rp

def paren(s: str, p: str) -> bool:
    return parenlr(s, p, p)

def unparenlr(s: str, lp: str, rp: str) -> str:
    return s[1:-1] if parenlr(s, lp, rp) else s

def unparen(s: str, p: str) -> str:
    return s[1:-1] if paren(s, p) else s

def unstring(s: str) -> str:
    return s[1:-1] if paren(s, '\'') or paren(s, '\"') else s


##  ===================================================  translates  ===================================================

U1 = TypeVar('U1')
U2 = TypeVar('U2')
def translate(char: U1, t: Dict[U1, U2]) -> U2:
    return t[char]

P = TypeVar('P')
def translate_to_str(s: List[P], t: Dict[P, str]) -> str:
    return ''.join(map(lambda e: translate(e, t), s))

V = TypeVar('V')
def translate_from_str(s: str, t: Dict[str, V]) -> List[V]:
    return list(map(lambda char: translate(char, t), s))

def translate_str(s: str, t: Dict[str, str]) -> str:
    return ''.join(map(lambda char: translate(char, t), s))

M1 = TypeVar('M1')
M2 = TypeVar('M2')
def translate_list(s: List[M1], t: Dict[M1, M2]) -> List[M2]:
    return list(map(lambda e: translate(e, t), s))


##  ===================================================  splits  ===================================================

T = TypeVar('T')
def first(l: List[T]) -> Tuple[T, List[T]]:
    return (l[0], l[1:])


def split(s: str, sep: str | None = None) -> List[str]:
    if sep is None:
        sep = ','

    return s.split(sep)


def substring_compare(s: str, start: int, scmp: str) -> bool:
    if start + len(scmp) > len(s):
        return False

    for (c1, c2) in zip(s, scmp):
        if c1 != c2:
            return False

    return True

def split_multi(s: str, seps: List[str]) -> List[str]:
    ss: List[str] = []

    cuti = 0
    for i in range(len(s)):
        cutl: int | None = None

        for sep in seps:
            if substring_compare(s, i, sep):
                cutl = len(sep)
                break

        if cutl is not None:
            ss.append(s[cuti:i])
            cuti += cutl

    ss.append(s[cuti:])

    return ss


##  ===================================================  basic splits  ===================================================

def splitn(s: str) -> List[str]: return split(s, '\n')
def splitnn(s: str) -> List[str]: return split(s, '\n\n')
def splitc(s: str) -> List[str]: return split(s, ',')
def splits(s: str) -> List[str]: return split(s, ' ')
def splitns(s: str) -> List[str]: return split_multi(s, [' ', '\n'])


##  ===================================================  cuts  ===================================================

def cut_n(s: str, seps: List[str]) -> List[str] | None:
    ss = []
    start = 0
    for sep in seps:
        if (end := s.find(sep, start)) == -1:
            return None
        
        ss.append(s[start:end])
        start = end + len(sep)

    ss.append(s[start:])

    return ss

def cut2(s: str, sep1: str) -> Tuple[str, str] | None:
    if (x := cut_n(s, [sep1])) is None:
        return None
    [a, b] = x
    return (a, b)

def cut3(s: str, sep1: str, sep2: str) -> Tuple[str, str, str] | None:
    if (x := cut_n(s, [sep1, sep2])) is None:
        return None
    [a, b, c] = x
    return (a, b, c)

def cut4(s: str, sep1: str, sep2: str, sep3: str) -> Tuple[str, str, str, str] | None:
    if (x := cut_n(s, [sep1, sep2, sep3])) is None:
        return None
    [a, b, c, d] = x
    return (a, b, c, d)

def cut5(s: str, sep1: str, sep2: str, sep3: str, sep4: str) -> Tuple[str, str, str, str, str] | None:
    if (x := cut_n(s, [sep1, sep2, sep3, sep4])) is None:
        return None
    [a, b, c, d, e] = x
    return (a, b, c, d, e)

def cut6(s: str, sep1: str, sep2: str, sep3: str, sep4: str, sep5: str) -> Tuple[str, str, str, str, str, str] | None:
    if (x := cut_n(s, [sep1, sep2, sep3, sep4, sep5])) is None:
        return None
    [a, b, c, d, e, f] = x
    return (a, b, c, d, e, f)


##  ===================================================  cuts without None  ===================================================

R = TypeVar('R')
def without_none(x: R | None) -> R:
    assert x is not None
    return x

def cut2u(s: str, sep1: str) -> Tuple[str, str]: return without_none(cut2(s, sep1))
def cut3u(s: str, sep1: str, sep2: str) -> Tuple[str, str, str]: return without_none(cut3(s, sep1, sep2))
def cut4u(s: str, sep1: str, sep2: str, sep3: str) -> Tuple[str, str, str, str]: return without_none(cut4(s, sep1, sep2, sep3))
def cut5u(s: str, sep1: str, sep2: str, sep3: str, sep4: str) -> Tuple[str, str, str, str, str]: return without_none(cut5(s, sep1, sep2, sep3, sep4))
def cut6u(s: str, sep1: str, sep2: str, sep3: str, sep4: str, sep5: str) -> Tuple[str, str, str, str, str, str]: return without_none(cut6(s, sep1, sep2, sep3, sep4, sep5))


##  ===================================================  map cuts  ===================================================

N1 = TypeVar('N1')
N2 = TypeVar('N2')
def cut2_map(s: str, sep: str, map_a: Callable[[str], N1], map_b: Callable[[str], N2]) -> Tuple[N1, N2] | None:
    if (cu := cut2(s, sep)) is None:
        return None
    
    (a, b) = cu
    return (map_a(a), map_b(b))

O = TypeVar('O')
def call_opt(f: Callable[[O], O] | None, o: O) -> O:
    return o if f is None else f(o)

def cut_n_map(s: str, seps: List[str], maps: List[Callable[[str], Any] | None]) -> List[Any] | None:
    ss: List[Any] = []
    start = 0
    for sep, map_ in zip(seps, maps):
        end = s.find(sep, start)
        if end == -1:
            return None

        ss.append(call_opt(map_, s[start:end]))
        start = end + len(sep)

    last_map = maps[len(seps)]
    ss.append(call_opt(last_map, s[start:]))

    return ss


##  ===================================================  numerical systems  ===================================================

NUM_DIGITS = '0123456789abcdefghijklmnopqrstuvwxyz'

def char_to_digit(c: str) -> int:
    # return NUM_DIGITS.index(c)  ## slower
    
    o = ord(c.lower())
    if o >= ord('0') and o <= ord('9'):
        return o - ord('o')
    if o >= ord('a') and o <= ord('z'):
        return o - ord('a') + 10

    return 0

def string_to_digits(s: str) -> List[int]:
    return list(map(char_to_digit, s))

def digits_to_int(base: int, digits: List[int]) -> int:
    n = 0
    for digit in digits:
        n = digit + base * n
    return n

def string_to_int(base: int, s: str) -> int:
    return digits_to_int(base, string_to_digits(s))


def digit_to_char(digit: int) -> str:
    return NUM_DIGITS[digit]

def digits_to_string(digits: List[int]) -> str:
    return ''.join(map(digit_to_char, digits))

def int_to_digits(base: int, n: int) -> List[int]:
    digits: List[int] = []
    while n > 0:
        (n, m) = divmod(n, base)
        digits.append(m)

    digits.reverse()
    return digits

def int_to_string(base: int, n: int) -> str:
    return digits_to_string(int_to_digits(base, n))


##  ===================================================  misc  ===================================================

def in_range(mi: int | None, ma: int | None, x: int) -> bool:
    return (mi is None or mi <= x) and (ma is None or x <= ma)

S1 = TypeVar('S1')
S2 = TypeVar('S2')
def lm(f: Callable[[S1], S2], i: Iterable[S1]) -> List[S2]:
    return list(map(f, i))

L1 = TypeVar('L1')
def lf(p: Callable[[L1], bool], i: Iterable[L1]) -> List[L1]:
    return list(filter(p, i))

K1 = TypeVar('K1')
def count(p: Callable[[K1], bool], i: Iterable[K1]) -> int:
    # return len(list(filter(p, i)))
    return lm(p, i).count(True)

nth = op.itemgetter


##  ===================================================  2d coords  ===================================================

Point2 = Tuple[int, int]
P2 = Point2

DIRS4 = [(0, 1), (0, -1), (1, 0), (-1, 0)]
DIRS8 = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, 1), (1, -1), (-1, -1)]


def iter_xy(ax: int, ay: int, bx: int, by: int) -> Iterator[Point2]:
    for x in range(ax, bx):
        for y in range(ay, by):
            yield (x, y)

def iter_wh(w: int, h: int) -> Iterator[Point2]:
    yield from iter_xy(0, 0, w, h)

def iter_neigh(dirs: List[Tuple[int, int]], x: int, y: int, minx: int | None, miny: int | None, maxx: int | None, maxy: int | None) -> Iterator[Point2]:
    if maxx is not None:
        maxx -= 1
    if maxy is not None:
        maxy -= 1

    for (dx, dy) in dirs:
        nx = x + dx
        ny = y + dy

        if in_range(minx, maxx, nx) and in_range(miny, maxy, ny):
            yield (nx, ny)

def iter_neigh4(x: int, y: int, minx: int | None, miny: int | None, maxx: int | None, maxy: int | None) -> Iterator[Tuple[int, int]]:
    yield from iter_neigh(DIRS4, x, y, minx, miny, maxx, maxy)

def iter_neigh8(x: int, y: int, minx: int | None, miny: int | None, maxx: int | None, maxy: int | None) -> Iterator[Tuple[int, int]]:
    yield from iter_neigh(DIRS8, x, y, minx, miny, maxx, maxy)

def iter_neigh_wh(dirs: List[Tuple[int, int]], x: int, y: int, w: int, h: int) -> Iterator[Point2]:
    yield from iter_neigh(dirs, x, y, 0, 0, w, h)

def iter_neigh_wh4(x: int, y: int, w: int, h: int) -> Iterator[Point2]:
    yield from iter_neigh(DIRS4, x, y, 0, 0, w, h)

def iter_neigh_wh8(x: int, y: int, w: int, h: int) -> Iterator[Point2]:
    yield from iter_neigh(DIRS8, x, y, 0, 0, w, h)


##  ===================================================  constants  ===================================================

APLHABET = 'abcdefghijklmnopqrstuvwxyz'
APLHABETU = lm(lambda s: s.upper(), APLHABET)
DIGITS = '0123456789'