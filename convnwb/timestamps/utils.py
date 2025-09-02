"""Utility functions for working with samples and timestamps."""

import numpy as np

###################################################################################################
###################################################################################################

def convert_samples_to_time(n_samples, fs, output='minutes'):
    """Convert a number of samples to the corresponding length of time.

    Parameters
    ----------
    n_samples : int
        Number of samples.
    fs : int
        Sampling rate.
    output : {'minutes', 'seconds'}
        The output unit.

    Returns
    -------
    float
        Time value, in unit of `output`.
    """

    assert output in ['minutes', 'seconds'], "Output format not understood."

    n_seconds = n_samples / fs

    if output == 'minutes':
        return n_seconds / 60
    else:
        return n_seconds


def create_timestamps_from_samples(samples, fs, offset=0):
    """Create a set of timestamps for a set of samples.

    Parameters
    ----------
    samples : int or 1d array
        Number of samples to create timestamps for.
    fs : int
        Sampling rate.
    offset : float, optional
        Time value to offset time values by.

    Returns
    -------
    timestamps : 1d array
        Timestamps, in seconds.
    """

    if isinstance(samples, (np.ndarray, list)):
        n_samples = len(samples)
        offset = offset + samples[0] / fs
    else:
        n_samples = samples

    return offset + np.arange(0, n_samples / fs, 1/fs)
