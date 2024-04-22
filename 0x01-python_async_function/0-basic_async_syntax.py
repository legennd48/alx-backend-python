#!/usr/bin/env python3
'''
0. The basics of async
'''
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    '''
    waits for a randon number of seconds and returns the wait time
    '''
    waiting = random.random() * max_delay
    await asyncio.sleep(waiting)
    return waiting
