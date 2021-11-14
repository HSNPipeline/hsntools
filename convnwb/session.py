"""Utilities for managing a session of data."""

import os
from pathlib import Path

from convnwb.io import get_files

###################################################################################################
###################################################################################################

SESSION_FOLDERS = ['behav', 'micro_lfp', 'raw_data', 'split_files', 'sorting', 'nwb']

def make_session_directory(subj, session, base_path, folders=SESSION_FOLDERS, verbose=True):
    """Create the folder structure for a session of data.

    Parameters
    ----------
    subj : str
        The subject code.
    session : int
        The number of the session to create the folder structure for.
    base_path str or Path
        The base path to the where to create the subject & session.
    verbose : bool, optional, default: True
        Whether to print out information.
    """

    base_path = Path(base_path)
    session = 'session_' + str(session)

    if verbose:
        print('Creating session directory for: {} / {}'.format(subj, session))
        print('Path: {}'.format(base_path / subj / session))

    if not os.path.exists(base_path / subj):
        print('Creating subject path: {}'.format(base_path / subj))
        os.mkdir(base_path / subj)

    if not os.path.exists(base_path / subj / session):
        print('Creating session path: {}'.format(base_path / subj / session))
        os.mkdir(base_path / subj / session)

    for folder in folders:
        print('Creating session sub-folders.')
        if not os.path.exists(base_path / subj / session / folder):
            os.mkdir(base_path / subj / session / folder)


class SDB():
    """Database object for a session of data."""

    def __init__(self, subj=None, session=None, base_path=None, folders=SESSION_FOLDERS):
        """Initialize a session DB object."""

        self.subj = subj
        self.session = 'session_' + str(session)
        self.base_path = Path(base_path)

        for folder in folders:
            setattr(self, folder, self.base_path / self.subj / self.session / folder)


    @property
    def subj_folder(self):
        return self.base_path / self.subj


    @property
    def session_folder(self):
        return self.base_path / self.subj / self.session


    def get_files(self, folder, **kwargs):
        """Get a list of files available in a specified sub-folder."""

        return get_files(getattr(self, folder), **kwargs)
