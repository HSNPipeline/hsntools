"""Tests for convnwb.utils"""

import inspect

import numpy as np

from convnwb.utils import *

###################################################################################################
###################################################################################################

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
