"""Utilities for managing a session of data."""

import os
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

# REPO_FOLDERS = [
#     'metadata',
#     'temp',
# ]

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

def create_session_directory(subject, task, session, recordings_path,
                             session_folders=SESSION_FOLDERS, verbose=True):
    """Create the folder structure for a session of data.

    Parameters
    ----------
    subject : str
        The subject code.
    task : str
        The task name.
    session : str
        The session label to create the folder structure for.
    recordings_path : str or Path
        The path to the recordings folder.
    session_folders : dict, optional
        Defines the folder names to define as part of the session folder.
        Each key defines a sub-directory within the `session` folder.
        Each set of values if a list of folder names for within each sub-directory.
    verbose : bool, optional, default: True
        Whether to print out information.
    """

    recordings_path = Path(recordings_path)

    print_status(verbose, 'Creating session directory...', 0)
    print_status(verbose, 'Path: {}'.format(recordings_path / subject / task / session), 1)

    if not os.path.exists(recordings_path / subject):
        #print_status(verbose, 'Creating subject path...', 1)
        os.mkdir(recordings_path / subject)

    if not os.path.exists(recordings_path / subject / task):
        #print_status(verbose, 'Creating task path...', 1)
        os.mkdir(recordings_path / subject / task)

    if not os.path.exists(recordings_path / subject / task / session):
        #print_status(verbose, 'Creating session path...', 1)
        os.mkdir(recordings_path / subject / task / session)

    #print_status(verbose, 'Creating session sub-folders....', 1)
    for subdir, subfolders in session_folders.items():
        if not os.path.exists(recordings_path / subject / task / session / subdir):
            os.mkdir(recordings_path / subject / task / session / subdir)
        for subfolder in subfolders:
            if not os.path.exists(recordings_path / subject / task / session / subdir / subfolder):
                os.mkdir(recordings_path / subject / task / session / subdir / subfolder)


# class SUPaths():
#     """Paths object for a session of single-unit data."""

#     def __init__(self, task=None, subj=None, session=None,
#                  base_path=None, repo_path=None,
#                  session_folders=SESSION_FOLDERS,
#                  base_folders=BASE_FOLDERS,
#                  repo_folders=REPO_FOLDERS):
#         """Initialize a session DB object.

#         Parameters
#         ----------
#         task : str
#             Task name.
#         subject : str
#             Subject label.
#         session : str
#             Session label.
#         data_path : str
#             Base path to the data.
#         repo_path : str
#             Base path to the repository.
#         session_folders, repo_folders, data_folders : list of str, optional
#             The list of folder names for the session, repo, and data directories.
#         """

#         self._task = task
#         self._subject = subject
#         self._session = session

#         self.base_path = Path(base_path)
#         self._reset_session_folders(session_folders)
#         self._reset_base_folders(base_folders)

#         if repo_path:
#             self.repo_path = Path(repo_path)
#             self._reset_repo_folders(repo_folders)

#     @property
#     def data(self):
#         return self.base_path / self._task

#     @property
#     def subj(self):
#         return self.data / self._subj

#     @property
#     def session(self):
#         return self.subj / self._session

#     def _reset_session_folders(self, session_folders):

#         for folder in session_folders:
#             setattr(self, folder, self.session / folder)

#     def _reset_base_folders(self, data_folders):

#         for folder in data_folders:
#             setattr(self, folder, self.base_path / folder)

#     def _reset_repo_folders(self, repo_folders):

#         for folder in repo_folders:
#             setattr(self, folder, self.repo_path / folder)

#     def get_files(self, folder, **kwargs):
#         """Get a list of files available in a specified sub-folder."""

#         return get_files(getattr(self, folder), **kwargs)
