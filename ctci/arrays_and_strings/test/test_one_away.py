import pytest
from ctci.arrays_and_strings.one_away import one_away

def test_case_1():
    assert(one_away("pale", "ple"))

def test_case_2():
    assert(one_away("pales", "pale"))

def test_case_3():
    assert(one_away("pale", "bale"))

def test_case_4():
    assert(not one_away("pale", "bake"))