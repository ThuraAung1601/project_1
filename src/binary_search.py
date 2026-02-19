"""Binary search implementation."""

from typing import Sequence, TypeVar

T = TypeVar("T")


def binary_search(sorted_values: Sequence[T], target: T) -> int:
    """Return the index of target inside sorted_values, or -1 if missing."""
    left, right = 0, len(sorted_values) - 1
    while left <= right:
        mid = left + (right - left) // 2
        mid_value = sorted_values[mid]
        if mid_value == target:
            return mid
        if mid_value < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1