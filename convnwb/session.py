"""Utilities for managing a session of data."""

import os
from pathlib import Path

from convnwb.io import get_files

###################################################################################################
###################################################################################################

BASE_FOLDERS = ['nwb']
REPO_FOLDERS = ['metadata', 'temp']
SESSION_FOLDERS = ['raw_data', 'behav', 'micro_lfp', 'neural',  'sorting', 'split_files']

def make_session_directory(subj, session, base_path, session_folders=SESSION_FOLDERS,
                           verbose=True):
    """Create the folder structure for a session of data.

    Parameters
    ----------
    subj : str
        The subject code.
    session : str
        The session label to create the folder structure for.
    base_path str or Path
        The base path to the where to create the subject & session.
    session_folders : list of str, optional
        Folder names to define as part of the session folder.
    verbose : bool, optional, default: True
        Whether to print out information.
    """

    if verbose:
        print('Creating session directory for: {} / {}'.format(subj, session))
        print('Path: {}'.format(base_path / subj / session))

    if not os.path.exists(base_path / subj):
        if verbose:
            print('Creating subject path: {}'.format(base_path / subj))
        os.mkdir(base_path / subj)

    if not os.path.exists(base_path / subj / session):
        if verbose:
            print('Creating session path: {}'.format(base_path / subj / session))
        os.mkdir(base_path / subj / session)

    if verbose:
        print('Creating session sub-folders.')
    for folder in session_folders:
        if not os.path.exists(base_path / subj / session / folder):
            os.mkdir(base_path / subj / session / folder)


class SDB():
    """Paths object for a session of data."""

    def __init__(self, subj=None, session=None, base_path=None, repo_path=None,
                 session_folders=SESSION_FOLDERS, base_folders=BASE_FOLDERS,
                 repo_folders=REPO_FOLDERS):
        """Initialize a session DB object.

        Parameters
        ----------
        subj : str
            Subject label.
        session : str
            Session label.
        data_path : str
            Base path to the data.
        repo_path : str
            Base path to the repository.
        session_folders, repo_folders, data_folders : list of str, optional
            The list of folder names for the session, repo, and data directories.
        """

        self._subj = subj
        self._session = session

        self.base_path = Path(base_path)
        self._reset_session_folders(session_folders)
        self._reset_base_folders(base_folders)

        if repo_path:
            self.repo_path = Path(repo_path)
            self._reset_repo_folders(repo_folders)

    @property
    def subj(self):
        return self.base_path / self._subj

    @property
    def session(self):
        return self.subj / self._session

    def _reset_session_folders(self, session_folders):

        for folder in session_folders:
            setattr(self, folder, self.session / folder)

    def _reset_base_folders(self, data_folders):

        for folder in data_folders:
            setattr(self, folder, self.base_path / folder)

    def _reset_repo_folders(self, repo_folders):

        for folder in repo_folders:
            setattr(self, folder, self.repo_path / folder)

    def get_files(self, folder, **kwargs):
        """Get a list of files available in a specified sub-folder."""

        return get_files(getattr(self, folder), **kwargs)
