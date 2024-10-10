#!/usr/bin/env python3
"""
More involved type annotations
"""
from typing import TypeVar, Mapping, Any, Union, TypeAlias


T = TypeVar('T')
D: TypeAlias = Union[T, None]
R: TypeAlias = Union[Any, T]


def safely_get_value(dct: Mapping, key: Any, default: D = None) -> R:
    """
    Generics in python annotations
    """
    if key in dct:
        return dct[key]
    else:
        return default
