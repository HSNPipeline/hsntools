"""Utility functions for managing files."""

import os
import json
import pickle

import yaml

###################################################################################################
###################################################################################################

### FILE UTILITIES

def check_ext(file_name, ext):
    """Check the extension for a file name, and add if missing.

    Parameters
    ----------
    file_name : str
        The name of the file.
    ext : str
        The extension to check and add.

    Returns
    -------
    str
        File name with the extension added.
    """

    return file_name + ext if not file_name.endswith(ext) else file_name


def check_folder(file_name, folder):
    """Check a file name, adding folder path if needed.

    Parameters
    ----------
    file_name : str
        The name of the file.
    folder : str or Path, optional
        Folder location of the file.

    Returns
    -------
    str
        Full path of the file.
    """

    return os.path.join(folder, file_name) if folder else file_name


def drop_hidden_files(files):
    """Clean hidden files from a list of files.

    Parameters
    ----------
    files : list of str
        File list.

    Returns
    -------
    list of str
        File list with hidden files dropped.
    """

    return [file for file in files if file[0] != '.']


def drop_file_extensions(files):
    """Drop the file extensions from a list of file names.

    Parameters
    ----------
    files : list of str
        File list.

    Returns
    -------
    list of str
        File list with extensions dropped.
    """

    return [file.split('.')[0] for file in files]


def ignore_files(files, ignore):
    """Ignore files based on a search term of interest.

    Parameters
    ----------
    files : list of str
        File list.
    ignore : str
        String to use to drop files from list.

    Returns
    -------
    list of str
        File list with ignored files dropped.
    """

    return [file for file in files if ignore not in file]


def select_files(files, search):
    """Select files based on a search term of interest.

    Parameters
    ----------
    files : list of str
        File list.
    search : str
        String to use to keep files.

    Returns
    -------
    list of str
        File list with selected files kept.
    """

    return [file for file in files if search in file]


def sort_files(files):
    """Sort a list of file names.

    Parameters
    ----------
    files : list of str
        List of file names, to sort.

    Returns
    -------
    list of str
        Sorted list of files.
    """

    return sorted(files)


### GENERAL FILE I/O

def get_files(folder, select=None, ignore=None, drop_hidden=True, sort=True, drop_extensions=False):
    """Get a list of files from a directory.

    Parameters
    ----------
    folder : str or Path
        Name of the folder to get the list of files from.
    select : str, optional
        A search string to use to select files.
    ignore : str, optional
        A search string to use to drop files.
    drop_hidden : bool, optional, default: True
        Whether to drop hidden files from the list.
    sort : bool, optional, default: True
        Whether to sort the list of file names.
    drop_extensions : bool, optional, default: False
        Whether the drop the file extensions from the returned file list.

    Returns
    -------
    list of str
        A list of files from the folder.
    """

    files = os.listdir(folder)

    # If requested, drop any hidden files (leading .'s)
    if drop_hidden:
        files = drop_hidden_files(files)

    # If requested, filter files to those that containing given search terms
    if select:
        files = select_files(files, select)

    # If requested, filter files to ignore any containing given search terms
    if ignore:
        files = ignore_files(files, ignore)

    # If requestied, sort the list of files
    if sort:
        files = sort_files(files)

    if drop_extensions:
        files = drop_file_extensions(files)

    return files


#### DATA FILES

def make_file_list(files):
    """Make a list of subject files.

    Parameters
    ----------
    files : dict
        Collection of files per subject.

    Returns
    -------
    file_lst : list of str
        List of all subject files.
    """

    file_list = []
    for subj, sessions in files.items():
        for session in sessions:
            file_list.append(subj + '_' + session)

    return file_list


#### CONFIG FILES

def save_config(cdict, file_name, folder=None):
    """Save out a config file.

    Parameters
    ----------
    cdict : dict
        Dictionary of information to save to the config file.
    file_name : str
        File name for the saved out file.
    folder : str or Path, optional
        Folder to save the config file to.
    """

    with open(check_ext(check_folder(file_name, folder), '.yaml'), 'w') as file:
        yaml.dump(cdict, file)


def load_config(file_name, folder=None):
    """Load an individual config file.

    Parameters
    ----------
    file_name : str
        Name of the config file to load.
    folder : str or Path, optional
        Folder to load the config file from.

    Returns
    -------
    data : dict
        Information from the loaded config file.
    """

    with open(check_ext(check_folder(file_name, folder), '.yaml'), 'r') as fobj:
        data = yaml.safe_load(fobj)

    return data


def load_configs(files, folder=None):
    """Load all configs together.

    Parameters
    ----------
    files : list of str
        Names of all the config files to load.
    folder : str or Path, optional
        Folder to load the config files from.

    Returns
    -------
    configs : dict
        Information from the config files.
    """

    configs = {}
    for file in files:
        label = file.split('_')[0]
        configs[label] = load_config(file, folder=folder)

    return configs


### TASK OBJECTS

def save_task_object(task, file_name, folder=None):
    """Save a task object.

    Parameters
    ----------
    task : Task
        Task object to save out.
    file_name : str
        Name for the file to be saved out.
    folder : str or Path, optional
        Folder to save out to.

    Notes
    -----
    Task objects are saved and loaded as pickle files.
    """

    with open(check_ext(check_folder(file_name, folder), '.task'), 'wb') as fobj:
        pickle.dump(task, fobj)


def load_task_object(file_name, folder=None):
    """Load a task object.

    Parameters
    ----------
    file_name : str
        File name of the file to load.
    folder : str or Path, optional
        Folder to load from.

    Returns
    -------
    task
        Loaded task object.

    Notes
    -----
    Task objects are saved and loaded as pickle files.
    """

    with open(check_ext(check_folder(file_name, folder), '.task'), 'rb') as load_obj:
        task = pickle.load(load_obj)

    return task


## OTHER FILE I/O

def save_txt(text, file_name, folder=None):
    """Save out a string of information to a txt file.

    Parameters
    ----------
    text : str
        Text to save out to a txt file.
    file_name : str
        File name to label the saved out file.
    folder : str or Path, optional
        Folder to save out to.
    """

    with open(check_ext(check_folder(file_name, folder), '.txt'), 'w') as txt_file:
        txt_file.write(text)


def load_txt(file_name, folder=None):
    """Load from a JSON file.

    Parameters
    ----------
    file_name : str
        File name of the file to load.
    folder : str or Path, optional
        Folder to load from.

    Returns
    -------
    text : dict
        Loaded text from the txt file.
    """

    with open(check_ext(check_folder(file_name, folder), '.txt')) as txt_file:
        text = txt_file.readlines()

    return text


def save_json(data, file_name, folder=None):
    """Save out a dictionary of data to a JSON file.

    Parameters
    ----------
    data : dict
        Data to save out to a JSON file.
    file_name : str
        File name to label the saved out file.
    folder : str or Path, optional
        Folder to save out to.
    """

    with open(check_ext(check_folder(file_name, folder), '.json'), 'w') as json_file:
        json.dump(data, json_file)


def load_json(file_name, folder=None):
    """Load from a JSON file.

    Parameters
    ----------
    file_name : str
        File name of the file to load.
    folder : str or Path, optional
        Folder to load from.

    Returns
    -------
    data : dict
        Loaded data from the JSON file.
    """

    with open(check_ext(check_folder(file_name, folder), '.json')) as json_file:
        data = json.load(json_file)

    return data
