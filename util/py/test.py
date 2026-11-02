from typing import Any, Generic, TypeVar, Callable, Protocol

import operator as op



T1 = TypeVar('T1')
T2 = TypeVar('T2')
T3 = TypeVar('T3')
class O(Generic[T1, T2]):
    def __init__(self, func: Callable[[T1], T2]):
        self.func = func

    def __or__(self, other: T1) -> T2:
        return self.func(other)

    def __lshift__(self, other: 'O[T3, T1]') -> 'O[T3, T2]':
        if not isinstance(other, O):
            raise NotImplemented

        return O(lambda inp: self.func(other.func(inp)))

    def __rshift__(self, other: 'O[T2, T3]') -> 'O[T1, T3]':
        if not isinstance(other, O):
            raise NotImplemented

        return O(lambda inp: other.func(self.func(inp)))

T4 = TypeVar('T4')
T5 = TypeVar('T5')
T6 = TypeVar('T6')
class FutureArg(Generic[T4, T5]):
    def __init__(self, func: Callable[[T4], T5]):
        self.func = func
    
    def __add__(self, other: Any)  -> O[Any, Any]: return rbin_partial(op.add, other)
    def __radd__(self, other: Any) -> O[Any, Any]: return lbin_partial(op.add, other)
    # def __mul__(self, other: Any)  -> O[Any, Any]: return FutureArg()
    def __rmul__(self, other: Any) -> O[Any, Any]: return lbin_partial(op.mul, other)

x: FutureArg[Any, Any] = FutureArg(lambda x: x)

U1 = TypeVar('U1')
U2 = TypeVar('U2')
U3 = TypeVar('U3')
def lbin_partial(f: Callable[[U1, U2], U3], u1: U1) -> O[U2, U3]:
    return O(lambda x: f(u1, x))

V1 = TypeVar('V1')
V2 = TypeVar('V2')
V3 = TypeVar('V3')
def rbin_partial(f: Callable[[V1, V2], V3], v2: V2) -> O[V1, V3]:
    return O(lambda x: f(x, v2))

M1 = TypeVar('M1')
M2 = TypeVar('M2')
M3 = TypeVar('M3')
def lbin_partial_o(f: Callable[[M1, M2], M3]) -> Callable[[M1], O[M2, M3]]:
    return lambda x: lbin_partial(f, x)

N1 = TypeVar('N1')
N2 = TypeVar('N2')
N3 = TypeVar('N3')
def rbin_partial_o(f: Callable[[N1, N2], N3]) -> Callable[[N2], O[N1, N3]]:
    return lambda x: rbin_partial(f, x)

O1 = TypeVar('O1', contravariant=True)
O2 = TypeVar('O2', covariant=True)
class OC(Protocol, Generic[O1, O2]):
    def __call__(self, v1: O1, **params: Any) -> O2: pass
O3 = TypeVar('O3')
O4 = TypeVar('O4')
def ksbin_partial(f: OC[O3, O4], **params: Any) -> O[O3, O4]:
    return O(lambda x: f(x, **params))

P1 = TypeVar('P1')
P2 = TypeVar('P2')
class PC2(Protocol, Generic[P1, P2]):
    def __call__(self, **params: Any) -> O[P1, P2]: pass
P3 = TypeVar('P3')
P4 = TypeVar('P4')
def ksbin_partial_o(f: OC[P3, P4]) -> PC2[P3, P4]:
    return lambda **params: ksbin_partial(f, **params)

add = lbin_partial_o(op.add)
mul = lbin_partial_o(op.mul)
oint = O(int)
ointb: PC2[Any, int] = ksbin_partial_o(int)