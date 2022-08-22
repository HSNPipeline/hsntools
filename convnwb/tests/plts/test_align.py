"""Tests for convnwb.plts.align"""

from convnwb.plts.align import *

###################################################################################################
###################################################################################################

def test_plot_alignment():

    arr1 = [1, 2, 3, 4, 5]
    arr2 = [1, 2, 3, 4, 5]

    plot_alignment(arr1, arr2)

    # Check that the plot was created
    ax = plt.gca()
    assert ax.has_data()
