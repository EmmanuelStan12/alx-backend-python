#!/usr/bin/env python3
"""Measure the runtime
"""
import asyncio
import time


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Measures the time for async
    """
    s = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    duration = time.perf_counter() - s
    return float(duration / n)
