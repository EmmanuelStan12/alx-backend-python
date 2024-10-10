#!/usr/bin/env python3
"""
Duck typing - first element in a sequence
"""
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Returns an iterator for the list below
    """
    if lst:
        return lst[0]
    else:
        return None
