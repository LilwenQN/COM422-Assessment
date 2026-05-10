import pytest
from Storm import Storm
from hurricane import Hurricane
from tornado import Tornado
from blizzard import Blizzard

def _equivalent(actual: Storm, expected: Storm) -> bool:
    if type(actual) != type (expected):
        print("wrong type")
        return False
    if type(actual) == Blizzard and type(expected) == Blizzard:
        if (actual.wind_speed == expected.wind_speed
            and actual.temp == expected.temp
            and actual.name == expected.name):
            return True
        print(f"Actual speed: {actual.wind_speed}")
        print(f"Expected speed: {expected.wind_speed}")
        print(f"Actual temp: {actual.temp}")
        print(f"Expected temp: {expected.temp}")
        return False
    else:
        if (actual.wind_speed == expected.wind_speed
            and actual.name == expected.name):
            return True
        print(f"Actual speed: {actual.wind_speed}")
        print(f"Expected speed: {expected.wind_speed}")
        return False

def test_update_storm_hurricane(full_storm_centre):
    changes = {
        "windspeed" : 30
    }
    assert full_storm_centre.update_storm("Violet", changes) == True
    actual = full_storm_centre.view_storm("Violet")
    expected = Hurricane("Violet", 30)
    assert _equivalent(actual, expected) == True

def test_update_storm_tornado(full_storm_centre):
    changes = {
        "windspeed" : 30
    }
    assert full_storm_centre.update_storm("Wubbo", changes) == True
    actual = full_storm_centre.view_storm("Wubbo")
    expected = Tornado("Wubbo", 30)
    assert _equivalent(actual, expected) == True

def test_update_storm_blizzard_windspeed(full_storm_centre):
    changes = {
        "windspeed" : 30
    }
    assert full_storm_centre.update_storm("Ashley", changes) == True
    actual = full_storm_centre.view_storm("Ashley")
    expected = Blizzard("Ashley", 30, -12)
    assert _equivalent(actual, expected) == True

def test_update_storm_blizzard_temperature(full_storm_centre):
    changes = {
        "temperature" : 30
    }
    assert full_storm_centre.update_storm("Ashley", changes) == True
    actual = full_storm_centre.view_storm("Ashley")
    expected = Blizzard("Ashley", 25, 30)
    assert _equivalent(actual, expected) == True

def test_update_storm_blizzard_both(full_storm_centre):
    changes = {
        "windspeed" : 30,
        "temperature" : -30
    }
    assert full_storm_centre.update_storm("Ashley", changes) == True
    actual = full_storm_centre.view_storm("Ashley")
    expected = Blizzard("Ashley", 30, -30)
    assert _equivalent(actual, expected) == True

def test_update_storm_hurricane_temperature(full_storm_centre):
    changes = {
        "temperature" : 30
    }
    assert full_storm_centre.update_storm("Violet", changes) == False
    actual = full_storm_centre.view_storm("Violet")
    expected = Hurricane("Violet", 25)
    assert _equivalent(actual, expected) == True

def test_update_storm_tornado_temperature(full_storm_centre):
    changes = {
        "temperature" : 30
    }
    assert full_storm_centre.update_storm("Wubbo", changes) == False
    actual = full_storm_centre.view_storm("Wubbo")
    expected = Tornado("Wubbo", 25)
    assert _equivalent(actual, expected) == True

def test_update_storm_bad_key(full_storm_centre):
    changes = {
        "hello" : 30
    }
    assert full_storm_centre.update_storm("Violet", changes) == False
    actual = full_storm_centre.view_storm("Violet")
    expected = Hurricane("Violet", 25)
    assert _equivalent(actual, expected) == True

def test_update_storm_hurricane_temperature_and_windspeed(full_storm_centre):
    changes = {
        "windspeed" : 30,
        "temperature" : -30
    }
    assert full_storm_centre.update_storm("Violet", changes) == False
    actual = full_storm_centre.view_storm("Violet")
    expected = Hurricane("Violet", 25)
    assert _equivalent(actual, expected) == True

def test_update_storm_tornado_temperature_and_windspeed(full_storm_centre):
    changes = {
        "windspeed" : 30,
        "temperature" : -30
    }
    assert full_storm_centre.update_storm("Wubbo", changes) == False
    actual = full_storm_centre.view_storm("Wubbo")
    expected = Tornado("Wubbo", 25)
    assert _equivalent(actual, expected) == True

def test_update_storm_valid_and_invalid_keys(full_storm_centre):
    changes = {
        "windspeed" : 30,
        "temperature" : -30,
        "hello" : -40
    }
    assert full_storm_centre.update_storm("Ashley", changes) == False
    actual = full_storm_centre.view_storm("Ashley")
    expected = Blizzard("Ashley", 25, -12)
    assert _equivalent(actual, expected) == True

def test_update_storm_doesnt_exist(full_storm_centre):
    changes = {
        "temperature" : 30
    }
    assert full_storm_centre.update_storm("hello", changes) == False
    actual_violet = full_storm_centre.view_storm("Violet")
    actual_wubbo = full_storm_centre.view_storm("Wubbo")
    actual_ashley = full_storm_centre.view_storm("Ashley")
    expected = [Hurricane("Violet", 25), Tornado("Wubbo", 25), Blizzard("Ashley", 25, -12)]
    assert _equivalent(actual_violet, expected[0]) == True
    assert _equivalent(actual_wubbo, expected[1]) == True
    assert _equivalent(actual_ashley, expected[2]) == True

def test_update_storm_notdict_errors(full_storm_centre):
    changes = "this is not a dictionary"
    with pytest.raises(Exception, match="Values must be provided as a dictionary"):
        full_storm_centre.update_storm("Violet", changes)
    actual = full_storm_centre.view_storm("Violet")
    expected = Hurricane("Violet", 25)
    assert _equivalent(actual, expected) == True

def test_update_storm_empty_dict(full_storm_centre):
    changes: dict = {}
    assert full_storm_centre.update_storm("Violet", changes) == False
    actual = full_storm_centre.view_storm("Violet")
    expected = Hurricane("Violet", 25)
    assert _equivalent(actual, expected) == True