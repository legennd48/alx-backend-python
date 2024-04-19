#!/usr/bin/env python3
'''
Module contains annotated functions.
'''
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    '''
    Convert key and value to a tuple where the value is squared.

    Args:
    - k (str): The key as a string.
    - v (Union[int, float]): The value as either an int or a float.

    Returns:
    - Tuple[str, float]: A tuple containing the key and
    the square of the value as a float.
    '''
    return (k, float(v**2))
