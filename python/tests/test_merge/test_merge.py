"""
Tests the merge function

Functions:
    test_merge_arg_is_list() -> None
    test_merge_negative_intervals() -> None
    test_merge_2_values_per_interval() -> None
    test_merge_start_interval_bigger_then_end_interval() -> None
    test_merge_min_2_intervals() -> None
    test_merge_many_intervals() -> None
    test_merge_large_range_intervals() -> None
    test_merge_challenge() -> None
"""
from merge.merge import merge


def test_merge_arg_is_list():
    """Test if exception raised with intervals arg not a list"""
    assert merge("I will fail!") == "TypeError: Intervals is not a list!"

def test_merge_negative_intervals():
    """Test if negative intervals can pass"""
    assert merge([[-2,6],[-28,-8],[-9,-3]]) == [[-28,-3],[-2,6]]

def test_merge_2_values_per_interval():
    """Test if exception raised with interval values not equal 2"""
    assert merge([[10], [23]]) == "ValueError: Please provide valid intervals!" \
        "\nAn interval has exact 2 values."

def test_merge_start_interval_bigger_then_end_interval():
    """Test if exception raised with staring interval bigger then ending interval"""
    assert merge([[100,50], [500,250]]) == "ValueError: Please provide valid intervals!" \
        "\nThe starting interval should not be higher then the ending interval."

def test_merge_min_2_intervals():
    """Test if exception raised when not multiple intervals were provided"""
    assert merge([[100,50]]) == "ValueError: Please provide at least 2 intervals to merge!"

def test_merge_many_intervals(many_intervals):
    """Test if code can handle large number of intervals"""
    assert merge(many_intervals)

def test_merge_large_range_intervals(large_range_interval):
    """Test if code can handle large number of intervals"""
    assert merge(large_range_interval)

def test_merge_challenge():
    """Test if the challenge example is passed"""
    assert merge([[25,30],[2,19],[14,23],[4,8]]) == [[2,23],[25,30]]
