#!/usr/bin/env python3
"""returning an asyncio task"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """return an asyncio task"""
    return asyncio.Task(wait_random(max_delay))
