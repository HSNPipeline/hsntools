"""File I/O functionality related to spike sorting / combinato files."""

from pathlib import Path

from convnwb.io import open_h5file

###################################################################################################
###################################################################################################

def load_data_chan(channel, directory, polarity='neg'):
    """Load a spike detection output file from Combinato - files with the form `data_chan_XX.h5`.

    Parameters
    ----------
    channel : int or str
        The channel number / label of the file to load.
    directory : str or Path
        The location of the path to load from.
    polarity : {'neg', 'pos'}
        Which polarity of detected spikes to load.

    Returns
    -------
    outputs : dict
        Extracted outputs from the data file.
            times: time values for each spike.
            waveforms: individual waveforms for all spikes, shape: [n_spikes, 64].
            artifacts: indicates if spike events are rejected artifact events (non-zero values)

    Notes
    -----
    This file is an output of the combinato spike detection process, including all detected
    spike events for a particular channel of data (pre-clustering).

    Has the fields 'neg', 'pos', 'thr', in which:
    - 'neg' / 'pos': negative and positive polarity, with subfield:
        - 'spikes': extracted waveforms
        - 'times': spike times (time values for the extracted waveforms)
        - 'artifacts': indicator for artifact events discarded before sorting
    - 'thr': information about the detection thresholds

    For descriptions of what each artifact means, see here:
    https://github.com/jniediek/combinato/blob/main/combinato/artifacts/mask_artifacts.py#L26

    This file contains all the putative spike events that are detected by combinato.
    Note that because this file includes event that are not sorted due to be being listed
    as artifacts, there are more spikes here than in the cluster outputs.
    The number of clustered spikes (with info in `sort_cat`) is # times - # artifacts.
    """

    outputs = {}
    with open_h5file('data_chan_' + str(channel), directory, ext='.h5') as h5file:
        outputs['times'] = h5file[polarity]['times'][:]
        outputs['waveforms'] = h5file[polarity]['spikes'][:]
        outputs['artifacts'] = h5file[polarity]['artifacts'][:]

    return outputs


def load_sort_cat(directory):
    """Load a combinato sorting output file.

    Parameters
    ----------
    directory : str
        Directory to load `sort_cat` file from.

    Returns
    -------
    outputs : dict
        Extracted outputs from the data file.
            groups: class & group assignments, shape: [n_groups, 2].
                1st col: class index / label; 2nd col: group assignment.
            index: indices corresponding to the spike times.
            classes: classes corresponding to the spike times.

    Notes
    -----
    The `index` and `classes` fields are shorter than the number of spike times (& waveforms).
    This is due to spikes that are marked as artifacts prior to the clustering process.

    Not all keys are loaded from the `sort_cat` file in this function.

    The full set of keys in a `sort_cat` includes:
        'artifacts', 'artifacts_prematch', 'classes', 'distance',
        'groups', 'groups_orig', 'index', 'matches', 'types', 'types_orig'
    """

    outputs = {}
    with open_h5file('sort_cat', directory, ext='.h5') as h5file:
        outputs['groups'] = h5file['groups'][:]
        outputs['index'] = h5file['index'][:]
        outputs['classes'] = h5file['classes'][:]

    return outputs
