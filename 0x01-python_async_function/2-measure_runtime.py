#!/usr/bin/env python3
""" 2. Measure the runtime """
import asyncio
import random
import time
from typing import List

wait_n = __import__('1-concurrent_coroutines').wait_n
wait_random = __import__('0-basic_async_syntax').wait_random


def measure_time(n: int = 0, max_delay: int = 10) -> float:
    """ Measure the runtime
    Args:
        n: number of times wait_random will be called
        max_delay: max wait time
    Return:
        average of all the delays
    """
    start = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    end = time.perf_counter()
    return (end - start) / n
