"""Tests for convnwb.paths.paths"""

from convnwb.tests.tsettings import TEST_PROJECT_PATH

from convnwb.paths.paths import *

###################################################################################################
###################################################################################################

def test_paths():

    subject = 'test_subject'
    task = 'test_task'
    session = 'session_0'
    recordings_name = 'test_recordings'

    # Test with minimal info
    paths = Paths(TEST_PROJECT_PATH)
    assert paths

    # Test with all info
    paths = Paths(TEST_PROJECT_PATH, subject, task, session,
                  recordings_name=recordings_name)
    assert paths

    for subdir, subfolders in SESSION_FOLDERS.items():
        assert getattr(paths, subdir)
        for subfolder in subfolders:
            assert getattr(paths, subfolder)
    for subdir in SUBJECT_FOLDERS:
        assert getattr(paths, subdir)
    for subdir in PROJECT_FOLDERS:
       assert getattr(paths, subdir)

def test_paths_get_files():

    subject = 'test_subject'
    task = 'test_task'
    session = 'session_0'
    recordings_name = 'test_recordings'

    paths = Paths(TEST_PROJECT_PATH, subject, task, session,
                  recordings_name=recordings_name)

    for subdir, subfolders in SESSION_FOLDERS.items():
        files = paths.get_files(subdir.split('_')[1])
        assert isinstance(files, list)
        for subfolder in subfolders:
            files = paths.get_files(subdir)
            assert isinstance(files, list)
    for subdir in SUBJECT_FOLDERS:
        files = paths.get_files(subdir)
        assert isinstance(files, list)
    for subdir in PROJECT_FOLDERS:
        files = paths.get_files(subdir)
        assert isinstance(files, list)
