#!/usr/bin/env python3
"""This is basics of async
"""
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """Waits for random delay from 0 to max_delay
    """
    duration = random.random() * max_delay
    await asyncio.sleep(duration)
    return duration
