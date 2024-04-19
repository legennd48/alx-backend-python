#!/usr/bin/env python3
'''
Module: 11. More involved type annotations
'''
from typing import Any, Mapping, Union, TypeVar


T = TypeVar('T')
Res = Union[Any, T]
Def = Union[T, None]


def safely_get_value(dct: Mapping[Any, T],
                     key: Any, default: Def = None) -> Res:
    '''
    Safely retrieve a value from a dictionary using a given key.

    Args:
    - dct (Mapping[Any, T]): The dictionary from which to retrieve the value.
    - key (Any): The key to look up in the dictionary.
    - default (Def, optional): The default value to return
    if the key is not found.
    Defaults to None.

    Returns:
    - Union[Any, T]: The value corresponding to the key if it exists,
    otherwise the default value.
    '''
    if key in dct:
        return dct[key]
    else:
        return default
