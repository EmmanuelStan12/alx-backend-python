#!/usr/bin/env python3
"""
Complex types - string and int/float to tuple
"""
from typing import List, Union


def to_kv(k: string, v: Union[int, float]) -> Tuple[str, float]:
    """
    Returns the k and the square of v
    """
    return (k, float(v**2))
