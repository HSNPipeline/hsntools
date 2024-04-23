"""Tests for convnwb.sorting.io"""

from convnwb.tests.tsettings import TEST_SORTING_PATH, TEST_SORT

from convnwb.sorting.io import *

###################################################################################################
###################################################################################################

def test_load_spike_data_file():

    sdata = load_spike_data_file(0, TEST_SORTING_PATH, 'neg')
    for label in ['times', 'waveforms', 'artifacts']:
        assert label in sdata

def test_load_sorting_data_file():

    sdata = load_sorting_data_file(TEST_SORT['channel'], TEST_SORTING_PATH,
                                   TEST_SORT['polarity'], TEST_SORT['user'])
    for label in ['groups', 'index', 'classes']:
        assert label in sdata
