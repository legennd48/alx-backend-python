#!/usr/bin/env python3
'''
1. Async Comprehensions
'''
from typing import List
from importlib import import_module as using


async_generator = using('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    '''
    Asynchronously generates and collects a list of
    10 float numbers from an asynchronous generator.

    Returns:
        List[float]: A list containing 10 float numbers
        generated asynchronously.

    This function asynchronously iterates over the
    'async_generator' from '0-async_generator' module
    to yield 10 float numbers.
    It then constructs and returns a list from these yielded numbers.
    '''
    return [num async for num in async_generator()]
