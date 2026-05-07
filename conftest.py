import pytest
from storm_centre import *

@pytest.fixture
def storm_centre():
    yield StormCentre()