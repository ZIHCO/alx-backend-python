#!/usr/bin/env python3
"""script contains sum_list"""


def sum_list(input_list: list[float]) -> float:
    """compute the sum of the list arg"""
    sum = 0
    for number in input_list:
        sum += number
    return sum
