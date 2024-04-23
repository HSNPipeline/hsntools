"""Pytest configuration file for testing convnwb."""

import os
import shutil
from datetime import datetime
from dateutil.tz import tzlocal

from pynwb import NWBFile

import pytest

from convnwb.io import open_h5file
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

    with open_h5file('test_hdf5.h5', TEST_PATHS['file'], mode='w') as h5file:
        dset1 = h5file.create_dataset("data", (50,), dtype='i')
        dset2 = h5file.create_dataset("data2", (50,), dtype='f')

@pytest.fixture(scope='session', autouse=True)
def spike_data_file():
    """Save out a test combinato spike data file."""

    n_spikes = 5
    with open_h5file('data_chan_0.h5', TEST_PATHS['file'], mode='w') as h5file:
        dgroup = h5file.create_group('neg')
        dgroup.create_dataset('times', (n_spikes,), dtype='f')
        dgroup.create_dataset('spikes', (n_spikes, 64), dtype='f')
        dgroup.create_dataset('artifacts', (n_spikes,), dtype='i')

@pytest.fixture(scope='session', autouse=True)
def sort_data_file():
    """Save out a test combinato spike sorting file."""

    n_spikes = 5
    with open_h5file('sort_cat.h5', TEST_PATHS['file'], mode='w') as h5file:
        h5file.create_dataset('groups', (2, 4), dtype='i')
        h5file.create_dataset('index', (n_spikes,), dtype='f')
        h5file.create_dataset('classes', (n_spikes,), dtype='i')
