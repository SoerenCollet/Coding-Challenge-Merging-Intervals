"""
Tests the merge function

Functions:
    test_merge()
"""
from merge.merge import merge


def test_merge_arg_is_list():
    """Test if exception raised with intervals arg not a list"""
    merge("I will fail!")

def test_merge_challenge():
    """Test if the challenge example is passed"""
    assert merge([[25,30],[2,19],[14,23],[4,8]]) == [[2,23],[25,30]]
