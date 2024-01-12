#!/usr/bin/env python3
"""script contains sum_mixed_list function"""
from typing import List, Union


def sum_mixed_list(mxed_lst: List[Union[int, float]]) -> float:
    """arg is a mix of integer and float"""
    sum = 0
    for entry in mxed_lst:
        sum += entry
    return sum
