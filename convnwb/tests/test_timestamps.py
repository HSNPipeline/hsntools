"""Tests for convnwb.timestamps"""

import numpy as np

from convnwb.timestamps import *

###################################################################################################
###################################################################################################

def test_align_times():

    t1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
    t2 = np.array([2, 3, 4, 5, 6, 7, 8, 9, 10])

    intercept, coef, score = align_times(t1, t2)

    model, score = align_times(t1, t2, return_model=True)
