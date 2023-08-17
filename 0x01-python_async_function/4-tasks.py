#!/usr/bin/env python3
"""
    function (do not create an async function, use the regular
    function syntax to do this) task_wait_random that takes an integer
    max_delay and returns a asyncio.Task
"""

import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    spawn task_wait_random n times with the specified max_delay.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    return [await task for task in asyncio.as_completed(tasks)]
