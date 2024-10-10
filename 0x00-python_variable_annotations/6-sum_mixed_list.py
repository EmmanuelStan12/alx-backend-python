#!/usr/bin/env python3
"""
Complex types - mixed lists
"""
from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """
    Returns the sum of mxd_list
    """
    return float(sum(mxd_list))
