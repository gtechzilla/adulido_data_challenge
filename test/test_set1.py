import unittest
import numpy as np
from numpy.testing import assert_almost_equal, assert_equal, assert_string_equal
from numpy.testing import assert_allclose, assert_raises, assert_raises_regex


def test_basic_test():
    out = {}
    assert_equal(isinstance(out, dict), True)
    