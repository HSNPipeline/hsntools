"""Base electrodes class."""

from copy import deepcopy

###################################################################################################
###################################################################################################

class ElectrodesBase(object):
    """Base object for collecting electrode information."""

    n_electrodes_per_bundle = 8

    def __init__(self):
        """Initialize ElectrodesBase object."""

        self.bundles = []
        self.locations = []

    @property
    def n_bundles(self):
        return len(self.bundles)

    def copy(self):
        """Return a deepcopy of this object."""

        return deepcopy(self)
