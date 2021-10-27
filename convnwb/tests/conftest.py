"""Pytest configuration file for testing convnwb."""

import os
import shutil

import pytest

from convnwb.tests.tsettings import TEST_FILE_PATH

###################################################################################################
###################################################################################################

## TEST SETUP

@pytest.fixture(scope='session', autouse=True)
def check_dir():
    """Once, prior to session, this will clear and re-initialize the test file directories."""

    # If the directories already exist, clear them
    if os.path.exists(TEST_FILE_PATH):
        shutil.rmtree(TEST_FILE_PATH)

    # Remake (empty) directories
    os.mkdir(TEST_FILE_PATH)
