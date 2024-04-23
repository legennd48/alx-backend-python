#!/usr/bin/env python3
'''
0. Async Generator
'''
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    '''
    Asynchronously generates a sequence of 10 random float
    numbers between 0.0 and 10.0.

    Yields:
        float: A random float number between 0.0 and 10.0.

    Raises:
        None: No exceptions are raised.

    Returns:
        Generator[float, None, None]: An asynchronous
        generator yielding float values.

    This generator introduces a 1-second delay between
    each yield using asyncio.sleep(1).
    '''
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
