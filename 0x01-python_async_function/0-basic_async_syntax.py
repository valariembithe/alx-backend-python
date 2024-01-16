#!/usr/bin/env python3
""" Task 0 module"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """ Performs asyncio function """
    x = random.random() * max_delay
    await asyncio.sleep(x)
    return x
