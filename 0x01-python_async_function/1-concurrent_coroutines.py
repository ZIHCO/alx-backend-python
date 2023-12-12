#!/usr/bin/env python3
"""This script returns a random generated sorted list
using concurrency"""
wait_random = __import__('0-basic_async_syntax').wait_random
import asyncio


async def wait_n(n: int, max_delay: int) -> list:
    delays_list = []

    async def wait_append_delay():
        delay = await wait_random(max_delay)
        delays_list.append(delay)

    routines = [wait_append_delay() for _ in range(n)]

    await asyncio.gather(*routines)
    return delays_list
