#!/usr/bin/env python3
'''
Annotated function that takes input list of floats
returns the sum as a float
'''
from typing import List, Union


def sum_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Calculate the sum of a list of floats and return as float.

    Args:
    - mxd_list (list[float]): List of floats to sum.

    Returns:
    - float: The sum of the input list as a float.
    """
    return float(sum(mxd_lst))
