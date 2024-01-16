#!/usr/bin/env python3
""" Task 4 module"""
import asyncio
from typing import List


task_wait_n = __import__('3-tasks').task_wait_n


async def task_wait_random(n: int, max_delay: int) -> List[float]:
    """Returns a list of delays"""
    wait_times = await asyncio.gather(
        *tuple(map(lambda _: task_wait_random(max_delay), range(n)))
    )
    return sorted(wait_times)
