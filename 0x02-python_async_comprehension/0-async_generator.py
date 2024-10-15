#!/usr/bin/env python3
"""Task 0: Async generator
"""
import asyncio
import random


async def async_generator():
    """This generator yields a number every
    1 second
    """
    for i in range(10):
        await asyncio.sleep(1)
        value = random.random() * 10
        yield value
