#!/usr/bin/env python3
'''
Module: 12. Type Checking
'''
from typing import List, Tuple


def zoom_array(input_tuple: Tuple[Any, ...], zoom_factor: int = 2) -> List[Any]:
    '''
    Creates multiple copies of items in a tuple based on the given zoom_factor.

    Args:
    - input_tuple (Tuple[Any, ...]): The tuple containing items to zoom.
    - zoom_factor (int, optional): The factor by which to zoom the items.
    Defaults to 2.

    Returns:
    - List[Any]: A list containing multiple copies of the
    items from the input tuple.
    '''
    zoomed_list: List[Any] = [
        item for item in input_tuple
        for _ in range(zoom_factor)
    ]
    return zoomed_list


initial_tuple = (12, 72, 91)

zoomed_2x_list = zoom_array(initial_tuple)

zoomed_3x_list = zoom_array(initial_tuple, 3)
