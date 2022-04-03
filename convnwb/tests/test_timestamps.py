"""Tests for convnwb.timestamps"""

import numpy as np

from convnwb.timestamps import *

###################################################################################################
###################################################################################################

def test_align_times():

    t1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
    t2 = np.array([2, 3, 4, 5, 6, 7, 8, 9, 10])

    intercept, coef, score = align_times(t1, t2)
    assert isinstance(intercept, float)
    assert isinstance(coef, float)
    assert isinstance(score, float)

    model, score = align_times(t1, t2, return_model=True)
    assert model
    assert isinstance(score, float)

def test_predict_times():

    t1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
    t2 = np.array([2, 3, 4, 5, 6, 7, 8, 9, 10])

    intercept, coef, score = align_times(t1, t2)

    out = predict_times(t1, intercept, coef)
    assert np.all(out)

def test_predict_times_model():

    t1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
    t2 = np.array([2, 3, 4, 5, 6, 7, 8, 9, 10])

    model, score = align_times(t1, t2, return_model=True)

    out = predict_times_model(t1, model)
    assert np.all(out)
