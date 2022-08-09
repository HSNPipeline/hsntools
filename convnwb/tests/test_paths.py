"""Tests for convnwb.session"""

import os

from convnwb.tests.tsettings import TEST_FILE_PATH

from convnwb.paths import *

###################################################################################################
###################################################################################################

def test_create_session_directory():

    task = 'test_task'
    subj = 'test_subj'
    session = 'session_0'
    create_session_directory(task=task, subj=subj, session=session,
                             base_path=TEST_FILE_PATH)

    assert os.path.exists(TEST_FILE_PATH / task)
    assert os.path.exists(TEST_FILE_PATH / task / subj)
    assert os.path.exists(TEST_FILE_PATH / task / subj / session)
    for folder in SESSION_FOLDERS:
        assert os.path.exists(TEST_FILE_PATH / task / subj / session / folder)

def test_supaths():

    task = 'test_task'
    subj = 'test_subj'
    session = 'session_0'
    db = SUPaths(task, subj, session, base_path=TEST_FILE_PATH)

    for folder in SESSION_FOLDERS:
        assert getattr(db, folder)

def test_supaths_get_files():

    task = 'test_task'
    subj = 'test_subj'
    session = 'session_0'
    db = SUPaths(task, subj, session, base_path=TEST_FILE_PATH)
    for folder in SESSION_FOLDERS:
        files = db.get_files(folder)
        assert isinstance(files, list)
