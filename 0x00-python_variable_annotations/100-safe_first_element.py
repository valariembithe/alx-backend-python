#!/usr/bin/env python3
""" Task 100 """
from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Retrieves first element of sequence list if any """
    if lst:
        return lst[0]
    else:
        return None
