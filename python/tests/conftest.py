"""
Fixture for usage in pytest

Functions:
    many_intervals() -> list
    large_range_interval() -> list
"""
from random import randint
import pytest


@pytest.fixture
def many_intervals() -> list:
    """Generates a specific number of intervals"""
    intervals = []
    count = 1000000

    for _ in range(count):
        start = randint(-1000, 1000)
        end = randint(-1000, 1000)
        while start > end:
            end = randint(-1000, 1000)
        intervals.append([start, end])

    return intervals

@pytest.fixture
def large_range_interval() -> list:
    """Generates large range intervals for merging"""
    intervals = []

    for _ in range(10):
        start = randint(-1000, 1000)
        offset = randint(1000000000, 1000000000000)
        intervals.append([start, start + offset])

    return intervals
