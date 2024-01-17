#!/usr/bin/env python3
"""contains coroutine async_generator"""
import random
import asyncio
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """loops 10 time, each time waits a second
    then yield a random number"""
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
