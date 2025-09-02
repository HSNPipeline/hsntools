"""Utility tools & helper functions."""

from datetime import datetime
from dateutil.tz import tzlocal

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
