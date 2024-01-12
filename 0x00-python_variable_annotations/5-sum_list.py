#!/usr/bin/env python3
"""script contains sum_list"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """compute the sum of the list arg"""
    sum = 0
    for number in input_list:
        sum += number
    return sum
