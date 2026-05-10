import pytest
from hurricane import Hurricane
from tornado import Tornado
from blizzard import Blizzard

def _add_extra_storm(storm_centre):
    # Use this function so storm being read is not always the last storm that was added
    storm = Hurricane("Extra", 100)
    storm_centre.add_storm(storm)
    return storm_centre

def test_view_storm_hurricane(full_storm_centre):
    hurricane = Hurricane("Bert", 40)
    full_storm_centre.add_storm(hurricane)
    full_storm_centre = _add_extra_storm(full_storm_centre)
    assert full_storm_centre.view_storm("Bert") == hurricane

def test_view_storm_tornado(full_storm_centre):
    tornado = Tornado("Conall", 40)
    full_storm_centre.add_storm(tornado)
    full_storm_centre = _add_extra_storm(full_storm_centre)
    assert full_storm_centre.view_storm("Conall") == tornado

def test_view_storm_blizzard(full_storm_centre):
    blizzard = Blizzard("Darragh", 40, -20)
    full_storm_centre.add_storm(blizzard)
    full_storm_centre = _add_extra_storm(full_storm_centre)
    assert full_storm_centre.view_storm("Darragh") == blizzard

def test_view_storm_doesnt_exist(full_storm_centre):
    assert full_storm_centre.view_storm("hello") == None

def test_view_storm_empty_centre(storm_centre):
    assert storm_centre.view_storm("hello") == None