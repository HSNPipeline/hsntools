"""Tests for convnwb.electrodes"""

from convnwb.electrodes import *

###################################################################################################
###################################################################################################

def test_electrodes_base():

    electrodes = ElectrodesBase()
    assert electrodes
