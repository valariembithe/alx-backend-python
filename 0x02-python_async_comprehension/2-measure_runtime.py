#!/usr/bin/env python3
""" Task 2 module"""
import asyncio
import time
from importlib import import_module


async_comprehension = import_module('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Returns total execution time"""
    start_time = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    return time.time - start_time
