"""Utility & helper functions for doing data conversion."""

import numpy as np

###################################################################################################
###################################################################################################

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
