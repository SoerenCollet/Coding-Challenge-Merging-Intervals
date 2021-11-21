"""
Tests the merge function

Functions:
    test_merge()
"""

from merge.merge import merge


def test_merge():
    """Test if the challenge example is passed"""
    assert merge([[25,30],[2,19],[14,23],[4,8]]) == [[2,23],[25,30]]