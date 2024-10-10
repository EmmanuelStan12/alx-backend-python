#!/usr/bin/env python3
"""
Complex types - functions
"""
from typing import List, Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns a function that multiplies by multiplier
    """
    return lambda x: x * multiplier
