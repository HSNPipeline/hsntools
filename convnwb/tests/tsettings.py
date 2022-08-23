"""Settings for tests."""

from pathlib import Path
import pkg_resources as pkg

###################################################################################################
###################################################################################################

# Set base test files path
BASE_TEST_OUTPUTS_PATH = Path(pkg.resource_filename(__name__, 'test_outputs'))

# Set paths for test files, separated by type
TEST_FILE_PATH = BASE_TEST_OUTPUTS_PATH / 'test_files'
TEST_PLOTS_PATH = BASE_TEST_OUTPUTS_PATH / 'test_plots'
TEST_PROJECT_PATH = BASE_TEST_OUTPUTS_PATH / 'test_project'
