#!/usr/bin/env python3
"""
Complex types - duck iterable object
"""
from typing import List, Sequence, Tuple, Iterable


def element_length(lst: Iterable[Sequence[int]]) -> List[Tuple[Sequence, int]]:
    """
    Returns an iterator for the list below
    """
    return [(i, len(i)) for i in lst]
