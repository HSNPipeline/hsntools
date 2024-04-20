"""Pytest configuration file for testing convnwb."""

import os
import shutil
from datetime import datetime
from dateutil.tz import tzlocal

import h5py
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

@pytest.fixture(scope='session', autouse=True)
def th5file():
    """Save out a test HDF5 file."""

    with h5py.File(TEST_PATHS['file'] / "test_hdf5.h5", "w") as h5file:
        dset1 = h5file.create_dataset("data", (50,), dtype='i')
        dset2 = h5file.create_dataset("data2", (50,), dtype='f')
