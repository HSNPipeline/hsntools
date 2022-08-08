"""Base task class."""

from copy import deepcopy

###################################################################################################
###################################################################################################

class TaskBase(object):
    """Base object for collecting task information."""

    def __init__(self):
        """Initialize TaskBase object."""

        # Define information about the status of the task object
        self.status = {
            'time_reset' = False,
            'time_offset' = None,
        }

        # Metadata - subject / session information
        self.meta = {
            'task' : None,
            'subject' : None,
            'session' : None
        }

        # Experiment information
        self.experiment = {
            'version' : {'label' : None, 'number' : None},
            'language' : None,
        }

        # Environment information
        self.environment = {}

        # Session information
        self.session = {
            'start_time' : None,
            'end_time' : None
        }

        # Synchronization information
        self.sync = {
            # Synchronization pulses
            'neural' : {},
            'behavioral' : {},
            # Synchronization alignment
            'alignment' : {
                'intercept' : None,
                'coef' : None,
                'score' : None
            }
        }

        # Position related information
        self.position = {
            'time' : [],
            'x' : [],
            'y' : [],
            'z' : [],
            'speed' : []
        }

        # Head direction information
        self.head_direction = {
            'time' : [],
            'degrees' : [],
        }

        # Information about timing of task phases
        self.phase_times = {}

        # Stimulus information
        self.stimuli = {}

        # Trial information
        self.trial = {}

        # Response information
        self.responses = {}


    def copy(self):
        """Return a deepcopy of this object."""

        return deepcopy(self)


    def get_trial(self, index, field=None):
        """Get the information for a specified trial.

        Parameters
        ----------
        index : int
            The index of the trial to access.
        field : str, optional, default: None
            Which trial data to access.
        """

        trial_data = getattr(self, 'trial')
        if field:
            trial_data = trial_data[field]

        trial_info = dict()
        for key in trial_data.keys():
            # Collect trial info, skipping dictionaries, which are subevents
            if not isinstance(trial_data[key], dict):
                trial_info[key] = trial_data[key][index]

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
