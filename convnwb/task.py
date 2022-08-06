"""Base task class."""

from copy import deepcopy

###################################################################################################
###################################################################################################

class TaskBase(object):
    """Base object for collecting task information."""

    def __init__(self):
        """Initialize TaskBase object."""

        # Set some information for tracking the task object
        self.time_reset = False
        self.time_offset = None

        # METADATA - subject / session information
        self.meta = {
            'task' : None,
            'subject' : None,
            'session' : None
        }

        # EXPERIMENT INFORMATION
        self.experiment = {
            'version' : {'label' : None, 'number' : None},
            'language' : None,
        }

        # SESSION INFORMATION
        self.session = {
            'start' : None,
            'end' : None
        }

        ## SYNCHRONIZATION
        self.sync = {}

        ## POSITION
        self.position = {
            'time' : [],
            'x' : [],
            'y' : [],
            'z' : [],
            'speed' : []
        }

        ## TRIAL INFORMATION
        self.trial = {}


    def copy(self):
        """Return a deepcopy of this object."""

        return deepcopy(self)


    def get_trial(self, index, field='trial'):
        """Get the information for a specified trial.

        Parameters
        ----------
        index : int
            The index of the trial to access.
        field : str
            Which trial data to access.
        """

        trial_info = dict()
        for key in getattr(self, field).keys():
            trial_info[key] = getattr(self, field)[key][index]

        return trial_info


    def plot_sync_allignment(self, n_pulses=100):
        """Plots alignment of the synchronization pulses.

        Parameters
        ----------
        n_pulses : int, optional, default: 100
            Number of pulses to plot for zoomed plot.
        """

        # should be implemented in subclass
        raise NotImplementedError
