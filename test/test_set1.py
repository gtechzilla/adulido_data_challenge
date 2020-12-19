import unittest
import numpy as np
from numpy.testing import assert_almost_equal, assert_equal, assert_string_equal
from numpy.testing import assert_allclose, assert_raises, assert_raises_regex
import pytest

    
def test_basic_test():
    out = {}
    assert_equal(isinstance(out, dict), True)
    
def test_for_checkbox_values():
    '''
    This tests to check if the values from the incoming call translates to the query.
    It checks for the length of the list as well as the values. 
    '''
    assert len(input_values) == len(checkbox_values)
    assert x: for x in checkbox_values is in input_values

def test_for_data_filter():
    '''
    Tests if the data displayed is as the data requested.
    '''
    assert data_displayed == data[query]

def test_for_end_API():
    '''
    This is to ensure that the end API is displayed with content choosen. 
    Even if there is no filter applied all data is displayed
    '''
    result = client.post('/recommend_sort_games/', data=json.dumps(data), content_type='application/json',)
    assert result.json is not None 