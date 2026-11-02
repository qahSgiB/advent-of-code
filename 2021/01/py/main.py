import itertools



def a(inp_file_path: str) -> int:
    with open(inp_file_path, 'r') as inp_file:
        depths = list(map(int, inp_file))

    count = 0
    for i in range(1, len(depths)):
        if depths[i - 1] < depths[i]:
            count += 1

    return count

def a1(inp_file_path: str) -> int:
    with open(inp_file_path, 'r') as inp_file:
        depths = list(map(int, inp_file))

    iter_b = iter(depths)
    next(iter_b)
    return sum(1 for a, b in zip(depths, iter_b) if a < b)

def a2(inp_file_path: str) -> int:
    with open(inp_file_path, 'r') as inp_file:
        depths = list(map(int, inp_file))
    
    return sum(1 for i in range(1, len(depths)) if depths[i - 1] < depths[i])

def a3(inp_file_path: str) -> int:
    with open(inp_file_path, 'r') as inp_file:
        depths = list(map(int, inp_file))

    return sum(1 for a, b in itertools.pairwise(depths) if a < b)

def a4(inp_file_path: str) -> int:
    return sum(1 for a, b in itertools.pairwise(map(int, open(inp_file_path, 'r'))) if a < b)


def b(inp_file_path: str) -> int:
    with open(inp_file_path, 'r') as inp_file:
        depths = list(map(int, inp_file))

    count = 0
    for i in range(len(depths) - 3):
        if depths[i] < depths[i + 3]:
            count += 1

    return count

def b1(inp_file_path: str) -> int:
    with open(inp_file_path, 'r') as inp_file:
        depths = list(map(int, inp_file))

    return sum(1 for i in range(len(depths) - 3) if depths[i] < depths[i + 3])



if __name__ == '__main__':
    print(b('inp.txt'))