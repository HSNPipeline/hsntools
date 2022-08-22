"""Functions for updating timestamps."""

import numpy as np

###################################################################################################
###################################################################################################

def offset_time(times, offset):
    """Apply an offset to timestamps.

    Parameters
    ----------
    times : 1d array
        Vector of timestamps to update.
    offset : float
        The time value to subtract from each logged time value.
    """

    return times - offset


def change_time_units(times, value, operation='divide'):
    """Change the units of timestamps.

    Parameters
    ----------
    times : 1d array
        Vector of timestamps to update.
    value : float
        Value to divide / multiply by.
    operation : {'divide', 'multiply'}
        Operation to apply.
    """

    func = {'divide' : np.divide, 'multiply' : np.multiply}[operation]
    return func(times, value)
