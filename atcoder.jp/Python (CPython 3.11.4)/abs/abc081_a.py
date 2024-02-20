def if__(cond, then, else_=lambda: None):
    if cond:
        return then()
    else:
        return else_()


def for__(iterable, body):
    for i in iterable:
        body(i)


def while__(cond_block, body):
    while cond_block():
        body()


def with__(obj, body):
    obj.__enter__()
    body(obj)
    obj.__exit__()


def discard__(obj):
    pass

def assert__(test, msg=None):
    assert test, msg

def then__(x, f):
    if x == None or x == NotImplemented:
        return x
    else:
        return f(x)
# from typing import TypeVar, Union, _SpecialForm, _type_check


class Error:
    def __init__(self, message):
        self.message = message


# T = TypeVar("T")
# @_SpecialForm
# def Result(self, parameters):
#    """Result type.
#
#    Result[T] is equivalent to Union[T, Error].
#    """
#    arg = _type_check(parameters, f"{self} requires a single type.")
#    return [arg, Error]


def is_ok(obj) -> bool:
    return not isinstance(obj, Error)



# from collections.abc import Iterable, Sequence, Iterator, Container


class Range:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __contains__(self, item):
        pass

    @staticmethod
    def from_slice(slice):
        pass

    def into_slice(self):
        pass

    def __getitem__(self, item):
        res = self.start + item
        if res in self:
            return res
        else:
            raise IndexError("Index out of range")

    # TODO: for Str, etc.
    def __len__(self):
        if self.start in self:
            if self.end in self:
                # len(1..4) == 4
                return self.end - self.start + 1
            else:
                # len(1..<4) == 3
                return self.end - self.start
        else:
            if self.end in self:
                # len(1<..4) == 3
                return self.end - self.start
            else:
                # len(1<..<4) == 2
                return self.end - self.start - 2

    def __iter__(self):
        return RangeIterator(rng=self)


# Sequence.register(Range)
# Container.register(Range)
# Iterable.register(Range)


# represents `start<..end`
class LeftOpenRange(Range):
    def __contains__(self, item):
        return self.start < item <= self.end


# represents `start..<end`
class RightOpenRange(Range):
    def __contains__(self, item):
        return self.start <= item < self.end

    @staticmethod
    def from_slice(slice):
        return Range(slice.start, slice.stop)

    def into_slice(self):
        return slice(self.start, self.end)


# represents `start<..<end`
class OpenRange(Range):
    def __contains__(self, item):
        return self.start < item < self.end


# represents `start..end`
class ClosedRange(Range):
    def __contains__(self, item):
        return self.start <= item <= self.end

    @staticmethod
    def from_slice(slice):
        return Range(slice.start, slice.stop - 1)

    def into_slice(self):
        return slice(self.start, self.end + 1)


class RangeIterator:
    def __init__(self, rng):
        self.rng = rng
        self.needle = self.rng.start
        if issubclass(Nat, type(self.rng.start)):
            if not (self.needle in self.rng):
                self.needle += 1
        elif issubclass(Str, type(self.rng.start)):
            if not (self.needle in self.rng):
                self.needle = chr(ord(self.needle) + 1)
        else:
            if not (self.needle in self.rng):
                self.needle = self.needle.succ()

    def __iter__(self):
        return self

    def __next__(self):
        if issubclass(Nat, type(self.rng.start)):
            if self.needle in self.rng:
                result = self.needle
                self.needle += 1
                return result
        elif issubclass(Str, type(self.rng.start)):
            if self.needle in self.rng:
                result = self.needle
                self.needle = chr(ord(self.needle) + 1)
                return result
        else:
            if self.needle in self.rng:
                result = self.needle
                self.needle = self.needle.succ()
                return result
        raise StopIteration


# Iterator.register(RangeIterator)
try:
    from typing import Union
except ImportError:
    import warnings
    warnings.warn("`typing.Union` is not available. Please use Python 3.8+.")
    class Union:
        pass

class UnionType:
        __origin__ = Union
        __args__: list # list[type]
        def __init__(self, *args):
            self.__args__ = args
        def __str__(self):
            s = "UnionType["
            for i, arg in enumerate(self.__args__):
                if i > 0:
                    s += ", "
                s += str(arg)
            s += "]"
            return s
        def __repr__(self):
            return self.__str__()

class FakeGenericAlias:
        __origin__: type
        __args__: list # list[type]
        def __init__(self, origin, *args):
            self.__origin__ = origin
            self.__args__ = args
try:
    from types import GenericAlias
except ImportError:
    GenericAlias = FakeGenericAlias

def is_type(x) -> bool:
    return isinstance(x, (type, FakeGenericAlias, GenericAlias, UnionType))

# The behavior of `builtins.isinstance` depends on the Python version.
def _isinstance(obj, classinfo) -> bool:
    if isinstance(classinfo, (FakeGenericAlias, GenericAlias, UnionType)):
        if classinfo.__origin__ == Union:
            return any(_isinstance(obj, t) for t in classinfo.__args__)
        else:
            return isinstance(obj, classinfo.__origin__)
    else:
        try:
            return isinstance(obj, classinfo)
        except:
            return False

class MutType:
    value: object






from collections import namedtuple

# (elem in y) == contains_operator(y, elem)
def contains_operator(y, elem) -> bool:
    if hasattr(elem, "type_check"):
        return elem.type_check(y)
    elif isinstance(y, UnionType):
        return any([contains_operator(t, elem) for t in y.__args__])
    # 1 in Int
    elif is_type(y):
        if _isinstance(elem, y):
            return True
        elif hasattr(y, "generic_try_new"):
            return is_ok(y.generic_try_new(elem, y))
        elif hasattr(y, "try_new") and is_ok(y.try_new(elem)):
            return True
        elif hasattr(y, "__origin__") and hasattr(y.__origin__, "type_check"):
            return y.__origin__.type_check(elem, y)
        # TODO: trait check
        return False
    # [1] in [Int]
    elif (
        _isinstance(y, list)
        and _isinstance(elem, list)
        and (len(y) == 0 or is_type(y[0]) or _isinstance(y[0], Range))
    ):
        type_check = all(map(lambda x: contains_operator(x[0], x[1]), zip(y, elem)))
        len_check = len(elem) <= len(y)
        return type_check and len_check
    # (1, 2) in (Int, Int)
    elif (
        _isinstance(y, tuple)
        and _isinstance(elem, tuple)
        and (len(y) == 0 or is_type(y[0]) or _isinstance(y[0], Range))
    ):
        if not hasattr(elem, "__iter__"):
            return False
        type_check = all(map(lambda x: contains_operator(x[0], x[1]), zip(y, elem)))
        len_check = len(elem) <= len(y)
        return type_check and len_check
    # {1: 2} in {Int: Int}
    elif (
        _isinstance(y, dict)
        and _isinstance(elem, dict)
        and (len(y) == 0 or is_type(next(iter(y.keys()))))
    ):
        if len(y) == 1:
            key = next(iter(y.keys()))
            key_check = all([contains_operator(key, el) for el in elem.keys()])
            value = next(iter(y.values()))
            value_check = all([contains_operator(value, el) for el in elem.values()])
            return key_check and value_check
        type_check = True # TODO:
        len_check = True  # It can be True even if either elem or y has the larger number of elems
        return type_check and len_check
    elif _isinstance(elem, list):
        
        return contains_operator(y, Array(elem))
    elif callable(elem):
        # TODO:
        return callable(y)
    else:
        return elem in y




class Int(int):
    def try_new(i):  # -> Result[Nat]
        if isinstance(i, int):
            return Int(i)
        else:
            return Error("not an integer")

    def bit_count(self):
        if hasattr(int, "bit_count"):
            return int.bit_count(self)
        else:
            return bin(self).count("1")

    def succ(self):
        return Int(self + 1)

    def pred(self):
        return Int(self - 1)

    def mutate(self):
        return IntMut(self)

    def __add__(self, other):
        return then__(int.__add__(self, other), Int)

    def __sub__(self, other):
        return then__(int.__sub__(self, other), Int)

    def __mul__(self, other):
        return then__(int.__mul__(self, other), Int)

    def __div__(self, other):
        return then__(int.__div__(self, other), Int)

    def __floordiv__(self, other):
        return then__(int.__floordiv__(self, other), Int)

    def __pow__(self, other):
        return then__(int.__pow__(self, other), Int)

    def __rpow__(self, other):
        return then__(int.__pow__(other, self), Int)

    def __pos__(self):
        return self

    def __neg__(self):
        return then__(int.__neg__(self), Int)


class IntMut(MutType):  # inherits Int
    value: Int

    def __init__(self, i):
        self.value = Int(i)

    def __int__(self):
        return self.value.__int__()

    def __float__(self):
        return self.value.__float__()

    def __repr__(self):
        return self.value.__repr__()

    def __hash__(self):
        return self.value.__hash__()

    def __eq__(self, other):
        if isinstance(other, MutType):
            return self.value == other.value
        else:
            return self.value == other

    def __ne__(self, other):
        if isinstance(other, MutType):
            return self.value != other.value
        else:
            return self.value != other

    def __le__(self, other):
        if isinstance(other, MutType):
            return self.value <= other.value
        else:
            return self.value <= other

    def __ge__(self, other):
        if isinstance(other, MutType):
            return self.value >= other.value
        else:
            return self.value >= other

    def __lt__(self, other):
        if isinstance(other, MutType):
            return self.value < other.value
        else:
            return self.value < other

    def __gt__(self, other):
        if isinstance(other, MutType):
            return self.value > other.value
        else:
            return self.value > other

    def __add__(self, other):
        if isinstance(other, MutType):
            return IntMut(self.value + other.value)
        else:
            return IntMut(self.value + other)

    def __sub__(self, other):
        if isinstance(other, MutType):
            return IntMut(self.value - other.value)
        else:
            return IntMut(self.value - other)

    def __mul__(self, other):
        if isinstance(other, MutType):
            return IntMut(self.value * other.value)
        else:
            return IntMut(self.value * other)

    def __floordiv__(self, other):
        if isinstance(other, MutType):
            return IntMut(self.value // other.value)
        else:
            return IntMut(self.value // other)

    def __truediv__(self, other):
        if isinstance(other, MutType):
            return IntMut(self.value / other.value)
        else:
            return IntMut(self.value / other)

    def __pow__(self, other):
        if isinstance(other, MutType):
            return IntMut(self.value**other.value)
        else:
            return IntMut(self.value**other)

    def __pos__(self):
        return self

    def __neg__(self):
        return IntMut(-self.value)

    def update(self, f):
        self.value = Int(f(self.value))

    def inc(self, i=1):
        self.value = Int(self.value + i)

    def dec(self, i=1):
        self.value = Int(self.value - i)

    def succ(self):
        return self.value.succ()

    def pred(self):
        return self.value.pred()


  # don't unify with the above line



class Nat(Int):
    def __init__(self, i):
        if int(i) < 0:
            raise ValueError("Nat can't be negative: {}".format(i))

    def try_new(i):  # -> Result[Nat]
        if i >= 0:
            return Nat(i)
        else:
            return Error("Nat can't be negative: {}".format(i))

    def times(self, f):
        for _ in range(self):
            f()

    def saturating_sub(self, other):
        if self > other:
            return self - other
        else:
            return 0

    def mutate(self):
        return NatMut(self)

    def __add__(self, other):
        return then__(super().__add__(other), Nat)

    def __mul__(self, other):
        return then__(super().__mul__(other), Nat)

    def __pos__(self):
        return self


class NatMut(IntMut):  # and Nat
    value: Nat

    def __init__(self, n: Nat):
        if int(n) < 0:
            raise ValueError("Nat can't be negative: {}".format(n))
        self.value = n

    def __int__(self):
        return self.value.__int__()

    def __float__(self):
        return self.value.__float__()

    def __repr__(self):
        return self.value.__repr__()

    def __hash__(self):
        return self.value.__hash__()

    def __eq__(self, other):
        if isinstance(other, MutType):
            return self.value == other.value
        else:
            return self.value == other

    def __ne__(self, other):
        if isinstance(other, MutType):
            return self.value != other.value
        else:
            return self.value != other

    def __le__(self, other):
        if isinstance(other, MutType):
            return self.value <= other.value
        else:
            return self.value <= other

    def __ge__(self, other):
        if isinstance(other, MutType):
            return self.value >= other.value
        else:
            return self.value >= other

    def __lt__(self, other):
        if isinstance(other, MutType):
            return self.value < other.value
        else:
            return self.value < other

    def __gt__(self, other):
        if isinstance(other, MutType):
            return self.value > other.value
        else:
            return self.value > other

    def __add__(self, other):
        if isinstance(other, MutType):
            return NatMut(self.value + other.value)
        else:
            return NatMut(self.value + other)

    def __radd__(self, other):
        if isinstance(other, MutType):
            return Nat(other.value + self.value)
        else:
            return Nat(other + self.value)

    def __mul__(self, other):
        if isinstance(other, MutType):
            return NatMut(self.value * other.value)
        else:
            return NatMut(self.value * other)

    def __rmul__(self, other):
        if isinstance(other, MutType):
            return Nat(other.value * self.value)
        else:
            return Nat(other * self.value)

    def __truediv__(self, other):
        if isinstance(other, MutType):
            return NatMut(self.value / other.value)
        else:
            return NatMut(self.value / other)

    def __pow__(self, other):
        if isinstance(other, MutType):
            return NatMut(self.value**other.value)
        else:
            return NatMut(self.value**other)

    def __pos__(self):
        return self

    def update(self, f):
        self.value = Nat(f(self.value))

    def try_new(i):  # -> Result[Nat]
        if i >= 0:
            return NatMut(i)
        else:
            return Error("Nat can't be negative")

    def times(self, f):
        for _ in range(self.value):
            f()





class Bool(Nat):
    def try_new(b: bool):  # -> Result[Nat]
        if b == True or b == False:
            return Bool(b)
        else:
            return Error("Bool can't be other than True or False")

    def __str__(self) -> str:
        if self:
            return "True"
        else:
            return "False"

    def __repr__(self) -> str:
        return self.__str__()

    def mutate(self):
        return BoolMut(self)

    def invert(self):
        return Bool(not self)


class BoolMut(NatMut):
    value: Bool

    def __init__(self, b: Bool):
        self.value = b

    def __repr__(self):
        return self.value.__repr__()

    def __bool__(self):
        return bool(self.value)

    def __hash__(self):
        return self.value.__hash__()

    def __eq__(self, other):
        if isinstance(other, MutType):
            return self.value == other.value
        else:
            return self.value == other

    def __ne__(self, other):
        if isinstance(other, MutType):
            return self.value != other.value
        else:
            return self.value != other

    def update(self, f):
        self.value = Bool(f(self.value))

    def invert(self):
        self.value = self.value.invert()





class Str(str):
    def __instancecheck__(cls, obj):
        return isinstance(obj, str)

    def try_new(s: str):  # -> Result[Nat]
        if isinstance(s, str):
            return Str(s)
        else:
            return Error("Str can't be other than str")

    def get(self, i: int):
        if len(self) > i:
            return Str(self[i])
        else:
            return None

    def mutate(self):
        return StrMut(self)

    def to_int(self):
        return Int(self) if self.isdigit() else None

    def contains(self, s):
        return s in self

    def __add__(self, other):
        return then__(str.__add__(self, other), Str)

    def __mul__(self, other):
        return then__(str.__mul__(self, other), Str)

    def __mod__(self, other):
        return then__(str.__mod__(other, self), Str)

    def __getitem__(self, index_or_slice):
        
        if isinstance(index_or_slice, slice):
            return Str(str.__getitem__(self, index_or_slice))
        elif isinstance(index_or_slice, Range):
            return Str(str.__getitem__(self, index_or_slice.into_slice()))
        else:
            return str.__getitem__(self, index_or_slice)


class StrMut(MutType):  # Inherits Str
    value: Str

    def __init__(self, s: str):
        self.value = s

    def __repr__(self):
        return self.value.__repr__()

    def __str__(self):
        return self.value.__str__()

    def __hash__(self):
        return self.value.__hash__()

    def __eq__(self, other):
        if isinstance(other, MutType):
            return self.value == other.value
        else:
            return self.value == other

    def __ne__(self, other):
        if isinstance(other, MutType):
            return self.value != other.value
        else:
            return self.value != other

    def update(self, f):
        self.value = Str(f(self.value))

    def try_new(s: str):
        if isinstance(s, str):
            self = StrMut()
            self.value = s
            return self
        else:
            return Error("Str! can't be other than str")

    def clear(self):
        self.value = ""

    def pop(self):
        if len(self.value) > 0:
            last = self.value[-1]
            self.value = self.value[:-1]
            return last
        else:
            return Error("Can't pop from empty `Str!`")

    def push(self, s: str):
        self.value += s

    def remove(self, idx: int):
        char = self.value[idx]
        self.value = self.value[:idx] + self.value[idx + 1 :]
        return char

    def insert(self, idx: int, s: str):
        self.value = self.value[:idx] + s + self.value[idx:]




class Float(float):
    EPSILON = 2.220446049250313e-16

    def try_new(i):  # -> Result[Nat]
        if isinstance(i, float):
            return Float(i)
        else:
            return Error("not a float")

    def mutate(self):
        return FloatMut(self)

    def __abs__(self):
        return Float(float.__abs__(self))

    def __add__(self, other):
        return then__(float.__add__(self, other), Float)

    def __sub__(self, other):
        return then__(float.__sub__(self, other), Float)

    def __mul__(self, other):
        return then__(float.__mul__(self, other), Float)

    def __div__(self, other):
        return then__(float.__div__(self, other), Float)

    def __floordiv__(self, other):
        return then__(float.__floordiv__(self, other), Float)

    def __truediv__(self, other):
        return then__(float.__truediv__(self, other), Float)

    def __pow__(self, other):
        return then__(float.__pow__(self, other), Float)

    def __rpow__(self, other):
        return then__(float.__pow__(float(other), self), Float)

    def __pos__(self):
        return self

    def __neg__(self):
        return then__(float.__neg__(self), Float)

    def nearly_eq(self, other, epsilon=EPSILON):
        return abs(self - other) < epsilon

class FloatMut(MutType):  # inherits Float
    value: Float

    EPSILON = 2.220446049250313e-16

    def __init__(self, i):
        self.value = Float(i)

    def __repr__(self):
        return self.value.__repr__()

    def __hash__(self):
        return self.value.__hash__()

    def __deref__(self):
        return self.value

    def __float__(self):
        return self.value.__float__()

    def __eq__(self, other):
        if isinstance(other, MutType):
            return self.value == other.value
        else:
            return self.value == other

    def __ne__(self, other):
        if isinstance(other, MutType):
            return self.value != other.value
        else:
            return self.value != other

    def __le__(self, other):
        if isinstance(other, MutType):
            return self.value <= other.value
        else:
            return self.value <= other

    def __ge__(self, other):
        if isinstance(other, MutType):
            return self.value >= other.value
        else:
            return self.value >= other

    def __lt__(self, other):
        if isinstance(other, MutType):
            return self.value < other.value
        else:
            return self.value < other

    def __gt__(self, other):
        if isinstance(other, MutType):
            return self.value > other.value
        else:
            return self.value > other

    def __add__(self, other):
        if isinstance(other, MutType):
            return FloatMut(self.value + other.value)
        else:
            return FloatMut(self.value + other)

    def __sub__(self, other):
        if isinstance(other, MutType):
            return FloatMut(self.value - other.value)
        else:
            return FloatMut(self.value - other)

    def __mul__(self, other):
        if isinstance(other, MutType):
            return FloatMut(self.value * other.value)
        else:
            return FloatMut(self.value * other)

    def __floordiv__(self, other):
        if isinstance(other, MutType):
            return FloatMut(self.value // other.value)
        else:
            return FloatMut(self.value // other)

    def __truediv__(self, other):
        if isinstance(other, MutType):
            return FloatMut(self.value / other.value)
        else:
            return FloatMut(self.value / other)

    def __pow__(self, other):
        if isinstance(other, MutType):
            return FloatMut(self.value**other.value)
        else:
            return FloatMut(self.value**other)

    def __pos__(self):
        return self

    def __neg__(self):
        return FloatMut(-self.value)

    def update(self, f):
        self.value = Float(f(self.value))

    def inc(self, value=1.0):
        self.value = Float(self.value + value)

    def dec(self, value=1.0):
        self.value = Float(self.value - value)









class Array(list):
    @staticmethod
    def try_new(arr):  # -> Result[Array]
        if isinstance(arr, list):
            return Array(arr)
        else:
            return Error("not a list")

    def generic_try_new(arr, cls = None):  # -> Result[Array]
        if cls is None:
            return Array.try_new(arr)
        else:
            elem_t = cls.__args__[0]
            elems = []
            for elem in arr:
                if not hasattr(elem_t, "try_new"):
                    return Error("not a " + str(elem_t))
                # TODO: nested check
                elem = elem_t.try_new(elem)
                if is_ok(elem):
                    elems.append(elem)
                else:
                    return Error("not a " + str(elem_t))
            return Array(elems)

    def dedup(self, same_bucket=None):
        if same_bucket is None:
            return Array(list(set(self)))
        else:
            removes = []
            for lhs, rhs in zip(self, self[1:]):
                if same_bucket(lhs, rhs):
                    removes.append(lhs)
            for remove in removes:
                self.remove(remove)
            return self

    def get(self, index, default=None):
        try:
            return self[index]
        except IndexError:
            return default

    def push(self, value):
        self.append(value)
        return self

    def partition(self, f):
        return Array(list(filter(f, self))), Array(
            list(filter(lambda x: not f(x), self))
        )

    def __mul__(self, n):
        return then__(list.__mul__(self, n), Array)

    def __getitem__(self, index_or_slice):
        if isinstance(index_or_slice, slice):
            return Array(list.__getitem__(self, index_or_slice))
        elif isinstance(index_or_slice, NatMut) or isinstance(index_or_slice, IntMut):
            return list.__getitem__(self, int(index_or_slice))
        elif isinstance(index_or_slice, Range):
            return Array(list.__getitem__(self, index_or_slice.into_slice()))
        else:
            return list.__getitem__(self, index_or_slice)

    def __hash__(self):
        return hash(tuple(self))

    def update(self, f):
        self = Array(f(self))

    def type_check(self, t: type) -> bool:
        if isinstance(t, list):
            if len(t) < len(self):
                return False
            for (inner_t, elem) in zip(t, self):
                if not contains_operator(inner_t, elem):
                    return False
            return True
        elif isinstance(t, set):
            return self in t
        elif isinstance(t, UnionType):
            return any([self.type_check(_t) for _t in t.__args__])
        elif not hasattr(t, "__args__"):
            return isinstance(self, t)
        elem_t = t.__args__[0]
        l = None if len(t.__args__) != 2 else t.__args__[1]
        if l is not None and l != len(self):
            return False
        for elem in self:
            if not contains_operator(elem_t, elem):
                return False
        return True

    def update_nth(self, index, f):
        self[index] = f(self[index])

    def sum(self, start=0):
        return sum(self, start)

    def prod(self, start=1):
        from functools import reduce
        return reduce(lambda x, y: x * y, self, start)

    def reversed(self):
        return Array(list.__reversed__(self))

    def insert_at(self, index, value):
        self.insert(index, value)
        return self

    def remove_at(self, index):
        del self[index]
        return self

    def remove_all(self, item):
        while item in self:
            self.remove(item)
        return self

    def repeat(self, n):
        from copy import deepcopy
        new = []
        for _ in range(n):
            new.extend(deepcopy(self))
        return Array(new)

class UnsizedArray:
    elem: object
    def __init__(self, elem):
        self.elem = elem
s_L1 = (input)()
(print)((s_L1).count(Str("1"),),)
