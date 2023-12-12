#!/usr/bin/env python3
"""This script is an async coroutine that randomly await
a number range."""
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """return a random number after awaiting the seconds"""
    i = random.uniform(0, max_delay)
    await asyncio.sleep(i)
    return i
