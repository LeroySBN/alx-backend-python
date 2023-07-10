#!/usr/bin/env python3
""" 0. The basics of async """
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """ Wait for a random delay between 0 and max_delay seconds
    Args:
        max_delay: max wait time
    Returns:
        random delay
    """
    delay = max_delay * random.random()
    await asyncio.sleep(delay)
    return delay
