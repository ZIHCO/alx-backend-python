#!/usr/bin/env python3
"""contain measure_runtime"""
import time
import asyncio

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime():
    """execute async_comprehension 4 times using asyncio.gather"""
    start_time = time.perf_counter()
    await asyncio.gather(async_comprehension(),
                         async_comprehension(),
                         async_comprehension(),
                         async_comprehension())
    return time.perf_counter() - start_time
