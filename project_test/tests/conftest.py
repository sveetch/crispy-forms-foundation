"""
Some fixture methods
"""
import os
import pytest

@pytest.fixture(scope='session')
def output_test_path(pytestconfig):
    """Return absolute path to test outputs directory"""
    return os.path.join(pytestconfig.rootdir.strpath, 'tests', 'output')
