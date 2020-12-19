import unittest
import numpy as np
from numpy.testing import assert_almost_equal, assert_equal, assert_string_equal
from numpy.testing import assert_allclose, assert_raises, assert_raises_regex
import json
import requests

    
def test_basic_test():
    out = {}
    assert_equal(isinstance(out, dict), True)



def test_for_end_API():
    '''
    test to see if we can get data to our API
    '''
    result = requests.post('/recommend_sort_games/', data=json.dumps(data), content_type='application/json',)
    assert result.json is not None 