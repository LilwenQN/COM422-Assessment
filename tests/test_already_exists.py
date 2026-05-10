import pytest

def test_find_hurricane(full_storm_centre):
    assert full_storm_centre.already_exists("Violet") == True

def test_find_tornado(full_storm_centre):
    assert full_storm_centre.already_exists("Wubbo") == True

def test_find_blizzard(full_storm_centre):
    assert full_storm_centre.already_exists("Ashley") == True

def test_does_not_exist(full_storm_centre):
    assert full_storm_centre.already_exists("hello") == False