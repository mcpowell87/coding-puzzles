import pytest
from ctci.arrays_and_strings.check_permutation import check_permutation

def test_case_1():
    assert(check_permutation("hello", "olehl"))
    
def test_case_2():
    assert(not check_permutation("hello", "goodbye"))

def test_case_3():
    assert(check_permutation("321", "123"))

def test_case_4():
    assert(not check_permutation("a", "b"))