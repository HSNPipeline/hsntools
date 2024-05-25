"""Tests for convnwb.timestamps.utils"""

from convnwb.timestamps.utils import *

###################################################################################################
###################################################################################################

def test_convert_samples_to_time():

    fs = 1000

    n_samples = 2500
    out2_min = convert_samples_to_time(n_samples, fs, 'seconds')
    assert out2_min == 2.5

    n_samples = 90000
    out1_min = convert_samples_to_time(n_samples, fs, 'minutes')
    assert out1_min == 1.5
