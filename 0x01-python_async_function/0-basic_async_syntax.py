#!/usr/bin/env python3
"""script contain the async couroutine, wait_random"""
from random import uniform
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """returns the elapsed time used in running"""
    random_time = uniform(0, max_delay)
    await asyncio.sleep(random_time)
    return random_time
