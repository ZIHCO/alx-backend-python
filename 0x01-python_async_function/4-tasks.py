#!/usr/bin/env python3
"""This script returns a random generated sorted list
using concurrency"""
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """return sorted list using asyncio"""
    routines = [task_wait_random(max_delay)
                for _ in range(n)]
    return [await routine
            for routine in asyncio.as_completed(routines)]
