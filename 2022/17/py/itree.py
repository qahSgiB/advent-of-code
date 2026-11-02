from typing import Optional, Tuple, TypeVar, ParamSpec, Callable, Concatenate



T = TypeVar('T')
P = ParamSpec('P')


class ITreeNode:
    low: int
    hight: int

    left: Optional['ITreeNode']
    right: Optional['ITreeNode']

    max_depth: int

    def __init__(self, low: int, high: int) -> None:
        self.low = low
        self.high = high

        self.left = None
        self.right = None

        self.max_depth = 0

    def __str__(self) -> str:
        if self.is_node():
            return f'<{self.low}, {self.high}>'

        assert self.left is not None
        assert self.right is not None

        return f'<{self.low}, {self.high}> (L {self.left}) (R {self.right})'

    def __repr__(self) -> str:
        return str(self)

    def is_valid(self) -> bool:
        if not (self.low <= self.high):
            return False

        if not ((self.left is None) == (self.right is None)):
            return False

        if self.is_node():
            return self.max_depth == 0

        assert self.left is not None
        assert self.right is not None

        if not (self.left.high < self.high and self.left.low == self.low):
            return False
        if not (self.right.low > self.low and self.right.high == self.high):
            return False

        if not (self.left.is_valid() and self.right.is_valid()):
            return False

        if not self.max_depth == max(self.left.max_depth, self.right.max_depth) + 1:
            print(self)
            print(f'{self.max_depth} {self.left.max_depth} {self.right.max_depth}')

        return self.max_depth == max(self.left.max_depth, self.right.max_depth) + 1

    @staticmethod
    def after_check_valid(f: Callable[Concatenate['ITreeNode', P], T]) -> Callable[Concatenate['ITreeNode', P], T]:
        def wrap(self: 'ITreeNode', /, *args: P.args, **kwargs: P.kwargs) -> T:
            ret = f(self, *args, **kwargs)
            assert self.is_valid()
            return ret

        return wrap

    def is_node(self) -> bool:
        return self.left is None and self.right is None

    def size(self) -> int:
        if self.is_node():
            return self.high - self.low + 1

        assert self.left is not None
        assert self.right is not None

        return self.left.size() + self.right.size()

    def __len__(self) -> int:
        return self.size()

    def contains(self, v: int) -> bool:
        if v < self.low or v > self.high:
            return False
        if self.is_node():
            return True

        assert self.left is not None
        assert self.right is not None

        return self.left.contains(v) or self.right.contains(v)

    def __contains__(self, v: int) -> bool:
        return self.contains(v)

    # @after_check_valid
    def add(self, l: int, h: int) -> None:
        if self.is_node():
            if h < self.low - 1:
                self.left = ITreeNode(l, h)
                self.right = ITreeNode(self.low, self.high)
                self.low = l
                self.max_depth = 1
            elif l > self.high + 1:
                self.left = ITreeNode(self.low, self.high)
                self.right = ITreeNode(l, h)
                self.high = h
                self.max_depth = 1
            else:
                self.low = min(self.low, l)
                self.high = max(self.high, h)
        else:
            assert self.left is not None
            assert self.right is not None

            do_left = h < self.right.low - 1
            do_right = l > self.left.high + 1

            if do_left and do_right:
                if self.left.max_depth < self.right.max_depth:
                    do_right = False
                else:
                    do_left = False

            if do_left:
                self.left.add(l, h)
                self.low = min(self.low, l)
                self.max_depth = self.left.max_depth + 1
            elif do_right:
                self.right.add(l, h)
                self.high = max(self.high, h)
                self.max_depth = self.right.max_depth + 1
            else:
                if self.left.max_depth < self.right.max_depth:
                    delete_right, nh = self.right.remove_high(h)
                    if delete_right:
                        self.hard_remove_right()
                        self.add(l, nh)
                    else:
                        self.max_depth = max(self.left.max_depth, self.right.max_depth) + 1
                        self.left.add(l, nh)
                else:
                    delete_left, nl = self.left.remove_low(l)
                    if delete_left:
                        self.hard_remove_left()
                        self.add(nl, h)
                    else:
                        self.max_depth = max(self.left.max_depth, self.right.max_depth) + 1
                        self.right.add(nl, h)

    def remove_high(self, h: int) -> Tuple[bool, int]:
        if h >= self.high:
            return (True, h)

        if self.is_node():
            return (True, self.high)

        assert self.left is not None
        assert self.right is not None

        if h < self.right.low - 1:
            left_delete, nh = self.left.remove_high(h)

            if left_delete:
                self.hard_remove_left()
                return (False, nh)
            
            self.low = self.left.low
            return (False, nh)

        right_delete, nh = self.right.remove_high(h)

        if right_delete:
            return (True,  nh)

        self.hard_remove_left()
        return (False,  nh)

    def remove_low(self, l: int) -> Tuple[bool, int]:
        if l <= self.low:
            return (True, l)

        if self.is_node():
            return (True, self.low)

        assert self.left is not None
        assert self.right is not None

        if l > self.left.high - 1:
            right_delete, nl = self.right.remove_low(l)

            if right_delete:
                self.hard_remove_right()
                return (False, nl)

            self.high = self.right.high
            return (False, nl)

        left_delete, nl = self.left.remove_low(l)

        if left_delete:
            return (True, nl)

        self.hard_remove_right()
        return (False, nl)

    def hard_remove_left(self) -> None:
        assert self.left is not None
        assert self.right is not None

        self.low = self.right.low
        self.max_depth = self.right.max_depth
        self.left = self.right.left
        self.right = self.right.right

    def hard_remove_right(self) -> None:
        assert self.left is not None
        assert self.right is not None

        self.high = self.left.high
        self.max_depth = self.left.max_depth
        self.right = self.left.right
        self.left = self.left.left


class ITree:
    root: Optional[ITreeNode]

    def __init__(self) -> None:
        self.root = None

    def __str__(self) -> str:
        return '<>' if self.root is None else str(self.root)

    def __repr__(self) -> str:
        return '<>' if self.root is None else repr(self.root)

    def is_valid(self) -> bool:
        return self.root is None or self.root.is_valid()

    def is_empty(self) -> bool:
        return self.root is None

    def size(self) -> int:
        return 0 if self.root is None else self.root.size()

    def __len__(self) -> int:
        return self.size()

    def contains(self, v: int) -> bool:
        return False if self.root is None else self.root.contains(v)

    def __contains__(self, v: int) -> bool:
        return self.contains(v)

    def add(self, low: int, high: int) -> None:
        if self.root is None:
            self.root = ITreeNode(low, high)
        else:
            self.root.add(low, high)



def test1() -> None:
    t = ITreeNode(1, 25)
    t.left = ITreeNode(1, 11)
    t.right = ITreeNode(23, 25)
    t.right.left = ITreeNode(23, 23)

def test2() -> None:
    t = ITreeNode(23, 23)
    t.add(1, 3)
    t.add(7, 11)
    t.add(25, 25)
    t.add(99, 100)
    t.add(67, 87)
    t.add(70, 104)
    assert t.is_valid()
    assert t.size() == 48
    assert not t.contains(24)
    t.add(24, 24)
    assert t.is_valid()
    assert t.size() == 49
    assert t.contains(24)
    t.add(8, 100)
    assert t.is_valid()
    t.add(4, 8)
    assert t.is_valid()
    assert t.size() == 104

def test3() -> None:
    t = ITree()
    assert str(t) == '<>'
    t.add(23, 23)
    t.add(1, 3)
    t.add(7, 11)
    t.add(25, 25)
    t.add(99, 100)
    t.add(67, 87)
    t.add(70, 104)
    assert t.is_valid()
    assert len(t) == 48
    assert 24 not in t
    t.add(24, 24)
    assert t.is_valid()
    assert len(t) == 49
    assert 24 in t
    t.add(8, 100)
    assert t.is_valid()
    t.add(4, 8)
    assert t.is_valid()
    assert len(t) == 104
    assert str(t) == '<1, 104>'


def test() -> None:
    test1()
    test2()
    test3()



if __name__ == '__main__':
    test()