#!/usr/bin/env python3
"""complex types - string and int/float to tuple"""
from typing import Union


def to_kv(k: str, v: int | float) -> tuple:
    """return a tuple with arg as entries"""
    return (k, v ** 2)
