"""Tests for convnwb.utils.run"""

import os

from pytest import raises

from convnwb.tests.tsettings import TEST_ERRORS_PATH

from convnwb.utils.run import *

###################################################################################################
###################################################################################################

def test_check_failure():

    def _runner_error():
        raise ValueError('test error')

    try:
       _runner_error()
    except Exception as excp:
       catch_error(True, 'test_error', TEST_ERRORS_PATH)
    assert os.path.exists(TEST_ERRORS_PATH / 'test_error.txt')

    with raises(ValueError):
        try:
            _runner_error()
        except Exception as excp:
            catch_error(False, 'test_error', TEST_ERRORS_PATH)
