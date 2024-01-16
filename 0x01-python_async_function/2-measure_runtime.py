#!/usr/bin/env python3
""" Task 2 module """
import asyncio
import time


wait_n = __import__('1-concurrent_runtime').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """ Returns a sum of wait time"""
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    return (time.time() - start_time) / n
