#!/usr/bin/env python3
"""Task 1 module"""
from typing import List
from importlib import import_module


async_generator = import_module('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Returns 10 random numbers"""
    return [x async for x in async_generator()]
