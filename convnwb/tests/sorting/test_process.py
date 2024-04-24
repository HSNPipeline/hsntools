"""Tests for convnwb.sorting.process"""

import numpy as np

from convnwb.tests.tsettings import TEST_SORTING_PATH, TEST_SORT

from convnwb.sorting.process import *

###################################################################################################
###################################################################################################

def test_collect_all_sorting():

    n_spikes = 12
    spike_data = {
        'channel' : 0,
        'polarity' : 'neg',
        'times' : np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]),
        'waveforms' : np.ones([n_spikes, 64]),
    }

    # Based on sort data index, set 2 spikes as bad (3 & 9), so 10 good spikes
    sort_data = {
        'channel' : 0,
        'polarity' : 'neg',
        'index' : np.array([0, 1, 2, 4, 5, 6, 7, 8, 10, 11]),
    }

    # Test with no valid clusters
    sort_data['classes'] = np.array([0, 1, 0, 1, 0, 1, 0, 1, 0, 1])
    sort_data['groups'] =  np.array([[0, 0], [1, -1]])
    out = collect_all_sorting(spike_data, sort_data)
    for label in ['classes', 'times']:
        assert out[label].size == 0

    # Test with 1 valid cluster
    sort_data['classes'] = np.array([0, 1, 2, 0, 1, 2, 0, 1, 2, 0])
    sort_data['groups'] = np.array([[0, 0], [1, -1], [2, 1]])
    out = collect_all_sorting(spike_data, sort_data)
    assert set(out['clusters']) == {1}
    assert np.array_equal(out['classes'], np.array([2, 2, 2]))
    assert np.array_equal(out['times'], np.array([2, 6, 10]))

    # Test with multiple valid clusters
    sort_data['classes'] = np.array([0, 1, 2, 3, 0, 1, 2, 3, 2, 3])
    sort_data['groups'] = np.array([[0, 0], [1, -1], [2, 1], [3, 2]])
    out = collect_all_sorting(spike_data, sort_data)
    assert set(out['clusters']) == {1, 2}
    assert np.array_equal(out['classes'], np.array([2, 3, 2, 3, 2, 3]))
    assert np.array_equal(out['times'], np.array([2, 4, 7, 8, 10, 11]))

def test_process_combinato_data():

    process_combinato_data(TEST_SORT['channel'], TEST_SORTING_PATH,
                           TEST_SORT['polarity'], TEST_SORT['user'],
                           TEST_SORTING_PATH / 'units')
