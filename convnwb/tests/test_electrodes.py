"""Tests for convnwb.electrodes"""

from convnwb.electrodes import *

###################################################################################################
###################################################################################################

def test_electrodes():

    electrodes = Electrodes()
    assert electrodes

def test_electrodes_add_bundles():

    bundle_name = 'name'
    bundle_location = 'location'

    electrodes = Electrodes()
    electrodes.add_bundle(bundle_name, bundle_location)

    assert bundle_name in electrodes.bundles
    assert bundle_location in electrodes.locations
