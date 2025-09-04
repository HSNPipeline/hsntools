"""File I/O."""

import json
import pickle

import yaml

from hsntools.io.utils import get_files, check_ext, check_folder
from hsntools.modutils.dependencies import safe_import, check_dependency

sio = safe_import('.io', 'scipy')
pd = safe_import('pandas')
mat73 = safe_import('mat73')

###################################################################################################
###################################################################################################

#### CONFIG FILES

def save_config(cdict, file_name, folder=None):
    """Save out a config file.

    Parameters
    ----------
    cdict : dict
        Dictionary of information to save to the config file.
    file_name : str
        File name to give the saved out config file.
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


### CUSTOM OBJECTS

def save_object(custom_object, file_name, folder=None):
    """Save a custom object.

    Parameters
    ----------
    custom_object : Task or Electrodes
        Object to save out.
    file_name : str
        File name to give the saved out object.
    folder : str or Path, optional
        Folder to save out to.

    Notes
    -----
    Custom objects are saved and loaded as pickle files.
    """

    ext = '.' + str(type(custom_object)).split('.')[-1].strip("'>").lower()
    if 'task' in ext:
        ext = '.task'

    with open(check_ext(check_folder(file_name, folder), ext), 'wb') as fobj:
        pickle.dump(custom_object, fobj)


def load_object(file_name, folder=None):
    """Load a custom object.

    Parameters
    ----------
    file_name : str
        File name of the file to load.
    folder : str or Path, optional
        Folder to load from.

    Returns
    -------
    custom_object
        Loaded task object.

    Notes
    -----
    Custom objects are saved and loaded as pickle files.
    """

    with open(check_folder(file_name, folder), 'rb') as load_obj:
        custom_object = pickle.load(load_obj)

    return custom_object

# alias these functions for backwards compatibility
save_task_object = save_object
def load_task_object(file_name, folder=None):
    return load_object(check_ext(file_name, '.task'), folder)
load_task_object.__doc__ = load_object

## OTHER FILE I/O

def save_txt(text, file_name, folder=None):
    """Save out text to a txt file.

    Parameters
    ----------
    text : str
        Text to save out to a txt file.
    file_name : str
        File name to give the saved out txt file.
    folder : str or Path, optional
        Folder to save out to.
    """

    with open(check_ext(check_folder(file_name, folder), '.txt'), 'w') as txt_file:
        txt_file.write(text)


def load_txt(file_name, folder=None):
    """Load text from a txt file.

    Parameters
    ----------
    file_name : str
        File name of the file to load.
    folder : str or Path, optional
        Folder to load from.

    Returns
    -------
    text : str
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
        File name to give the saved out json file.
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


def save_jsonlines(data, file_name, folder=None):
    """Save out data to a JSONlines file.

    Parameters
    ----------
    data : list of dict
        Data to save out to a JSONlines file.
    file_name : str
        File name to give the saved out json file.
    folder : str or Path, optional
        Folder to save out to.
    """

    with open(check_ext(check_folder(file_name, folder), '.json'), 'a') as jsonlines_file:
        for cur_data in data:
            json.dump(cur_data, jsonlines_file)
            jsonlines_file.write('\n')


def load_jsonlines(file_name, folder=None):
    """Load from a JSON lines file.

    Parameters
    ----------
    file_name : str
        File name of the file to load.
    folder : str or Path, optional
        Folder to load from.

    Returns
    -------
    data : dict
        Loaded data from the JSONlines file.
    """

    all_data = {}
    with open(check_ext(check_folder(file_name, folder), '.json'), 'r') as jsonlines_file:
        for line in jsonlines_file:
            line_data = json.loads(line)
            key = list(line_data.keys())[0]
            all_data[key] = line_data[key]

    return all_data


@check_dependency(pd, 'pandas')
def load_excel(file_name, folder, sheet=0):
    """Load an excel (xlsx) file.

    Parameters
    ----------
    file_name : str
        File name of the file to load.
    folder : str or Path, optional
        Folder to load from.

    Returns
    -------
    pd.DataFrame
        Loaded data from the excel file.
    """

    return pd.read_excel(check_ext(check_folder(file_name, folder), '.xlsx'),
                         engine='openpyxl', sheet_name=sheet)


def load_matfile(file_name, folder=None, version=None, **kwargs):
    """Load a .mat file.

    Parameters
    ----------
    file_name : str
        File name of the file to load.
    folder : str or Path, optional
        Folder to load from.
    version : {'scipy', 'mat73'}
        Which matfile load function to use:
            'scipy' : uses `scipy.io.loadmat`, works for matfiles older than v7.3
            'mat73' : uses `mat73.loadmat`, works for matfile v7.3 files
        If not specified, tries both.
    **kwargs
        Additional keywork arguments to pass into to matfile load function.

    Returns
    -------
    dict
        Loaded data from the matfile.
    """

    loaders = {
        'scipy' : _load_matfile_scipy,
        'mat73' : _load_matfile73,
    }

    file_path = check_ext(check_folder(file_name, folder), '.mat')

    if version:
        return loaders[version](file_path, **kwargs)
    else:
        try:
            _load_matfile_scipy(file_path, **kwargs)
        except NotImplementedError:
            return _load_matfile73(file_path, **kwargs)


@check_dependency(sio, 'scipy')
def _load_matfile_scipy(file_path, **kwargs):
    """Load matfile - scipy version."""

    return sio.loadmat(file_path, **kwargs)


@check_dependency(mat73, 'mat73')
def _load_matfile73(file_path, **kwargs):
    """Load matfile - mat73 version."""

    return mat73.loadmat(file_path, **kwargs)
