"""Settings for tests."""

import os
from pathlib import Path
import pkg_resources as pkg

###################################################################################################
###################################################################################################

# Set paths for test files
TEST_FILE_PATH = Path(pkg.resource_filename(__name__, 'test_files'))
