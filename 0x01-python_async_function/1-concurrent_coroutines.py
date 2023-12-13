#!/usr/bin/env python3
"""This script returns a random generated sorted list
using concurrency"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """return sorted list using asyncio"""
    routines = [asyncio.create_task(wait_random(max_delay))
                for _ in range(n)]
    return [await routine
            for routine in asyncio.as_completed(routines)]
