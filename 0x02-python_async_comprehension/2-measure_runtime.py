#!/usr/bin/env python3
"""Task 2: Runtime for parallel routines
"""
import asyncio
import time


a_comp = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Measure runtime of generator
    """
    start = time.perf_counter()
    await asyncio.gather(*[a_comp() for _ in range(4)])
    duration = time.perf_counter() - start
    return duration
