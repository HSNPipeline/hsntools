"""
Directories & File Management
=============================

This example introduces and explores the file management and directory structure functionality
of `convnwb`.
"""

###################################################################################################
# SUBTITLE
# --------
#
#
#

# sphinx_gallery_thumbnail_number = 1

# Import paths related functionality
from convnwb.paths import Paths
from convnwb.paths import (create_project_directory,
                           create_subject_directory,
                           create_session_directory)

###################################################################################################

# Define settings for creating a project structure
project = 'tproj'
subject = 'subj1'
experiments = ['task1', 'task2']
exp1_sessions = [0, 1]
exp2_sessions = 'session_0'

###################################################################################################

# Create a base project directory
create_project_directory('.', project)

###################################################################################################

# Create an example subject directory
create_subject_directory(project, subject, experiments=experiments)

###################################################################################################

# Create an example session directory
create_session_directory(project, subject, 'task1', exp1_sessions)

###################################################################################################

# Create an session directory for the second task
create_session_directory(project, subject, 'task2', exp2_sessions)

###################################################################################################
#
#
#
#

###################################################################################################
#
#
#


###################################################################################################

# Create a paths object defined
paths = Paths('./tproj', subject, experiment=experiments[0], session=0)

###################################################################################################

# Print the directory structure from the paths object
paths.print_structure()

###################################################################################################




#
paths.get_files('docs')

###################################################################################################

#
paths.get_subfolders('recordings')

###################################################################################################

# ...
print(paths.all_paths)

###################################################################################################

# ...
print(paths.all_folders)

###################################################################################################
