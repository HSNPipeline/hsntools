"""Paths object that defines a layout for single-unit project."""

from copy import deepcopy
from pathlib import Path

from convnwb.io.utils import get_files, get_subfolders, make_session_name

from convnwb.paths.defaults import PROJECT_FOLDERS, SUBJECT_FOLDERS, SESSION_FOLDERS

###################################################################################################
###################################################################################################

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
    def session_name(self):
        """Name of the session this object reflects."""
        return make_session_name(self._subject, self._experiment, self._session)


    @property
    def recordings(self):
        """"Path of the recordings folder."""
        return self.project / self._recordings_name


    @property
    def subject(self):
        """Path of the subject folder."""
        return self.recordings / self._subject


    @property
    def experiment(self):
        """"Path of the experiment folder."""
        return self.subject / self._experiment


    @property
    def session(self):
        """Path of the session folder."""
        return self.experiment / self._session


    def get_files(self, folder, **kwargs):
        """Get a list of files available in a specified folder."""

        return get_files(getattr(self, folder), **kwargs)


    def get_subfolders(self, folder, **kwargs):
        """Get a list of sub-folder available in a specified folder."""

        return get_subfolders(getattr(self, folder), **kwargs)
