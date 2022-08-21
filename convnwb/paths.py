"""Utilities for managing a session of data."""

import os
from copy import deepcopy
from pathlib import Path

from convnwb.io import get_files
from convnwb.utils import print_status

###################################################################################################
###################################################################################################

PROJECT_FOLDERS = [
    'docs',
    'info',
    'nwb',
    'recordings',
]

SUBJECT_FOLDERS = [
    'anatomy',
    'electrodes',
    'notes',
]

SESSION_FOLDERS = {
    '01_raw' : [
        'behavior',
        'neural',
        'sync',
    ],
    '02_processing' : [
        'alignment',
        'metadata',
        'sorting',
        'task',
    ],
    '03_extracted' : [
        'spikes',
        'micro_lfp',
    ],
}


def make_folder(path):
    """Make a folder, if it does not already exist.

    Parameters
    ----------
    path : str of Path
        Path to the folder to make.
    """

    if not os.path.exists(path):
        os.mkdir(path)


def create_project_directory(base_path, project, project_folders=PROJECT_FOLDERS, verbose=True):
    """Create the folder structure for a project.

    Parameters
    ----------
    base_path : str or Path
        The path to the folder where to put the project.
    project : str
        The project name.
    project_folders : list, optional
        List of sub-folders to initialize in the project folder.
    verbose : bool, optional, default: True
        Whether to print out information.
    """

    base_path = Path(base_path)
    print_status(verbose, 'Creating project directory...', 0)
    print_status(verbose, 'Path: {}'.format(base_path / project), 1)

    make_folder(base_path / project)
    for subfolder in project_folders:
        make_folder(base_path / project / subfolder)


def create_subject_directory(project_path, subject, experiments=None,
                             subject_folders=SUBJECT_FOLDERS, recordings_name='recordings',
                             verbose=True):
    """Create the folder structure for a subject.

    Parameters
    ----------
    project_path : str or Path
        The path to the project folder.
    subject : str
        The subject code.
    experiments : str or list, optional
        Experiment name(s) to initialize in the subject folder.
    subject_folders : list, optional
        List of sub-folders to initialize in the subject folder.
    recordings_name : str, optional
        The name of the subfolder (within `project_path`) to store recordings.
    verbose : bool, optional, default: True
        Whether to print out information.
    """

    recordings_path = Path(project_path) / recordings_name

    print_status(verbose, 'Creating subject directory...', 0)
    print_status(verbose, 'Path: {}'.format(recordings_path / subject), 1)

    make_folder(recordings_path)
    make_folder(recordings_path / subject)

    all_subject_folders = deepcopy(subject_folders)
    if experiments:
        experiments = [experiments] if isinstance(experiments, str) else experiments
        all_subject_folders = all_subject_folders + experiments
    for subfolder in all_subject_folders:
        make_folder(recordings_path / subject / subfolder)


def create_session_directory(project_path, subject, experiment, session,
                             recordings_name='recordings', session_folders=SESSION_FOLDERS,
                             verbose=True):
    """Create the folder structure for a session of data.

    Parameters
    ----------
    project_path : str or Path
        The path to the project folder.
    subject : str
        The subject code.
    experiment : str
        Experiment name.
    session : str or int
        The session label to create the folder structure for.
        Can be an integer index, or a string, for example `session_0`.
    recordings_name : str, optional
        The name of the subfolder (within `project_path`) to store recordings.
    session_folders : dict, optional
        Defines the folder names to initialize as part of the session folder.
        Each key defines a sub-directory within the `session` folder.
        Each set of values is a list of folder names for within each sub-directory.
    verbose : bool, optional, default: True
        Whether to print out information.
    """

    recordings_path = Path(project_path) / recordings_name

    session = 'session_' + str(session) if 'session' not in str(session) else session

    print_status(verbose, 'Creating session directory...', 0)
    print_status(verbose, 'Path: {}'.format(recordings_path / subject / experiment / session), 1)

    create_subject_directory(project_path, subject, experiments=[experiment],
                             recordings_name=recordings_name, verbose=False)

    make_folder(recordings_path / subject / experiment / session)
    for subdir, subfolders in session_folders.items():
        make_folder(recordings_path / subject / experiment / session / subdir)
        for subfolder in subfolders:
            make_folder(recordings_path / subject / experiment / session / subdir / subfolder)


class Paths():
    """Paths object for a session of single-unit data."""

    def __init__(self, project_path, subject=None, experiment=None, session=None,
                 project_folders=PROJECT_FOLDERS, recordings_name='recordings',
                 subject_folders=SUBJECT_FOLDERS, session_folders=SESSION_FOLDERS):
        """Defines a paths object for a project.

        Parameters
        ----------
        project_path : str or Path
            The path to the project folder.
        subject : str, optional
            Subject label.
        experiment : str, optional
            Experiment name.
        session : str or int, optional
            The session label. Can be an integer index, or a string, for example `session_0`.
        project_folders : list, optional
            Defines the sub-folders that are part of the subject folder.
        recordings_name : str, optional
            The name of the subfolder (within `project_path`) to store recordings.
        subject_folders : list, optional
            Defines the sub-folders that are part of the project folder.
        session_folders : dict, optional
            Defines the folder names to that are part of the session folder.
            Each key defines a sub-directory within the `session` folder.
            Each set of values is a list of folder names within each sub-directory.
        """

        self._subject = subject
        self._experiment = experiment
        session = 'session_' + str(session) if 'session' not in str(session) else session
        self._session = session

        self._recordings_name = recordings_name
        self._session_folders = deepcopy(session_folders)
        self._subject_folders = deepcopy(subject_folders)
        self._project_folders = deepcopy(project_folders)

        self.project = Path(project_path)


    def __getattr__(self, folder):
        """Alias all the defined folder paths to access them as attributes."""

        for subdir, subfolders in self._session_folders.items():
            if folder in subdir:
                return self.session / subdir
            elif folder in subfolders:
                return self.session / subdir / folder
        for subdir in self._subject_folders:
            if folder in subdir:
                return self.subject / subdir
        for subdir in self._project_folders:
            if folder in subdir:
                return self.project / subdir
        raise ValueError('Requested path not found.')


    @property
    def recordings(self):
        return self.project / self._recordings_name


    @property
    def subject(self):
        return self.recordings / self._subject


    @property
    def experiment(self):
        return self.subject / self._experiment


    @property
    def session(self):
        return self.experiment / self._session


    def get_files(self, folder, **kwargs):
        """Get a list of files available in a specified sub-folder."""

        return get_files(getattr(self, folder), **kwargs)
