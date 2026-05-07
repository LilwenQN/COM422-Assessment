import pytest
from hurricane import Hurricane

def test_create_tropical_storm():
    hurricane = Hurricane("Amy", 70)
    assert hurricane.calculate_classification() == "Tropical Storm"
    assert hurricane.get_advice() == "Close storm shutters and stay away from windows"

def test_create_category_one():
    hurricane = Hurricane("Bram", 80)
    assert hurricane.calculate_classification() == "Category one"
    assert hurricane.get_advice() == "Close storm shutters and stay away from windows"

def test_create_category_one_LB_in():
    hurricane = Hurricane("Bram", 74)
    assert hurricane.calculate_classification() == "Category one"
    assert hurricane.get_advice() == "Close storm shutters and stay away from windows"
    
def test_create_category_one_LB_out():
    hurricane = Hurricane("Bram", 73)
    assert hurricane.calculate_classification() == "Tropical Storm"
    assert hurricane.get_advice() == "Close storm shutters and stay away from windows"

def test_create_category_one_UB_in():
    hurricane = Hurricane("Bram", 95)
    assert hurricane.calculate_classification() == "Category one"
    assert hurricane.get_advice() == "Close storm shutters and stay away from windows"
    
def test_create_category_one_UB_out():
    hurricane = Hurricane("Bram", 96)
    assert hurricane.calculate_classification() == "Category two"
    assert hurricane.get_advice() == "Close storm shutters and stay away from windows"