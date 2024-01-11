#!/usr/bin/env python3
""" A module that annotates the function's parameters"""
from typing import Iterable, List,  Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ Returns length of list"""
    return [(i, len(i)) for i in lst]
