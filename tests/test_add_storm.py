import pytest
from blizzard import Blizzard
from hurricane import Hurricane
from tornado import Tornado

def test_add_storm_hurricane(storm_centre):
    hurricane = Hurricane("Ruby", 100)
    assert storm_centre.add_storm(hurricane) == True
    
def test_add_storm_tornado(storm_centre):
    tornado = Tornado("Ruby", 100)
    assert storm_centre.add_storm(tornado) == True

def test_add_storm_blizzard(storm_centre):
    blizzard = Blizzard("Ruby", 45, 20)
    assert storm_centre.add_storm(blizzard) == True

def test_add_storm_duplicate_name_hurricane(storm_centre):
    storm_centre.add_storm(Hurricane("Ruby", 100))
    assert storm_centre.add_storm(Hurricane("Ruby", 10)) == False

def test_add_storm_duplicate_name_tornado(storm_centre):
    storm_centre.add_storm(Tornado("Ruby", 100))
    assert storm_centre.add_storm(Tornado("Ruby", 10)) == False

def test_add_storm_duplicate_name_blizzard(storm_centre):
    storm_centre.add_storm(Blizzard("Ruby", 100, 0))
    assert storm_centre.add_storm(Blizzard("Ruby", 10, 0)) == False

def test_add_storm_duplicate_name_hurricane_tornado(storm_centre):
    storm_centre.add_storm(Hurricane("Ruby", 100))
    assert storm_centre.add_storm(Tornado("Ruby", 10)) == False

def test_add_storm_duplicate_name_hurricane_blizzard(storm_centre):
    storm_centre.add_storm(Hurricane("Ruby", 100))
    assert storm_centre.add_storm(Blizzard("Ruby", 10, 0)) == False

def test_add_storm_duplicate_name_blizzard_tornado(storm_centre):
    storm_centre.add_storm(Blizzard("Ruby", 100, 0))
    assert storm_centre.add_storm(Tornado("Ruby", 10)) == False

def test_add_storm_different_name_hurricane(storm_centre):
    storm_centre.add_storm(Hurricane("Stevie", 100))
    assert storm_centre.add_storm(Hurricane("Tadhg", 10)) == True

def test_add_storm_different_name_tornado(storm_centre):
    storm_centre.add_storm(Tornado("Stevie", 100))
    assert storm_centre.add_storm(Tornado("Tadhg", 10)) == True

def test_add_storm_different_name_blizzard(storm_centre):
    storm_centre.add_storm(Blizzard("Stevie", 100, 0))
    assert storm_centre.add_storm(Blizzard("Tadhg", 10, 0)) == True

def test_add_storm_different_name_hurricane_tornado(storm_centre):
    storm_centre.add_storm(Hurricane("Stevie", 100))
    assert storm_centre.add_storm(Tornado("Tadhg", 10)) == True

def test_add_storm_different_name_hurricane_blizzard(storm_centre):
    storm_centre.add_storm(Hurricane("Stevie", 100))
    assert storm_centre.add_storm(Blizzard("Tadhg", 10, 0)) == True

def test_add_storm_different_name_blizzard_tornado(storm_centre):
    storm_centre.add_storm(Blizzard("Stevie", 100, 0))
    assert storm_centre.add_storm(Tornado("Tadhg", 10)) == True

def test_add_storm_20(storm_centre):
    for i in range(20):
        assert storm_centre.add_storm(Hurricane(str(i), 100)) == True

def test_add_storm_21(storm_centre):
    for i in range(20):
        assert storm_centre.add_storm(Hurricane(str(i), 100)) == True
    assert storm_centre.add_storm(Hurricane("21", 100)) == False