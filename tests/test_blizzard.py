import pytest
from blizzard import Blizzard

def test_create_snow_storm():
    blizzard = Blizzard("Nico", 20, 10)
    assert blizzard.calculate_classification() == "Snow Storm"
    assert blizzard.get_advice() == "Take care and avoid travel if possible."

def test_create_snow_storm_low_temp():
    blizzard = Blizzard("Nico", 20, -50)
    assert blizzard.calculate_classification() == "Snow Storm"
    assert blizzard.get_advice() == "Take care and avoid travel if possible."

def test_create_snow_storm_UB_in():
    blizzard = Blizzard("Nico", 34, 10)
    assert blizzard.calculate_classification() == "Snow Storm"
    assert blizzard.get_advice() == "Take care and avoid travel if possible."

def test_create_blizzard():
    blizzard = Blizzard("Oscar", 40, 10)
    assert blizzard.calculate_classification() == "Blizzard"
    assert blizzard.get_advice() == "Keep warm, Do not travel unless absolutely essential."

def test_create_blizzard_low_temp():
    blizzard = Blizzard("Oscar", 40, -50)
    assert blizzard.calculate_classification() == "Blizzard"
    assert blizzard.get_advice() == "Keep warm, Do not travel unless absolutely essential."

def test_create_blizzard_LB_in():
    blizzard = Blizzard("Oscar", 35, 10)
    assert blizzard.calculate_classification() == "Blizzard"
    assert blizzard.get_advice() == "Keep warm, Do not travel unless absolutely essential."

def test_create_blizzard_UB_in_low_temp():
    blizzard = Blizzard("Oscar", 44, -50)
    assert blizzard.calculate_classification() == "Blizzard"
    assert blizzard.get_advice() == "Keep warm, Do not travel unless absolutely essential."

def test_create_blizzard_fast_wind_high_temp():
    blizzard = Blizzard("Oscar", 400, 10)
    assert blizzard.calculate_classification() == "Blizzard"
    assert blizzard.get_advice() == "Keep warm, Do not travel unless absolutely essential."

def test_create_blizzard_fast_wind_high_temp_LB_in():
    blizzard = Blizzard("Oscar", 400, -11)
    assert blizzard.calculate_classification() == "Blizzard"
    assert blizzard.get_advice() == "Keep warm, Do not travel unless absolutely essential."

def test_create_severe_blizzard():
    blizzard = Blizzard("Patrick", 400, -100)
    assert blizzard.calculate_classification() == "Severe Blizzard"
    assert blizzard.get_advice() == "Keep warm, avoid all travel."

def test_create_severe_blizzard_wind_LB():
    blizzard = Blizzard("Patrick", 45, -100)
    assert blizzard.calculate_classification() == "Severe Blizzard"
    assert blizzard.get_advice() == "Keep warm, avoid all travel."

def test_create_severe_blizzard_temp_UB():
    blizzard = Blizzard("Patrick", 400, -12)
    assert blizzard.calculate_classification() == "Severe Blizzard"
    assert blizzard.get_advice() == "Keep warm, avoid all travel."