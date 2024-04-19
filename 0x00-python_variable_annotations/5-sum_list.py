#!/usr/bin/env python3
'''
Annotated function that takes input list of floats
returns the sum as a float
'''
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Calculate the sum of a list of floats and return as float.

    Args:
    - input_list (list[float]): List of floats to sum.

    Returns:
    - float: The sum of the input list as a float.
    """
    total_sum = 0.0
    for num in input_list:
        total_sum += num

    return total_sum
