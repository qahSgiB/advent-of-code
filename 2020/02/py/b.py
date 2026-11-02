from typing import Any, Callable, Dict, List, Tuple, TypeVar

import itertools



def remove_newline(l: str) -> str:
    return l[:-1] if l[-1] == '\n' else l

def remove_last_empty(l: List[str], empty: str | None = None) -> List[str]:
    if empty is None:
        empty = ''
    
    return l[:-1] if len(l) > 0 and l[-1] == empty else l


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


def load_file(file_path: str | None = None) -> str:
    if file_path is None:
        file_path = 'inp.txt'

    with open(file_path, 'r') as file_:
        return file_.read()

def load_file_lines(file_path: str | None = None) -> List[str]:
    if file_path is None:
        file_path = 'inp.txt'

    with open(file_path, 'r') as file_:
        return remove_last_empty(list(map(remove_newline, iter(file_))))


T = TypeVar('T')
def first(l: List[T]) -> Tuple[T, List[T]]:
    return (l[0], l[1:])


def split(s: str, sep: str | None = None) -> List[str]:
    if sep is None:
        sep = ','

    return s.split(sep)

def split_two(s: str, sep: str) -> Tuple[str, str]:
    sep_pos = s.index(sep)
    return (s[:sep_pos], s[sep_pos + 1:])

N1 = TypeVar('N1')
N2 = TypeVar('N2')
def split_two_map(s: str, sep: str, map_a: Callable[[str], N1], map_b: Callable[[str], N2]) -> Tuple[N1, N2]:
    (a, b) = split_two(s, sep)
    return (map_a(a), map_b(b))

def split_n(s: str, seps: List[str]) -> List[str]:
    ss = []
    start = 0
    for sep in seps:
        end = s.index(sep, start)
        ss.append(s[start:end])
        start = end + len(sep)

    return ss

O = TypeVar('O')
def call_opt(f: Callable[[O], O] | None, o: O) -> O:
    return o if f is None else f(o)

def split_n_map(s: str, seps: List[str], maps: List[Callable[[str], Any] | None]) -> List[Any]:
    ss: List[Any] = []
    start = 0
    for sep, map_ in zip(seps, maps):
        end = s.index(sep, start)
        ss.append(call_opt(map_, s[start:end]))
        start = end + len(sep)

    last_map = maps[len(seps)]
    ss.append(call_opt(last_map, s[start:]))

    return ss


U1 = TypeVar('U1')
U2 = TypeVar('U2')
def translate(char: U1, t: Dict[U1, U2]) -> U2:
    return t[char]

V = TypeVar('V')
def translate_str(s: str, t: Dict[str, V]) -> List[V]:
    return list(map(lambda char: translate(char, t), s))

M1 = TypeVar('M1')
M2 = TypeVar('M2')
def translate_list(s: List[M1], t: Dict[M1, M2]) -> List[M2]:
    return list(map(lambda e: translate(e, t), s))



def parse_sub_el(s: str) -> Any:
    pass

def parse_el(s: str) -> Any:
    ##  ------------------------  split  ------------------------
    # s_els = split(s, ',')
    # s_els = split(s, '\n')

    ##  ------------------------  first el  ------------------------
    # f_el, s_els = first(s_els)

    # els = map(int, s_els)
    # els = map(parse_sub_el, s_els)

    return split_n_map(s, ['-', ' ', ': '], [int, int, None, None])


def map_el(el: Any) -> Any:
    [mi, ma, char, s] = el
    return (s[mi - 1] == char and s[ma - 1] != char) or (s[mi - 1] != char and s[ma - 1] == char)

def count(els: List[Any]) -> int:
    return sum(map(map_el, els))



def solve(inp_file_path: str) -> Any:
    ##  ------------------------  lines  ------------------------
    inp_els = load_file_lines()
    ##  ------------------------  groups  ------------------------
    # inp_s = load_file()
    # inp_els = split(inp_s, '\n\n')

    # inp = map(int, inp_els)
    inp = list(map(parse_el, inp_els))
    return count(inp)



if __name__ == '__main__':
    print(solve('inp.txt'))