"""Tests for convnwb.session"""

import os

from convnwb.tests.tsettings import TEST_PROJECT_PATH

from convnwb.paths import *

###################################################################################################
###################################################################################################

def test_create_session_directory():

    subject = 'test_subject'
    task = 'test_task'
    session = 'session_0'
    recordings_subdir = 'test_recordings'

    create_session_directory(subject, task, session, TEST_PROJECT_PATH, recordings_subdir)

    test_path = TEST_PROJECT_PATH / recordings_subdir

    assert os.path.exists(test_path / subject)
    assert os.path.exists(test_path / subject / task)
    assert os.path.exists(test_path / subject / task / session)

    for subdir, subfolders in SESSION_FOLDERS.items():
        assert os.path.exists(test_path / subject / task / session / subdir)
        for subfolder in subfolders:
            assert os.path.exists(test_path / subject / task / session / subdir / subfolder)

def test_paths():

    subject = 'test_subject'
    task = 'test_task'
    session = 'session_0'
    recordings_subdir = 'test_recordings'

    paths = Paths(subject, task, session, TEST_PROJECT_PATH, recordings_subdir)
    assert paths

    for subdir, subfolders in SESSION_FOLDERS.items():
        assert getattr(paths, subdir)
        for subfolder in subfolders:
            assert getattr(paths, subfolder)

def test_paths_get_files():

    subject = 'test_subject'
    task = 'test_task'
    session = 'session_0'
    recordings_subdir = 'test_recordings'

    paths = Paths(subject, task, session, TEST_PROJECT_PATH, recordings_subdir)

    for subdir, subfolders in SESSION_FOLDERS.items():
        files = paths.get_files(subdir.split('_')[1])
        assert isinstance(files, list)
        for subfolder in subfolders:
            files = paths.get_files(subdir)
            assert isinstance(files, list)
