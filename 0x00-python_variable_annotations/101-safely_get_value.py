#!/usr/bin/env python3
""" 11. More involved type annotations """
from typing import Mapping, Any, Union, TypeVar
T = TypeVar('T')

dict1 = dct: Mapping
key1 = key: Any


def safely_get_value(dct1, key1, default: Union[T, None]) -> Union[Any, T]:
    """ Given the parameters and the return values, add type annotations
        to the function
    """
    if key in dct:
        return dct[key]
    else:
        return default
