"""Pytest configuration file for testing convnwb."""

import os
import shutil
from datetime import datetime
from dateutil.tz import tzlocal

from pynwb import NWBFile

import pytest

from convnwb.tests.tsettings import BASE_TEST_OUTPUTS_PATH, TEST_PATHS

###################################################################################################
###################################################################################################

## TEST SETUP

@pytest.fixture(scope='session', autouse=True)
def check_dir():
    """Once, prior to session, this will clear and re-initialize the test file directories."""

    # If the directories already exist, clear them
    if os.path.exists(BASE_TEST_OUTPUTS_PATH):
        shutil.rmtree(BASE_TEST_OUTPUTS_PATH)

    # Remake base test outputs path, and then each sub-directory
    os.mkdir(BASE_TEST_OUTPUTS_PATH)
    for name, TEST_PATH in TEST_PATHS.items():
        os.mkdir(TEST_PATH)

@pytest.fixture(scope='session')
def tnwbfile():
    """Create a test NWBfile."""

    yield NWBFile('session_desc', 'session_id', datetime.now(tzlocal()))
