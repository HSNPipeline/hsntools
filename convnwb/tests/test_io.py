"""Tests for convnwb.io"""

import os

import pandas as pd

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

def test_drop_ext():

    f_name = 'test'
    ext = '.txt'

    out1 = drop_ext(f_name + ext)
    assert out1 == 'test'

    out2 = drop_ext(f_name)
    assert out2 == 'test'

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

def test_drop_file_extensions():

    files = ['file_a.txt', 'file_b.json']
    out = drop_file_extensions(files)
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

def test_make_session_name():

    name1 = make_session_name('subject', 'experiment', 0)
    assert name1 == 'experiment_subject_session_0'

    name2 = make_session_name('subject', 'experiment', 'session_0')
    assert name2 == 'experiment_subject_session_0'

def test_make_file_list():

    files = {'sub1' : ['session1', 'session2'], 'sub2' : ['session1']}
    out = make_file_list('exp', files)
    assert isinstance(out, list)
    assert len(out) == 3
    for el in ['exp_sub1_session1', 'exp_sub1_session2', 'exp_sub2_session1']:
        assert el in out

    out2 = make_file_list('exp', files, ext='.nwb')

def test_file_in_list():

    file_name = 'test.txt'
    file_list1 = ['abc.txt', 'def.txt']
    file_list2 = ['test.txt', 'other_test.txt']

    assert file_in_list(file_name, file_list1) is False
    assert file_in_list(file_name, file_list2) is True

def test_missing_files():

    files = ['session1.nwb', 'session2.nwb', 'session3.nwb']
    compare = ['session1.nwb', 'session2.nwb']

    out = missing_files(files, compare)
    assert out == ['session3.nwb']

def test_get_files():

    out = get_files('.')
    assert isinstance(out, list)

def test_save_nwbfile(tnwbfile):

    test_fname = 'test_nwbfile'
    save_nwbfile(tnwbfile, test_fname, TEST_FILE_PATH)
    assert os.path.exists(os.path.join(TEST_FILE_PATH, test_fname + '.nwb'))

def test_load_nwbfile():

    test_fname = 'test_nwbfile'
    tnwbfile = load_nwbfile(test_fname, TEST_FILE_PATH)
    assert tnwbfile

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

    assert os.path.exists(os.path.join(TEST_FILE_PATH, f_name + '.task'))

def test_load_task_object():

    f_name = 'task_obj'
    task = load_task_object(f_name, TEST_FILE_PATH)
    assert task

def test_save_txt():

    text = "Words, words, words."
    f_name = 'test_txt'

    save_txt(text, f_name, TEST_FILE_PATH)
    assert os.path.exists(os.path.join(TEST_FILE_PATH, f_name + '.txt'))

def test_load_txt():

    f_name = 'test_txt'
    text = load_txt(f_name, TEST_FILE_PATH)
    assert text

def test_save_json():

    data = {'a' : 12, 'b' : 21}
    f_name = 'test_json'

    save_json(data, f_name, TEST_FILE_PATH)
    assert os.path.exists(os.path.join(TEST_FILE_PATH, f_name + '.json'))

def test_load_json():

    f_name = 'test_json'
    data = load_json(f_name, TEST_FILE_PATH)
    assert data

def test_save_jsonlines():

    data = [{'A1' : {'a' : 12, 'b' : 21}},
            {'A2' : {'a' : 21, 'b' : 12}}]
    f_name = 'test_jsonlines'

    save_jsonlines(data, f_name, TEST_FILE_PATH)
    assert os.path.exists(os.path.join(TEST_FILE_PATH, f_name + '.json'))

def test_load_jsonlines():

    f_name = 'test_jsonlines'
    data = load_jsonlines(f_name, TEST_FILE_PATH)
    assert data
    assert isinstance(data, dict)
    assert isinstance(data[list(data.keys())[0]], dict)

def test_load_jsons_to_df():

    files = ['test_json', 'test_json']
    out = load_jsons_to_df(files, TEST_FILE_PATH)
    assert isinstance(out, pd.DataFrame)
    assert len(out) == len(files)

    # Test giving a file location
    out = load_jsons_to_df(TEST_FILE_PATH)
    assert isinstance(out, pd.DataFrame)
