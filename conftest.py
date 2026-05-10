import pytest
from storm_centre import *

@pytest.fixture
def storm_centre():
    yield StormCentre()

@pytest.fixture
def full_storm_centre():
    storm_centre = StormCentre()
    storm_centre.add_storm(Hurricane("Violet", 25))
    storm_centre.add_storm(Tornado("Wubbo", 25))
    storm_centre.add_storm(Blizzard("Ashley", 25, -12))
    yield storm_centre