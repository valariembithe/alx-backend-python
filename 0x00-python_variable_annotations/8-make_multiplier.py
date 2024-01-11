#!/usr/bin/env python3
""" A module that performs function make_multiplier"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ Returns a float"""
    return lambda x: x * multiplier
