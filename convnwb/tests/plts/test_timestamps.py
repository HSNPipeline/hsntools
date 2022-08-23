"""Tests for convnwb.plts.timestamps"""

from convnwb.tests.tutils import plot_test
from convnwb.tests.tsettings import TEST_PLOTS_PATH

from convnwb.plts.timestamps import *

###################################################################################################
###################################################################################################

@plot_test
def test_plot_alignment():

    arr1 = [1, 2, 3, 4, 5]
    arr2 = [1, 2, 3, 4, 5]

    plot_alignment(arr1, arr2)
