import pytest
from hurricane import Hurricane

def test_create_tropical_storm():
    hurricane = Hurricane("Amy", 70)
    assert hurricane.calculate_classification() == "Tropical Storm"
    assert hurricane.get_advice() == "Close storm shutters and stay away from windows"

def test_create_category_one_LB_out():
    hurricane = Hurricane("Bram", 73)
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

def test_create_category_one_UB_in():
    hurricane = Hurricane("Bram", 95)
    assert hurricane.calculate_classification() == "Category one"
    assert hurricane.get_advice() == "Close storm shutters and stay away from windows"

def test_create_category_two():
    hurricane = Hurricane("Chandra", 100)
    assert hurricane.calculate_classification() == "Category two"
    assert hurricane.get_advice() == "Close storm shutters and stay away from windows"

def test_create_category_two_LB_in():
    hurricane = Hurricane("Chandra", 96)
    assert hurricane.calculate_classification() == "Category two"
    assert hurricane.get_advice() == "Close storm shutters and stay away from windows"

def test_create_category_two_UB_in():
    hurricane = Hurricane("Chandra", 110)
    assert hurricane.calculate_classification() == "Category two"
    assert hurricane.get_advice() == "Close storm shutters and stay away from windows"

def test_create_category_three():
    hurricane = Hurricane("Dave", 120)
    assert hurricane.calculate_classification() == "Category three"
    assert hurricane.get_advice() == "Coastal regions are encouraged to evacuate"

def test_create_category_three_LB_in():
    hurricane = Hurricane("Dave", 111)
    assert hurricane.calculate_classification() == "Category three"
    assert hurricane.get_advice() == "Coastal regions are encouraged to evacuate"

def test_create_category_three_UB_in():
    hurricane = Hurricane("Dave", 129)
    assert hurricane.calculate_classification() == "Category three"
    assert hurricane.get_advice() == "Coastal regions are encouraged to evacuate"

def test_create_category_four():
    hurricane = Hurricane("Eddie", 140)
    assert hurricane.calculate_classification() == "Category four"
    assert hurricane.get_advice() == "Evacuate"

def test_create_category_four_LB_in():
    hurricane = Hurricane("Eddie", 130)
    assert hurricane.calculate_classification() == "Category four"
    assert hurricane.get_advice() == "Evacuate"

def test_create_category_four_UB_in():
    hurricane = Hurricane("Eddie", 156)
    assert hurricane.calculate_classification() == "Category four"
    assert hurricane.get_advice() == "Evacuate"

def test_create_category_five():
    hurricane = Hurricane("Fionnuala", 4000)
    assert hurricane.calculate_classification() == "Category five"
    assert hurricane.get_advice() == "Evacuate"

def test_create_category_five_LB_in():
    hurricane = Hurricane("Fionnuala", 157)
    assert hurricane.calculate_classification() == "Category five"
    assert hurricane.get_advice() == "Evacuate"