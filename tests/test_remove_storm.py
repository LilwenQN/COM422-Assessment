import pytest

def test_remove_storm_hurricane(full_storm_centre):
    assert full_storm_centre.remove_storm("Violet") == True
    assert full_storm_centre.already_exists("Violet") == False

def test_remove_storm_tornado(full_storm_centre):
    assert full_storm_centre.remove_storm("Wubbo") == True
    assert full_storm_centre.already_exists("Wubbo") == False
    
def test_remove_storm_blizzard(full_storm_centre):
    assert full_storm_centre.remove_storm("Ashley") == True
    assert full_storm_centre.already_exists("Ashley") == False

def test_remove_storm_doesnt_exist(full_storm_centre):
    assert full_storm_centre.remove_storm("hello") == False

def test_remove_storm_empty_centre(storm_centre):
    assert storm_centre.remove_storm("hello") == False