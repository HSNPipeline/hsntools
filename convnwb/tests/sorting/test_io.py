"""Tests for convnwb.sorting.io"""

from convnwb.tests.tsettings import TEST_SORTING_PATH, TEST_SORT

from convnwb.sorting.io import *

###################################################################################################
###################################################################################################

def test_load_data_chan():

    sdata = load_data_chan(0, TEST_SORTING_PATH, 'neg')
    for label in ['times', 'waveforms', 'artifacts']:
        assert label in sdata

def test_load_sort_cat():

    sdata = load_sort_cat(TEST_SORT['channel'], TEST_SORTING_PATH,
                          TEST_SORT['polarity'], TEST_SORT['user'])
    for label in ['groups', 'index', 'classes']:
        assert label in sdata
