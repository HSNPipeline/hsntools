"""Processing functionality related to spike sorting / combinato files."""

import numpy as np

###################################################################################################
###################################################################################################

def get_sorting_kept_labels(groups):
    """Process the combinato groups info - selecting only valid class / group information.

    Parameters
    ----------
    group : 2d array
        Combinato organized array of class and group information.
        1st col: class index / label; 2nd col: group assignment.

    Returns
    -------
    valid_classes : 1d array
        An array of the class assignments that reflect valid (to-be-kept) spikes.
    valid_groups : 1d array
        An array of the group assignments that reflect valid (to-be-kept) spikes.
    """

    # Separate columns: class indices and group assignments
    class_labels, group_labels = groups.T

    # Create a mask for all valid cluster label: excludes 0 (unassigned) and -1 (artifacts)
    mask = group_labels > 0

    # Get the set of valid clusters & groups
    valid_classes = class_labels[mask]
    valid_groups = group_labels[mask]

    return valid_classes, valid_groups


def get_group_labels(class_labels, groups):
    """Get the group label for each spike (based on spike class + group mapping).

    Parameters
    ----------
    class_labels : 1d array
        Class assignment of each spike, as extracted from the sorting data.
    groups : 2d array
        Class and group assignment mapping, as extracted from the sorting data.

    Returns
    -------
    group_labels : 1d array
        Group label for each spike.
    """

    group_labels = np.zeros(len(class_labels), dtype=int)
    for ind, cval in enumerate(class_labels):
        group_labels[ind] = groups[:, 1][cval == groups[:, 0]]

    return group_labels


def collect_all_sorting(spike_data, sort_data):
    """Collect together all the organized spike sorting information for a channel of data.

    Parameters
    ----------
    spike_data : dict
        Loaded data from the spike data file.
        Should include the keys: `times`, `waveforms`.
    sort_data : dict
        Loaded sorting data from the spike sorting data file.
        Should include the keys: `index`, `classes`, `groups`.

    Returns
    -------
    outputs : dict
        Each value is an array of all values for valid events in the channel of data, including:
            `times` : spike times for each event
            `waveforms` : spike waveform for each event
            `classes` : class assignment for each event
            `clusters` : cluster (group) assignment for each event

    Notes
    -----
    Kept information is for all valid spikes - all clusters considered putative single units.

    This excludes:

    - spike events detected but excluded from sorting due to being listed as artifact
    - spike events entered into sorting, but that are unassigned to a group
    - spike events sorted into a group, but who's group was listed as an artifact
    """

    # Get the set of valid class & group labels, and make a mask
    valid_classes, valid_groups = get_sorting_kept_labels(sort_data['groups'])
    class_mask = np.isin(sort_data['classes'], valid_classes)

    # Create a vector reflecting group assignment of each spike
    group_labels = get_group_labels(sort_data['classes'], sort_data['groups'])

    outputs = {

        # spike data collected as the non-artifact spikes, sub-selected for valid classes
        'times' : spike_data['times'][sort_data['index']][class_mask],
        'waveforms' : spike_data['waveforms'][sort_data['index'][class_mask], :],

        # spike sorting information collected as the valid class labels
        'classes' : sort_data['classes'][class_mask],
        'clusters' : group_labels[class_mask],
    }

    return outputs


def extract_clusters(data):
    """Extract individual clusters from data reflecting all spikes from a channel.

    Parameters
    ----------
    data : dict
        Spike sorting information from a channel of data.
        Should include the keys: `times`, `clusters`, `waveforms`.

    Returns
    -------
    cluster_times : list of 1d array
        Spike times, separated for each cluster. List has length of n_clusters.
    cluster_waveforms : list of 2d array
        Spike waveforms, separated for each cluster. List has length of n_clusters.
    """

    clusters = []
    for cluster_ind in set(data['clusters']):
        mask = data['clusters'] == cluster_ind

        cluster_info = {}
        cluster_info['ind'] = cluster_ind
        cluster_info['times'] = data['times'][mask]
        cluster_info['waveforms'] = data['waveforms'][mask, :]
        cluster_info['classes'] = data['classes'][mask]
        clusters.append(cluster_info)

    return clusters
