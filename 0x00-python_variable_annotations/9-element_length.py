#!/usr/bin/env python3
'''
Module 9. Let's duck type an iterable object
'''
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''
    Compute the length of each sequence in an iterable and
    return as a list of tuples.

    Args:
    - lst (Iterable[Sequence]): An iterable containing sequences.

    Returns:
    - List[Tuple[Sequence, int]]: A list of tuples where
    each tuple contains a sequence and its corresponding length.
    '''
    return [(i, len(i)) for i in lst]
