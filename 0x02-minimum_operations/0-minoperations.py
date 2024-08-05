#!/usr/bin/python3
"""
Module that calculates the fewest number of operations needed
to result in exactly n H characters in the file.
"""


def minOperations(n):
    """
    Calculate the minimum number of operations needed to result
    in exactly n H characters in the file.
    
    Args:
        n (int): The target number of H characters.
    
    Returns:
        int: The minimum number of operations needed.
    """
    if n <= 1:
        return 0

    operations = 0
    factor = 2

    while n > 1:
        while n % factor == 0:
            operations += factor
            n //= factor
        factor += 1

    return operations
