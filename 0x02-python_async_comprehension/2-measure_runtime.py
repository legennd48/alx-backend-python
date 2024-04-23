#!/usr/bin/env python3
'''
2. Run time for four parallel comprehensions
'''
import asyncio
import time
from importlib import import_module as using


async_comprehension = using('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    '''
    Measures the total execution time for calling
    async_comprehension 4 times asynchronously.

    Returns:
        float: Total execution time in seconds.

    This function executes async_comprehension 4 times
    using asyncio.gather() to run them concurrently.
    It measures the total time taken for all
    4 calls and returns this duration.
    '''
    start_time = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    return time.time() - start_time
