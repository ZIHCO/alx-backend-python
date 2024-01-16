#!/usr/bin/env python3
"""contain wait_n definition"""
import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """executes multiple couroutines at same time"""
    list_routines = ([asyncio.create_task(wait_random(max_delay))
                     for i in range(n)])
    return [await routine for routine in asyncio.as_completed(list_routines)]
