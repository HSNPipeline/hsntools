"""Base electrodes class."""

from copy import deepcopy

###################################################################################################
###################################################################################################

class Electrodes():
    """Object for collecting electrode information."""

    n_electrodes_per_bundle = 8

    def __init__(self):
        """Initialize Electrodes object."""

        self.bundles = []
        self.locations = []

    def __iter__(self):
        """Iterate across bundles in the object."""

        for ind in range(self.n_bundles):
            yield self.bundles[ind], self.locations[ind]

    @property
    def n_bundles(self):
        """The number of bundles stored in the object."""

        return len(self.bundles)

    def add_bundle(self, name, location):
        """Add a bundle to the object."""

        self.bundles.append(name)
        self.locations.append(location)

    def add_bundles(self, names, locations):
        """Add multiple bundles to the object."""

        for name, location in zip(names, locations):
            self.add_bundle(name, location)

    def copy(self):
        """Return a deepcopy of this object."""

        return deepcopy(self)
