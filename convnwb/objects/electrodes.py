"""Base electrodes class."""

from copy import deepcopy

from convnwb.modutils.dependencies import safe_import, check_dependency

pd = safe_import('pandas')

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


    def data_keys(self, skip=None):
        """Get a list of data keys defined in the electrodes object.

        Parameters
        ----------
        skip : str or list of str
            Name(s) of any data attributes to skip.

        Returns
        -------
        data_keys : list of str
            List of data attributes available in the object.
        """

        data_keys = list(vars(self).keys())

        if skip:
            for skip_item in [skip] if isinstance(skip, str) else skip:
                data_keys.remove(skip_item)

        return data_keys


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


    def to_dict(self):
        """Convert object data to a dictionary."""

        out_dict = {}
        for key in self.data_keys():
            out_dict[key] = getattr(self, key)

        return out_dict


    @check_dependency(pd, 'pandas')
    def to_dataframe(self):
        """Return object data as a dataframe."""

        return pd.DataFrame(self.to_dict())
