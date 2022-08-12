"""Tests for convnwb.utils"""

import inspect
from datetime import datetime

import numpy as np

from convnwb.utils import *

###################################################################################################
###################################################################################################

def test_print_status():

    print_status(True, 'words, words, words', 1)
    print_status(False, 'words, words, words', 2)

def test_get_current_date():

    date = get_current_date()
    assert isinstance(date, datetime)

def test_convert_time_to_date():

    date = convert_time_to_date(1234567891)
    assert isinstance(date, datetime)

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

def test_convert_type():

    var = '12'
    out = convert_type(var, int)
    assert out == 12
    assert isinstance(out, int)

def test_convert_to_array():

    data = ['1', '2', '3']

    out1 = convert_to_array(data, int)
    assert isinstance(out1, np.ndarray)
    assert len(data) == len(out1)
    assert 'int' in str(out1.dtype)

    out2 = convert_to_array(data, float)
    assert 'float' in str(out2.dtype)
