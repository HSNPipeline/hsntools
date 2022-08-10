"""Tests for convnwb.timestamps"""

import numpy as np

from convnwb.timestamps import *

###################################################################################################
###################################################################################################

def test_fit_sync_alignment():

    t1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
    t2 = np.array([2, 3, 4, 5, 6, 7, 8, 9, 10])

    intercept, coef, score = fit_sync_alignment(t1, t2)
    assert isinstance(intercept, float)
    assert isinstance(coef, float)
    assert isinstance(score, float)

    model, score = fit_sync_alignment(t1, t2, return_model=True)
    assert model
    assert isinstance(score, float)

def test_predict_times():

    t1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
    t2 = np.array([2, 3, 4, 5, 6, 7, 8, 9, 10])

    intercept, coef, score = fit_sync_alignment(t1, t2)

    out = predict_times(t1, intercept, coef)
    assert np.all(out)

def test_predict_times_model():

    t1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
    t2 = np.array([2, 3, 4, 5, 6, 7, 8, 9, 10])

    model, score = fit_sync_alignment(t1, t2, return_model=True)

    out = predict_times_model(t1, model)
    assert np.all(out)

def test_match_pulses():

    # Create data as monotonically increasing random, offset copy, missing some values
    t_diff = 0.5
    sync1 = np.add.accumulate(np.abs(np.random.randn(100)))
    sync2 = sync1[15:] + t_diff
    n_pulses = 50

    sync1_out, sync2_out = match_pulses(sync1, sync2, n_pulses)
    assert isinstance(sync1_out, np.ndarray)
    assert isinstance(sync2_out, np.ndarray)
    assert len(sync1_out) == len(sync2_out) == n_pulses

    # Check that after alignment can reconstruct the time difference
    diffs = sync2_out - sync1_out
    assert np.all(np.isclose(diffs, np.ones(len(diffs)) * t_diff))

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
