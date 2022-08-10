"""Utility & helper functions for doing data conversion."""

from datetime import datetime
from dateutil.tz import tzlocal

import numpy as np

###################################################################################################
###################################################################################################

def print_status(verbose, message, level=1):
    """Print a status update.

    Parameters
    ----------
    verbose : bool
        Whether to print.
    message : str
        Text to print out.
    level : int
        Indentation level.
    """

    if verbose:
        print('\t' * level + message)


def get_current_date(tz=None):
    """Get the current datetime.

    Parameters
    ----------
    tz : dateutil.tz.tz, optional
        Timezone information. If not provided, defaults to the local time zone.

    Returns
    -------
    date : datetime.datetime
        The current date information.
    """

    if not tz:
        tz = tzlocal()

    date = datetime.now(tzlocal())

    return date


def convert_time_to_date(timestamp, tz=None):
    """Convert a time value to a datetime date.

    Parameters
    ----------
    timestamp : float
        Timestamp value to convert.
    tz : dateutil.tz.tz, optional
        Timezone information. If not provided, defaults to the local time zone.

    Returns
    -------
    date : datetime.datetime
        Date corresponding to the given timestamp.
    """

    if not tz:
        tz = tzlocal()

    date = datetime.fromtimestamp(timestamp, tz=tz)

    return date


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

    if var is None:
        out = True
    elif isinstance(var, (int, float, str)):
        out = not bool(var)
    elif isinstance(var, (list, tuple)):
        out = not bool(len(var))
    elif isinstance(var, np.ndarray):
        out = not var.any()
    else:
        msg = 'Empty check for given type {} not implemented.'.format(str(type(var)))
        raise NotImplementedError(msg)

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


def convert_type(variable, dtype):
    """Convert type of a given variable.

    Parameters
    ----------
    variable
        Variable to type cast.
    dtype : type
        Type to cast to.

    Returns
    -------
    out
        Typecast `value`, with type `dtype`.
    """

    out = dtype(variable)

    return out


def convert_to_array(data, dtype):
    """Convert to an array of specified data type.

    Parameters
    ----------
    data : array_like
        Data to cast to an array.
    dtype : str
        Data type to cast the array.

    Returns
    -------
    array : np.ndarray
        Data, converted to array.
    """

    array = np.array(data).astype(dtype)

    return array
