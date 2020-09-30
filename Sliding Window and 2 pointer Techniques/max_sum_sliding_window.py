"""
Given an array of integer elements and an integer 'k', we are required to find the
maximum sum of 'k' consecutive elements in the array.

Instead of using a nested for loop, in a Brute force approach we will use a technique
called 'Window sliding technique' where the nested loops can be converted to a single
loop to reduce time complexity.
"""
import sys
from typing import List


def max_sum(array: List[int], k: int) -> int:
    """
    Returns the maximum sum of k consecutive elements
    >>> arr = [1, 4, 2, 10, 2, 3, 1, 0, 20]
    >>> k = 4
    >>> max_sum(arr, k)
    24
    >>> k = 10
    >>> max_sum(arr,k)
    Invalid input
    -1
    """
    if len(array) < k or k < 0:
        print("Invalid input")
        return -1
    max_sum = -sys.maxsize
    current_sum = sum(array[:k])
    for i in range(len(array) - k):
        current_sum = current_sum - array[i] + array[i + k]
        current_sum = max(max_sum, current_sum)
    return current_sum


if __name__ == "__main__":
    from random import randint
    from doctest import testmod

    testmod()
    array = [randint(-1000, 1000) for i in range(100)]
    k = randint(0, 110)
    print(f"The maximum sum of {k} consecutive elements is {max_sum(array,k)}")
