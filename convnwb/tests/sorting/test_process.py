"""Tests for convnwb.sorting.process"""

from collections import Counter

import numpy as np

from convnwb.sorting.process import *

###################################################################################################
###################################################################################################

def test_get_sorting_kept_labels():

    # Test no valid groups
    groups0 = np.array([[0,  0], [1, -1]])
    out_cl0, out_gr0 = get_sorting_kept_labels(groups0)
    assert out_cl0.shape == out_gr0.shape
    assert out_cl0.size == 0

    # Test 1 valid group (with two classes)
    groups1 = np.array([[0,  0], [1, 1], [2, -1], [3, 1]])
    out_cl1, out_gr1 = get_sorting_kept_labels(groups1)
    assert out_cl1.shape == out_gr1.shape
    assert np.array_equal(out_cl1, np.array([1, 3]))
    assert np.array_equal(out_gr1, np.array([1, 1]))

def test_get_group_labels():

    class_labels = np.array([1, 0, 2, 3, 1, 2])
    groups = np.array([[0, 0], [1, 1], [2, -1], [3, 2]])

    group_labels = get_group_labels(class_labels, groups)
    assert len(group_labels) == len(class_labels)
    assert np.array_equal(group_labels, np.array([1, 0, -1, 2, 1, -1]))

def test_collect_all_sorting():

    n_spikes = 12
    spike_data = {
        'times' : np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]),
        'waveforms' : np.ones([n_spikes, 64]),
    }

    # Based on sort data index, set 2 spikes as bad (3 & 9), so 10 good spikes
    sort_data = {
        'index' : np.array([0, 1, 2, 4, 5, 6, 7, 8, 10, 11]),
    }

    # Test with no valid clusters
    sort_data['classes'] = np.array([0, 1, 0, 1, 0, 1, 0, 1, 0, 1])
    sort_data['groups'] =  np.array([[0, 0], [1, -1]])
    out = collect_all_sorting(spike_data, sort_data)
    for values in out.values():
        assert values.size == 0

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

def test_extract_clusters():

    n_spikes = 12
    sdata = {
        'times' : np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]),
        'waveforms' : np.ones([n_spikes, 64]),
        'clusters' : np.array([0, 1, 0, 1, 0, 2, 0, 1, 0, 2, 0, 1]),
        'classes' : np.array([1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]),
    }

    counts = Counter(sdata['clusters'])

    clusters = extract_clusters(sdata)
    assert len(clusters) == len(set(sdata['clusters']))
    for cluster in clusters:
        for label in ['times', 'classes']:
            assert len(cluster[label]) == counts[cluster['ind']]
        assert cluster['waveforms'].shape[0] == counts[cluster['ind']]
        assert np.array_equal(cluster['times'],
                              sdata['times'][sdata['clusters'] == cluster['ind']])
