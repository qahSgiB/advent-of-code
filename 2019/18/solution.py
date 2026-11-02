from typing import List



DIRS = [
    ( 0,  1),
    ( 0, -1),
    ( 1,  0),
    (-1,  0)
]



class DfsNode:
    def __init__(self, value: str, distance: int):
        self.value = value
        self.distance = distance

        self.nexts: List['DfsNode'] = []

    def __repr__(self) -> str:
        nexts_str = ', '.join(map(repr, self.nexts))
        return f'<{self.value} | {self.distance} | {nexts_str}>'

    def pprint_rec(self, depth: int) -> None:
        print(f'{depth:2d} | '+'  '*depth+f'{self.value} {self.distance}')

        for next_ in self.nexts: next_.pprint_rec(depth+1)

    def pprint(self) -> None: self.pprint_rec(0)



def load_input(input_path: str) -> str:
    with open(input_path, 'r') as input_file: return input_file.read()


def input_to_grid(inp: str) -> List[List[str]]:
    return list(map(lambda line: list(line), inp.split('\n')))


def grid_dfs(grid: List[List[str]], x: int, y: int, visited: List[List[bool]], distance: int, dfs_node: DfsNode) -> None:
    size_x, size_y = len(grid[0]), len(grid)

    if x < 0 or x >= size_x or y < 0 or y >= size_y: return
    if visited[y][x]: return
    
    value = grid[y][x]
    visited[y][x] = True

    if value == '#': return

    if value == '.':
        for dir_x, dir_y in DIRS: grid_dfs(grid, x+dir_x, y+dir_y, visited, distance+1, dfs_node)

    else:
        new_dfs_node = DfsNode(value, distance)
        dfs_node.nexts.append(new_dfs_node)

        for dir_x, dir_y in DIRS: grid_dfs(grid, x+dir_x, y+dir_y, visited, 1, new_dfs_node)

def grid_to_dfs_node(grid: List[List[str]]) -> DfsNode:
    size_x, size_y = len(grid[0]), len(grid)

    start_x, start_y = -1, -1
    for y, line in enumerate(grid):
        for x, tile in enumerate(line):
            if tile == '@':
                start_x, start_y = x, y
                break

        if start_x != -1:
            break

    visited = [[False for _ in range(size_x)] for _ in range(size_y)]

    start_dfs_node = DfsNode('start', 0)
    grid_dfs(grid, start_x, start_y, visited, 0, start_dfs_node)

    return start_dfs_node.nexts[0]



input_ = load_input('input.txt')
test_input = load_input('test_input.txt')