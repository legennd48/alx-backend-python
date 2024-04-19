#!/usr/bin/env python3
'''
Module: 10. Duck typing - first element of a sequence
'''
from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    '''
    Safely retrieve the first element of a sequence if it exists.

    Args:
    - lst (Sequence[Any]): A sequence from which to retrieve the first element.

    Returns:
    - Union[Any, None]: The first element of the sequence if it exists,
    otherwise None.
    '''
    if lst:
        return lst[0]
    else:
        return None
