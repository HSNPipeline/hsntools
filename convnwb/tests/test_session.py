"""Tests for convnwb.session"""

import os

from convnwb.tests.tsettings import TEST_FILE_PATH

from convnwb.session import *

###################################################################################################
###################################################################################################

def test_make_session_directory():

    subj = 'test_subj'
    session = 0
    session_str = 'session_' + str(session)
    make_session_directory(subj=subj, session=session, base_path=TEST_FILE_PATH)

    assert os.path.exists(TEST_FILE_PATH / subj)
    assert os.path.exists(TEST_FILE_PATH / subj / session_str)
    for folder in SESSION_FOLDERS:
        assert os.path.exists(TEST_FILE_PATH / subj / session_str / folder)

def test_sdb():

    subj = 'test_subj'
    session = 0
    db = SDB(subj, session, base_path=TEST_FILE_PATH)

    for folder in SESSION_FOLDERS:
        assert getattr(db, folder)

def test_sdb_get_files():

    subj = 'test_subj'
    session = 0
    db = SDB(subj, session, base_path=TEST_FILE_PATH)
    for folder in SESSION_FOLDERS:
        files = db.get_files(folder)
        assert isinstance(files, list)
