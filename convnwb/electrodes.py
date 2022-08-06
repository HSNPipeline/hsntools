"""Base electrodes class."""

from copy import deepcopy

###################################################################################################
###################################################################################################

class Electrodes(object):
    """Base object for collecting electrode information."""

    n_electrodes_per_bundle = 8

    def __init__(self):
        """Initialize ElectrodesBase object."""

        self.bundles = []
        self.locations = []

    @property
    def n_bundles(self):
        """The number of bundles stored in the object."""

        return len(self.bundles)

    def add_bundle(self, name, location):
        """Add a bundle to the object."""

        self.bundles.append(name)
        self.locations.append(location)

    def copy(self):
        """Return a deepcopy of this object."""

        return deepcopy(self)
