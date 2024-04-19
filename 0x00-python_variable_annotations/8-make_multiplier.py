#!/usr/bin/env python3
'''
module: function that multiplies its input by the
given multiplier
'''
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''
    Create a multiplier function that multiplies its
    input by the given multiplier.

    Args:
    - multiplier (float): The multiplier to use in the multiplier
    function.

    Returns:
    - Callable[[float], float]: A function that multiplies its input
    by the multiplier.
    '''
    return lambda x: x * multiplier
