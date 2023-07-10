#!/usr/bin/env python3
""" 4. Tasks """
import asyncio
import random
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int = 0, max_delay: int = 10) -> List[float]:
    """
    Args:
        n: number of times wait_random will be called
        max_delay: max wait time
    Return:
        list of all the delays
    """
    delays = [task_wait_random(max_delay) for _ in range(n)]
    return [await delay for delay in asyncio.as_completed(delays)]
