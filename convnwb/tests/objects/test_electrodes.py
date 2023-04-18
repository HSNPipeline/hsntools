"""Tests for convnwb.objects.electrodes"""

import pandas as pd

from convnwb.objects.electrodes import *

###################################################################################################
###################################################################################################

def test_electrodes():

    electrodes = Electrodes()
    assert electrodes

def test_electrodes_add_bundle():

    bundle_name = 'name'
    bundle_location = 'location'

    electrodes = Electrodes()
    electrodes.add_bundle(bundle_name, bundle_location)

    assert bundle_name in electrodes.bundles
    assert bundle_location in electrodes.locations

def test_electrodes_add_bundle():

    names = ['n1', 'n2']
    locations = ['l1', 'l2']

    electrodes = Electrodes()
    electrodes.add_bundles(names, locations)

    for name, location in zip(electrodes.bundles, electrodes.locations):
        assert name in electrodes.bundles
        assert location in electrodes.locations

def test_electrodes_n_bundles():

    electrodes = Electrodes()
    electrodes.add_bundles(['n1', 'n2'], ['l1', 'l2'])
    assert electrodes.n_bundles == 2

def test_electrodes_iter():

    names = ['n1', 'n2']
    locations = ['l1', 'l2']
    electrodes = Electrodes()
    electrodes.add_bundles(names, locations)

    for ind, (name, loc) in enumerate(electrodes):
        assert name in names
        assert loc in locations
    assert ind == len(names) - 1

def test_electrodes_to_dict():

    electrodes = Electrodes()
    electrodes.add_bundles(['n1', 'n2'], ['l1', 'l2'])
    odict = electrodes.to_dict()
    assert isinstance(odict, dict)

def test_electrodes_to_dataframe():

    electrodes = Electrodes()
    electrodes.add_bundles(['n1', 'n2'], ['l1', 'l2'])
    df = electrodes.to_dataframe()
    assert isinstance(df, pd.DataFrame)
