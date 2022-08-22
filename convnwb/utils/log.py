"""Utilities for logging."""

from datetime import datetime
from dateutil.tz import tzlocal

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
