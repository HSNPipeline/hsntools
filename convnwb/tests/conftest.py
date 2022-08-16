"""Pytest configuration file for testing convnwb."""

import os
import shutil
from datetime import datetime
from dateutil.tz import tzlocal

from pynwb import NWBFile

import pytest

from convnwb.tests.tsettings import TEST_FILE_PATH, TEST_PROJECT_PATH

###################################################################################################
###################################################################################################

## TEST SETUP

@pytest.fixture(scope='session', autouse=True)
def check_dir():
    """Once, prior to session, this will clear and re-initialize the test file directories."""

    # Clear and re-initialize test directories
    for TEST_PATH in [TEST_FILE_PATH, TEST_PROJECT_PATH]:
        if os.path.exists(TEST_PATH):
            shutil.rmtree(TEST_PATH)

        # Remake (empty) directories
        os.mkdir(TEST_PATH)


@pytest.fixture(scope='session')
def tnwbfile():
    """Create a test NWBfile."""

    yield NWBFile('session_desc', 'session_id', datetime.now(tzlocal()))
