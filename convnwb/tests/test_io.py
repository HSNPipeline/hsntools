"""Tests for convnwb.io"""

import os

from convnwb.tests.tobjects import TestTask
from convnwb.tests.tsettings import TEST_FILE_PATH

from convnwb.io import *

###################################################################################################
###################################################################################################

def test_check_ext():

    f_name = 'test'
    ext = '.txt'

    out1 = check_ext(f_name, ext)
    assert out1 == 'test.txt'

    out2 = check_ext(f_name + '.txt', ext)
    assert out2 == 'test.txt'

def test_check_folder():

    folder = 'folder'
    f_name = 'file'

    out1 = check_folder(f_name, folder)
    assert out1 == 'folder/file'

    out2 = check_folder(f_name, None)
    assert out2 == 'file'

def test_drop_hidden_files():

    files = ['.', '.hidden', 'file_a', 'file_b']
    out = drop_hidden_files(files)
    assert out == ['file_a', 'file_b']

def test_ignore_files():

    files = ['data_1.txt', 'other.txt', 'data_2.txt', 'temp.txt']
    out = ignore_files(files, 'other')
    assert out == ['data_1.txt', 'data_2.txt', 'temp.txt']
    pass

def test_select_files():

    files = ['data_1.txt', 'other.txt', 'data_2.txt', 'temp.txt']
    out = select_files(files, 'data')
    assert out == ['data_1.txt', 'data_2.txt']

def test_sort_files():

    files = ['data_1.txt', 'other.txt', 'data_2.txt', 'temp.txt']
    out = sort_files(files)
    assert out == ['data_1.txt', 'data_2.txt', 'other.txt', 'temp.txt']

def test_get_files():

    out = get_files('.')
    assert isinstance(out, list)

def test_make_file_list():

    files = {'sub1' : ['session1', 'session2'], 'sub2' : ['session1']}
    out = make_file_list(files)
    assert isinstance(out, list)
    assert len(out) == 3
    for el in ['sub1_session1', 'sub1_session2', 'sub2_session1']:
        assert el in out

def test_save_config():

    cdict1 = {'d1' : 1, 'd2' : 'name', 'd3' : ['a', 'b', 'c']}
    f_name1 = 'test_config1'
    save_config(cdict1, f_name1, TEST_FILE_PATH)

    assert os.path.exists(os.path.join(TEST_FILE_PATH, f_name1 + '.yaml'))

    cdict2 = {'d1' : 'words', 'd2' : None, 'd3' : ['list', 'of', 'terms']}
    f_name2 = 'test_config2'
    save_config(cdict2, f_name2, TEST_FILE_PATH)

    assert os.path.exists(os.path.join(TEST_FILE_PATH, f_name2 + '.yaml'))

def test_load_config():

    f_name1 = 'test_config1'
    config = load_config(f_name1, TEST_FILE_PATH)
    assert isinstance(config, dict)

def test_load_configs():

    f_names = ['test_config1', 'test_config2']
    configs = load_configs(f_names, TEST_FILE_PATH)
    assert isinstance(configs, dict)

def test_save_task_object():

    task = TestTask()
    f_name = 'task_obj'
    save_task_object(task, f_name, TEST_FILE_PATH)

    assert os.path.exists(os.path.join(TEST_FILE_PATH, f_name + '.p'))

def test_load_task_object():

    f_name = 'task_obj'
    task = load_task_object(f_name, TEST_FILE_PATH)
    assert task

def test_save_json():

    data = {'a' : 12, 'b' : 21}
    f_name = 'test_json'

    save_json(data, f_name, TEST_FILE_PATH)
    assert os.path.exists(os.path.join(TEST_FILE_PATH, f_name + '.json'))

def test_load_json():

    f_name = 'test_json'
    data = load_json(f_name, TEST_FILE_PATH)
    assert data
