#!/usr/bin/env python3
"""contain wait_n definition"""
import asyncio
from typing import List


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """executes multiple couroutines at same time"""
    list_routines = [task_wait_random(max_delay) for i in range(n)]
    return [await routine for routine in asyncio.as_completed(list_routines)]
