#!/usr/bin/env python3
'''
1. Let's execute multiple coroutines at the same time with async
'''
import asyncio
from typing import List


wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    '''
    runs wait_random a certain number of times
    '''
    wait_time = await asyncio.gather(
        *list(map(lambda _: wait_random(max_delay), range(n)))
    )

    return sorted(wait_time)
