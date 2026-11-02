from typing import Iterable, List



def create_tuple(vars: Iterable[str]) -> str:
    return '(' + ', '.join(vars) + ')'

def create_fun_type(types: Iterable[str]) -> str:
    return ' -> '.join(types)

def create_n_vars(s: str, n: int) -> List[str]:
    return list(map(lambda x: f'{s}{x}', range(n)))


for i in range(3, 7):
    as_ = create_n_vars('a', i)
    bs = create_n_vars('b', i)
    fs = create_n_vars('f', i)

    f_tuple_type = create_tuple(map(create_fun_type, zip(as_, bs)))
    f_tuple = create_tuple(fs)
    a_tuple = create_tuple(as_)
    b_tuple = create_tuple(bs)

    res = create_tuple(f'{fs[n]} {as_[n]}' for n in range(i))

    print(f'map{i} :: {create_fun_type((f_tuple_type, a_tuple, b_tuple))}')
    print(f'map{i} {f_tuple} {a_tuple} = {res}')
    print('')