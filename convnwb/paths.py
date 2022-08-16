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
    'metadata',
    'nwb',
    'recordings',
]

SUBJECT_FOLDERS = [
    'anat',
    'info',
]

SESSION_FOLDERS = {
    '01_raw' : [
        'behavior',
        'neural',
        'sync',
    ],
    '02_processing' : [
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


def create_subject_directory(subject, project_path, recordings_subdir='recordings',
                             task_list=None, subject_folders=SUBJECT_FOLDERS, verbose=True):
    """Create the folder structure for a subject.

    Parameters
    ----------
    subject : str
        The subject code.
    project_path : str or Path
        The path to the project folder.
    recordings_subdir : str
        The name of the subfolder (within `project_path`) to store recordings.
    task_list : list, optional
        List of task names to initialize in the subject folder.
    subject_folders : list, optional
        List of sub-folders to initialize in the subject folder.
    verbose : bool, optional, default: True
        Whether to print out information.
    """

    recordings_path = Path(project_path / recordings_subdir)

    print_status(verbose, 'Creating subject directory...', 0)
    print_status(verbose, 'Path: {}'.format(recordings_path / subject), 1)

    make_folder(recordings_path)
    make_folder(recordings_path / subject)

    all_subject_folders = subject_folders + [] if not task_list else task_list
    for subfolder in all_subject_folders:
        make_folder(recordings_path / subject / subfolder)


def create_session_directory(subject, task, session, project_path,
                             recordings_subdir='recordings', session_folders=SESSION_FOLDERS,
                             verbose=True):
    """Create the folder structure for a session of data.

    Parameters
    ----------
    subject : str
        The subject code.
    task : str
        The task name.
    session : str
        The session label to create the folder structure for.
    project_path : str or Path
        The path to the project folder.
    recordings_subdir : str
        The name of the subfolder (within `project_path`) to store recordings.
    session_folders : dict, optional
        Defines the folder names to define as part of the session folder.
        Each key defines a sub-directory within the `session` folder.
        Each set of values if a list of folder names for within each sub-directory.
    verbose : bool, optional, default: True
        Whether to print out information.
    """

    recordings_path = Path(project_path / recordings_subdir)

    print_status(verbose, 'Creating session directory...', 0)
    print_status(verbose, 'Path: {}'.format(recordings_path / subject / task / session), 1)

    make_folder(recordings_path)
    make_folder(recordings_path / subject)
    make_folder(recordings_path / subject / task)
    make_folder(recordings_path / subject / task / session)

    for subdir, subfolders in session_folders.items():
        make_folder(recordings_path / subject / task / session / subdir)
        for subfolder in subfolders:
            make_folder(recordings_path / subject / task / session / subdir / subfolder)


class Paths():
    """Paths object for a session of single-unit data."""

    def __init__(self, subject, task, session, project_path,
                 recordings_subdir='recordings', session_folders=SESSION_FOLDERS):
        """Defines a paths object for a human single unit data.

        Parameters
        ----------
        subject : str
            Subject label.
        task : str
            Task name.
        session : str
            Session label.
        project_path : str or Path
            The path to the project folder.
        recordings_subdir : str
            The name of the subfolder (within `project_path`) to store recordings.
        session_folders : dict, optional
            Defines the folder names to define as part of the session folder.
            Each key defines a sub-directory within the `session` folder.
            Each set of values if a list of folder names for within each sub-directory.
        """

        self._subject = subject
        self._task = task
        self._session = session

        self._recordings_subdir = recordings_subdir
        self._session_folders = deepcopy(session_folders)

        self.project = Path(project_path)


    def __getattr__(self, folder):
        """Alias all the defined folder paths to access them as attributes."""

        for subdir, subfolders in self._session_folders.items():
            if folder in subdir:
                return self.session / subdir
            elif folder in subfolders:
                return self.session / subdir / folder
        raise ValueError('Requested path not found.')


    @property
    def recordings(self):
        return self.project / self._recordings_subdir


    @property
    def session(self):
        return self.recordings / self._subject / self._task / self._session


    def get_files(self, folder, **kwargs):
        """Get a list of files available in a specified sub-folder."""

        return get_files(getattr(self, folder), **kwargs)
