#!/usr/bin/env python3
'''
Module: 12. Type Checking
'''
from typing import List, Tuple


def zoom_array(lst: Tuple[Any, ...], factor: int = 2) -> List[Any]:
    '''
    Creates multiple copies of items in a tuple based on the given factor.

    Args:
    - lst (Tuple[Any, ...]): The tuple containing items to zoom.
    - factor (int, optional): The factor by which to zoom the items.
    Defaults to 2.

    Returns:
    - List[Any]: A list containing multiple copies of the
    items from the input tuple.
    '''
    zoomed_in: List[Any] = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
