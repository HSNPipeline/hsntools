"""File I/O functionality related to spike sorting / combinato files."""

from pathlib import Path

from convnwb.io.utils import get_files
from convnwb.io import open_h5file, save_to_h5file, load_from_h5file

###################################################################################################
###################################################################################################

def load_spike_data_file(channel, folder, polarity):
    """Load a spike detection output file from Combinato - files with the form `data_chan_XX.h5`.

    Parameters
    ----------
    channel : int or str
        The channel number / label of the file to load.
    folder : str or Path
        The location of the path to load from.
    polarity : {'neg', 'pos'}
        Which polarity of detected spikes to load.

    Returns
    -------
    outputs : dict
        Extracted outputs from the data file, including:
            channel: stores the channel number / label.
            polarity: stores the polarity spikes were sorted.
            times: time values for each spike.
            waveforms: individual waveforms for all spikes, shape: [n_spikes, 64].
            artifacts: indicates if spike events are rejected artifact events (non-zero values).

    Notes
    -----
    This file is an output of the combinato spike detection process. This file includes all
    detected spike events for a particular channel of data (pre-clustering) from the
    combinato threshold detection process.

    The file has the fields 'neg', 'pos', 'thr', in which:
    - 'neg' / 'pos': reflect negative or positive polarity, each with subfields:
        - 'spikes': 2d array of extracted waveforms, as [n_spikes, 64 timepoints]
        - 'times': 1d array spike times (time values for the extracted waveforms)
        - 'artifacts': 1d array indicating artifact events that were discarded before clustering
    - 'thr': information about the detection thresholds

    In the 'artifacts' field, each 0 reflects a non-artifact (these spikes go into clustering).
    Each non-zero value reflects an artifact, with each number reflecting the artifact category.
    For descriptions of what each artifact label means, see here:
    https://github.com/jniediek/combinato/blob/main/combinato/artifacts/mask_artifacts.py#L26

    For any event listed as an artifact, these events do not enter the clustering process.
    Because of this, the total number of events in this file is greater than the number
    of events that included in subsequent clustering files. The number of clustered spikes
    (with corresponding information in `sort_cat` files) is # spike_times - # artifacts.
    """

    channel = str(channel)
    channel = 'chan_' + channel if channel[:5] != 'chan_' else channel

    outputs = {}
    with open_h5file('data_' + channel, folder, ext='.h5') as h5file:
        outputs['channel'] = channel
        outputs['polarity'] = polarity
        outputs['times'] = h5file[polarity]['times'][:]
        outputs['waveforms'] = h5file[polarity]['spikes'][:]
        outputs['artifacts'] = h5file[polarity]['artifacts'][:]

    return outputs


def load_sorting_data_file(channel, folder, polarity, user):
    """Load a combinato sorting output file - files with the file name `sort_cat.h5`.

    Parameters
    ----------
    channel : int or str
        The channel number / label of the file to load.
    folder : str or Path
        Directory to load `sort_cat` file from.
    polarity : {'neg', 'pos'}
        Which polarity of sorting results to load.
    user : str
        The 3 character user label to load.

    Returns
    -------
    outputs : dict
        Extracted outputs from the data file, including the fields:
            channel: stores the channel number / label.
            polarity: stores the polarity spikes were sorted.
            groups: class & group assignments, shape: [n_groups, 2].
                1st col: class index / label; 2nd col: group assignment.
            index: indices corresponding to the spike times.
            classes: classes corresponding to the spike times.

    Notes
    -----
    The `index` and `classes` fields are shorter than the number of spike times (& waveforms).
    This is due to spikes that are marked as artifacts prior to the clustering process.
    The 'index' field maps the index of each spike in the data files to it's label in this file.

    Not all keys are loaded from the `sort_cat` file in this function.

    The full set of keys in a `sort_cat` includes:
        'artifacts', 'artifacts_prematch', 'classes', 'distance',
        'groups', 'groups_orig', 'index', 'matches', 'types', 'types_orig'
    """

    channel = str(channel)
    channel = 'chan_' + channel if channel[:5] != 'chan_' else channel

    folder = Path(folder) / channel / 'sort_{}_{}'.format(polarity, user)

    outputs = {}
    with open_h5file('sort_cat', folder, ext='.h5') as h5file:
        outputs['channel'] = channel
        outputs['polarity'] = polarity
        outputs['groups'] = h5file['groups'][:]
        outputs['index'] = h5file['index'][:]
        outputs['classes'] = h5file['classes'][:]

    return outputs


def save_units(units, folder):
    """Save out units information.

    Parameters
    ----------
    units : list of dict
        List of dictionaries containing information for each unit.
    folder : str or Path
        Location to save files out to.
    """

    for unit in units:
        save_to_h5file(unit, 'times_ch{}_u{}'.format(unit['channel'], unit['ind']), folder)


def load_units(folder):
    """Load a set of units files from a folder.

    Parameters
    ----------
    folder : str or Path
        Location to load files from.
        Will load all files in this folder with 'times' in the name.

    Returns
    -------
    units : list of dict
        List of dictionaries containing the loaded information for each unit.
    """

    fields = ['ind', 'channel', 'polarity', 'times', 'waveforms', 'classes']

    units = []
    unit_files = get_files(folder, select='times')
    for unit_file in unit_files:
        units.append(load_from_h5file(fields, unit_file, folder))

    return units
