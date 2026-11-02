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



@da.dataclass
class WInt:
    n: int = 0

    def maxxer(self, o: int) -> bool:
        # self.n += 1
        if o > self.n:
            print(o)
            self.n = o
            return True
        
        return False

@da.dataclass
class GNode:
    li: int
    ls: str
    flow: int



Graph = Tuple[List[GNode], Dict[str, GNode], List[int]]

AOCEl = Tuple[str, int, List[str]]
AOCInput = Graph
AOCResult = int



def parse_el(s: str) -> AOCEl:
    valve = s[6:8]
    ls, rs = cut2u(s, '; ')
    flow = int(cut2u(ls, '=')[1])
    single = rs[6] == ' '
    next_valves = [ rs[22:] ] if single else split(rs[23:], ', ')
    return (valve, flow, next_valves)

def parse(s: str) -> AOCInput:
    els = lm(parse_el, remove_last_empty(splitn(s)))
    nodes_count = len(els)

    nodes = [ GNode(index, valve, flow) for (index, (valve, flow, _)) in enumerate(els) ]
    str_nodes = { node.ls: node for node in nodes }
    dist_matrix: List[int] = [ -1 for _ in range(nodes_count * nodes_count) ]

    for (valve, _, next_valves) in els:
        for next_valve in next_valves:
            dist_matrix[str_nodes[valve].li * nodes_count + str_nodes[next_valve].li] = 1

    for nk in range(nodes_count):
        for nfrom in range(nodes_count):
            for nto in range(nodes_count):
                dfk = dist_matrix[nfrom * nodes_count + nk]
                dkt = dist_matrix[nk * nodes_count + nto]
                if dfk == -1 or dkt == -1:
                    continue

                dft = dist_matrix[nfrom * nodes_count + nto]
                dist_matrix[nfrom * nodes_count + nto] = dfk + dkt if dft == -1 else min(dft, dfk + dkt)

    to_remove = { index for index in range(nodes_count) if nodes[index].flow == 0 and nodes[index].ls != 'AA' }

    new_nodes: List[GNode] = []
    new_str_nodes: Dict[str, GNode] = {}
    new_dist_matrix: List[int] = []

    new_nfrom = 0
    for nfrom in range(nodes_count):
        if nfrom in to_remove:
            continue

        node = nodes[nfrom]
        new_node = GNode(new_nfrom, node.ls, node.flow)

        new_nodes.append(new_node)
        new_str_nodes[node.ls] = new_node

        new_nto = 0
        for nto in range(nodes_count):
            if nto in to_remove:
                continue

            new_dist_matrix.append(dist_matrix[nfrom * nodes_count + nto])

            new_nto += 1

        new_nfrom += 1

    return (new_nodes, new_str_nodes, new_dist_matrix)

def dfs(nodes: List[GNode], dist_matrix: List[int], max_time: int, visited: Set[int], node_index: int, time: int, s: int, max_s: WInt) -> None:
    nodes_count = len(nodes)
    node = nodes[node_index]

    if time >= max_time - 2:
        max_s.maxxer(s + node.flow if time == max_time - 2 else s)
        return

    if node.flow > 0:
        time += 1
        s += (max_time - time) * node.flow
        max_s.maxxer(s)

    if len(visited) == nodes_count - 1:
        max_s.maxxer(s)
        return

    visited.add(node_index)

    for next_node_index in range(nodes_count):
        if next_node_index in visited or nodes[next_node_index].ls == 'AA':
            continue

        d = dist_matrix[node_index * nodes_count + next_node_index]
        dfs(nodes, dist_matrix, max_time, visited, next_node_index, time + d, s, max_s)

    visited.remove(node_index)

def dfs_double(nodes: List[GNode], dist_matrix: List[int], max_time: int, visited: List[bool], node_index_a: int, node_index_b: int, time_a: int, time_b: int, s: int, max_s: WInt) -> None:
    nodes_count = len(nodes)
    node_a = nodes[node_index_a]
    node_b = nodes[node_index_b]

    if time_a == max_time - 2:
        time_a += 1
        s += node_a.flow

    if time_b == max_time - 2:
        time_b += 1
        s += node_b.flow

    done_a = time_a >= max_time - 1
    done_b = time_b >= max_time - 1

    if done_a and done_b:
        max_s.maxxer(s)
        return

    update_a = True
    if done_a:
        update_a = False
    elif not done_b:
        update_a = time_a < time_b

    node_index = node_index_a
    node = node_a
    time = time_a
    if not update_a:
        node_index = node_index_b
        node = node_b
        time = time_b

    if node.flow > 0:
        time += 1
        s += (max_time - time) * node.flow
        max_s.maxxer(s)

    if all(visited):
        if update_a:
            time_b += 1
            if time_b < max_time:
                s += (max_time - time_b) * node_b.flow
                max_s.maxxer(s)
        else:
            time_a += 1
            if time_a < max_time:
                s += (max_time - time_a) * node_a.flow
                max_s.maxxer(s)
        return

    # next_nodes = sorted((next_node_index for next_node_index in range(nodes_count) if not visited[next_node_index] and nodes[next_node_index].ls != 'AA'), key = lambda n: nodes[n].flow, reverse = True)
    # for next_node_index in next_nodes:

    for next_node_index in range(nodes_count):
        if visited[next_node_index]:
            continue

        d = dist_matrix[node_index * nodes_count + next_node_index]
        visited[next_node_index] = True
        if update_a:
            dfs_double(nodes, dist_matrix, max_time, visited, next_node_index, node_index_b, time + d, time_b, s, max_s)
        else:
            dfs_double(nodes, dist_matrix, max_time, visited, node_index_a, next_node_index, time_a, time + d, s, max_s)
        visited[next_node_index] = False


def a(inp: AOCInput) -> AOCResult:
    nodes, str_nodes, dist_matrix = inp

    s = WInt()
    dfs(nodes, dist_matrix, 30, set(), str_nodes['AA'].li, 0, 0, s)
    return s.n

def b(inp: AOCInput) -> AOCResult:
    nodes, str_nodes, dist_matrix = inp

    s = WInt()
    visited = [False for _ in range(len(nodes))]
    visited[str_nodes['AA'].li] = True
    dfs_double(nodes, dist_matrix, 26, visited, str_nodes['AA'].li, str_nodes['AA'].li, 0, 0, 0, s)
    return s.n



def main() -> None:
    import sys

    inp_file = 'inp.txt'

    args_len = len(sys.argv)
    if args_len >= 2 and sys.argv[1] == '-t':
        inp_file = 'test_inp.txt'
    elif args_len >= 3 and sys.argv[1] == '-i':
        inp_file = sys.argv[2]

    inp = parse(load_file(inp_file))
    # print(a(inp))
    print(b(inp))

if __name__ == '__main__':
    main()