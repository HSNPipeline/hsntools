"""Tests for convnwb.sorting.utils"""

from collections import Counter

import numpy as np

from convnwb.sorting.utils import *

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

def test_extract_clusters():

    n_spikes = 12
    sdata = {
        'channel' : 0,
        'polarity' : 'neg',
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
