#!/usr/bin/env python3
""" 2. Run time for four parallel comprehensions """
import asyncio
import random
from typing import Generator, List


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ Run time for four parallel comprehensions """
    start = asyncio.get_running_loop().time()
    await asyncio.gather(*(async_comprehension() for i in range(4)))
    end = asyncio.get_running_loop().time()
    return end - start
