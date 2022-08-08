"""Tests for convnwb.task"""

from convnwb.task import *

###################################################################################################
###################################################################################################

def test_task_base():

    task = TaskBase()
    assert task

def test_task_data_keys():

    task = TaskBase()
    keys = task.data_keys()
    assert 'status' not in keys
    for attribute in ['trial', 'responses', 'sync', 'session']:
        assert attribute in keys

    # Test adding custom attribute
    task.custom = None
    assert 'custom' in task.data_keys()

def test_task_get_trial():

    # Check without using subfield
    task = TaskBase()
    trial_data = {'a' : [1, 2], 'b' : [True, False]}
    task.trial = trial_data
    assert task.get_trial(0) == {'a' : 1, 'b' : True}
    assert task.get_trial(1) == {'a' : 2, 'b' : False}

    # Check using subfield
    task = TaskBase()
    trial_data = {'top' : ['a1', 'a2'],
                  'field' : {'a' : [1, 2], 'b' : [True, False]}}
    task.trial = trial_data
    assert task.get_trial(0, 'field') == {'a' : 1, 'b' : True}
    assert task.get_trial(1, 'field') == {'a' : 2, 'b' : False}
