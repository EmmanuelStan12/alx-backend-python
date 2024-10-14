#!/usr/bin/env python3
"""task 4: Tasks part 2
"""
import asyncio
from typing import List


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Wait for n number of routines
    """
    r = await asyncio.gather(*(task_wait_random(max_delay) for _ in range(n)))
    return sorted(r)
