#!/usr/bin/env python3
"""contain coroutine async_comprehension"""
import asyncio
from typing import Iterator

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> Iterator[float]:
    """async comprehension"""
    return [i async for i in async_generator()]
