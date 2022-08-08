"""Utility & helper functions for doing data conversion."""

import numpy as np

###################################################################################################
###################################################################################################

def is_empty(var):
    """Check if a variable is empty, across possible types.

    Parameters
    ----------
    var
        Variable to test for whether it's empty.

    Returns
    -------
    empty : bool
        Indicates whether the given variable is empty.
    """

    if isinstance(var, (int, float, str)):
        out = not bool(var)
    elif isinstance(var, (list, tuple)):
        out = not bool(len(var))
    elif isinstance(var, np.ndarray):
        out = not var.any()
    else:
        raise NotImplementedError('Empty check for given type not implemented.')

    return out


def incrementer(start=0, end=999):
    """Generator that returns an incrementing index value.

    Parameters
    ----------
    start, end : int
        The start and end point for the incrementer.

    Yields
    ------
    ind : int
        The current index value.
    """

    for ind in range(start, end):
        yield ind


def clean_strings(lst):
    """Helper function to clean a list of string values for adding to NWB.

    Parameters
    ----------
    lst : list
        A list of (mostly) strings to be prepped for adding to NWB.

    Returns
    -------
    list of str
        Cleaned list.

    Notes
    -----
    Each element is checked:
    - str types and made lower case and kept
    - any other type is replaced with 'none' (as a string)
    - the goal is to replace Python nan or None types for empty cells
    """

    return [val.lower() if isinstance(val, str) else 'none' for val in lst]


def get_event_time(event_times, start, end):
    """Select a (single) event based on time range, returning NaN if not found.

    Parameters
    ----------
    event_times : 1d array
        Event times.
    start, end : float
        Start and end times to select between.

    Returns
    -------
    event : float or np.nan
        The selected event time, if found, or NaN.
    """

    try:
        event = event_times[np.logical_and(event_times >= start, event_times <= end)][0]
    except IndexError:
        event = np.nan

    return event


def str_to_bool(string):
    """Convert a string to a boolean.

    Parameters
    ----------
    string : {'True', 'False'}
        String to convert to boolean.

    Returns
    -------
    bool
        Boolean represetation of the string.
    """

    assert string.lower() in ['true', 'false']
    return string.lower() == 'true'


def list_str_to_bool(lst):
    """Convert a list of strings to a list of boolean.

    Parameters
    ----------
    lst : list of str
        List of strings to convert to boolean.

    Returns
    -------
    lst of bool
        List with elements converted to boolean.
    """

    return [str_to_bool(el) for el in lst]


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
