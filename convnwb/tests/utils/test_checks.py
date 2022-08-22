"""Tests for convnwb.utils.checks"""

from convnwb.utils.checks import *

###################################################################################################
###################################################################################################

def test_is_empty():

    assert is_empty(None)
    assert is_empty('')
    assert is_empty(0)
    assert is_empty([])
    assert is_empty(np.array([]))
    assert not is_empty('abc')
    assert not is_empty(12)
    assert not is_empty([1, 2])
    assert not is_empty(np.array([1, 2]))

def test_is_type():

    assert is_type(10, None)
    assert is_type(10, int)
    assert not is_type(10, str)

def test_clean_strings():

    strs = ['word', 12, 'More words', None]

    out = clean_strings(strs)
    assert isinstance(out, list)
    for el in out:
        assert isinstance(el, str)
