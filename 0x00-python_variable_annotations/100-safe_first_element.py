#!/usr/bin/env python3
""" 9. Let's duck type an iterable object """
from typing import Sequence, Tuple, Union, Any


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Returns the first element of a list
    """
    if lst:
        return lst[0]
    else:
        return None
