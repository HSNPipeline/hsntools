"""Utility functions for working with samples and timestamps."""

###################################################################################################
###################################################################################################

def convert_samples_to_time(n_samples, fs, output='minutes'):
    """Convert a number of samples to corresponding time length.

    Parameters
    ----------
    n_samples : in
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
