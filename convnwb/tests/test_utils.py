"""Tests for convnwb.utils"""

import inspect

import numpy as np

from convnwb.utils import *

###################################################################################################
###################################################################################################

def test_is_empty():

    assert is_empty('')
    assert is_empty(0)
    assert is_empty([])
    assert is_empty(np.array([]))
    assert not is_empty('abc')
    assert not is_empty(12)
    assert not is_empty([1, 2])
    assert not is_empty(np.array([1, 2]))

def test_incrementer():

    # Test basic usage
    start, end = 0, 5
    inc = incrementer(start, end)
    assert inspect.isgenerator(inc)
    out = next(inc)
    assert isinstance(out, int)

    # Check giving specified range
    start, end = 5, 10
    inc = incrementer(start, end)
    for value in inc:
        assert isinstance(value, int)
        assert value < end

def test_clean_strings():

    strs = ['word', 12, 'More words', None]

    out = clean_strings(strs)
    assert isinstance(out, list)
    for el in out:
        assert isinstance(el, str)

def test_get_event_time():

    times = np.array([0.5, 1.25, 2.5, 3.5])

    out1 = get_event_time(times, 2, 3)
    assert out1 == 2.5

    out2 = get_event_time(times, 4, 5)
    assert np.isnan(out2)

def test_str_to_bool():

    assert str_to_bool('True')
    assert not str_to_bool('False')

def test_lst_str_to_bool():

    lst = ['False', 'True', 'False']
    assert list_str_to_bool(lst) == [False, True, False]

def test_offset_time():

    times = np.array([1., 2., 3.])
    out = offset_time(times, 1.)
    expected = np.array([0., 1., 2.])
    assert np.array_equal(out, expected)

def test_change_time_units():

    times = np.array([1., 2., 3.])

    out1 = change_time_units(times, 10, 'divide')
    expected1 = np.array([0.1, 0.2, 0.3])
    assert np.array_equal(out1, expected1)

    out2 = change_time_units(times, 10, 'multiply')
    expected2 = np.array([10., 20., 30.])
    assert np.array_equal(out2, expected2)
