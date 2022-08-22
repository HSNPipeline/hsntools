"""Tests for convnwb.paths.create"""

import os

from convnwb.tests.tsettings import TEST_FILE_PATH, TEST_PROJECT_PATH

from convnwb.paths.create import *

###################################################################################################
###################################################################################################

def test_make_folder():

    make_folder(TEST_FILE_PATH / 'test_folder')
    assert os.path.exists(TEST_FILE_PATH / 'test_folder')
    make_folder(TEST_FILE_PATH / 'test_folder')

def test_create_project_directory():

    project = 'test_project'
    project_path = TEST_PROJECT_PATH.parent
    create_project_directory(project_path, project)
    assert os.path.exists(project_path / project)
    for subdir in PROJECT_FOLDERS:
        assert os.path.exists(project_path / project / subdir)

def test_create_subject_directory():

    subject = 'test_subject'
    recordings_name = 'test_recordings'

    create_subject_directory(TEST_PROJECT_PATH, subject,
                             recordings_name=recordings_name)

    test_path = TEST_PROJECT_PATH / recordings_name

    assert os.path.exists(test_path / subject)
    for subdir in SUBJECT_FOLDERS:
        assert os.path.exists(test_path / subject / subdir)

def test_create_session_directory():

    subject = 'test_subject'
    task = 'test_task'
    session = 'session_0'
    recordings_name = 'test_recordings'

    create_session_directory(TEST_PROJECT_PATH, subject, task, session,
                             recordings_name=recordings_name)

    test_path = TEST_PROJECT_PATH / recordings_name

    assert os.path.exists(test_path / subject)
    assert os.path.exists(test_path / subject / task)
    assert os.path.exists(test_path / subject / task / session)

    for subdir, subfolders in SESSION_FOLDERS.items():
        assert os.path.exists(test_path / subject / task / session / subdir)
        for subfolder in subfolders:
            assert os.path.exists(test_path / subject / task / session / subdir / subfolder)
