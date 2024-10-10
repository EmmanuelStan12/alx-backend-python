#!/usr/bin/env python3
"""
More involved type annotations
"""
from typing import TypeVar, Mapping, Any, Union, TypeAlias


T = TypeVar('T')
Def: TypeAlias = Union[T, None]
Res: TypeAlias = Union[Any, T]


def safely_get_value(dct: Mapping, key: Any, default: Def = None) -> Res:
    """
    Generics in python annotations
    """
    if key in dct:
        return dct[key]
    else:
        return default
