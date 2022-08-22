"""Tests for convnwb.utils.log"""

from convnwb.utils.log import *

###################################################################################################
###################################################################################################

def test_print_status():

    print_status(True, 'words, words, words', 1)
    print_status(False, 'words, words, words', 2)

def test_get_current_date():

    date = get_current_date()
    assert isinstance(date, datetime)
