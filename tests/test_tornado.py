import pytest
from tornado import Tornado

def test_create_f0():
    tornado = Tornado("Gerard", 50)
    assert tornado.calculate_classification() == "F0"
    assert tornado.get_advice() == "Find safe room/shelter, shield yourself from debris"

def test_create_f0_LB_in():
    tornado = Tornado("Gerard", 40)
    assert tornado.calculate_classification() == "F0"
    assert tornado.get_advice() == "Find safe room/shelter, shield yourself from debris"

def test_create_f0_UB_in():
    tornado = Tornado("Gerard", 72)
    assert tornado.calculate_classification() == "F0"
    assert tornado.get_advice() == "Find safe room/shelter, shield yourself from debris"

def test_create_f1():
    tornado = Tornado("Hannah", 100)
    assert tornado.calculate_classification() == "F1"
    assert tornado.get_advice() == "Find safe room/shelter, shield yourself from debris"

def test_create_f1_LB_in():
    tornado = Tornado("Hannah", 73)
    assert tornado.calculate_classification() == "F1"
    assert tornado.get_advice() == "Find safe room/shelter, shield yourself from debris"

def test_create_f1_UB_in():
    tornado = Tornado("Hannah", 112)
    assert tornado.calculate_classification() == "F1"
    assert tornado.get_advice() == "Find safe room/shelter, shield yourself from debris"

def test_create_f2():
    tornado = Tornado("Isla", 130)
    assert tornado.calculate_classification() == "F2"
    assert tornado.get_advice() == "Find underground shelter, crouch near to the floor covering your head with your hands"

def test_create_f2_LB_in():
    tornado = Tornado("Isla", 113)
    assert tornado.calculate_classification() == "F2"
    assert tornado.get_advice() == "Find underground shelter, crouch near to the floor covering your head with your hands"

def test_create_f2_UB_in():
    tornado = Tornado("Isla", 157)
    assert tornado.calculate_classification() == "F2"
    assert tornado.get_advice() == "Find underground shelter, crouch near to the floor covering your head with your hands"

def test_create_f3():
    tornado = Tornado("Janna", 160)
    assert tornado.calculate_classification() == "F3"
    assert tornado.get_advice() == "Find underground shelter, crouch near to the floor covering your head with your hands"

def test_create_f3_LB_in():
    tornado = Tornado("Janna", 158)
    assert tornado.calculate_classification() == "F3"
    assert tornado.get_advice() == "Find underground shelter, crouch near to the floor covering your head with your hands"

def test_create_f3_UB_in():
    tornado = Tornado("Janna", 205)
    assert tornado.calculate_classification() == "F3"
    assert tornado.get_advice() == "Find underground shelter, crouch near to the floor covering your head with your hands"

def test_create_f4():
    tornado = Tornado("Kasia", 250)
    assert tornado.calculate_classification() == "F4"
    assert tornado.get_advice() == "Find underground shelter, crouch near to the floor covering your head with your hands"

def test_create_f4_LB_in():
    tornado = Tornado("Kasia", 206)
    assert tornado.calculate_classification() == "F4"
    assert tornado.get_advice() == "Find underground shelter, crouch near to the floor covering your head with your hands"

def test_create_f4_UB_in():
    tornado = Tornado("Kasia", 260)
    assert tornado.calculate_classification() == "F4"
    assert tornado.get_advice() == "Find underground shelter, crouch near to the floor covering your head with your hands"

def test_create_f5():
    tornado = Tornado("Lilith", 4000)
    assert tornado.calculate_classification() == "F5"
    assert tornado.get_advice() == "Find underground shelter, crouch near to the floor covering your head with your hands"

def test_create_f5_LB_in():
    tornado = Tornado("Lilith", 261)
    assert tornado.calculate_classification() == "F5"
    assert tornado.get_advice() == "Find underground shelter, crouch near to the floor covering your head with your hands"

def test_create_unclassified_tornado():
    tornado = Tornado("Marty", 0)
    assert tornado.calculate_classification() == "Unclassified"
    assert tornado.get_advice() == "There is no need to panic"

def test_create_unclassified_tornado_UB_in():
    tornado = Tornado("Marty", 39)
    assert tornado.calculate_classification() == "Unclassified"
    assert tornado.get_advice() == "There is no need to panic"