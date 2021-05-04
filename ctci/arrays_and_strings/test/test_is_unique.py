import pytest
from ctci.arrays_and_strings.is_unique import is_unique

def test_case_1():
    assert(not is_unique("hello"))
    
def test_case_2():
    assert(is_unique("abcdef"))

def test_case_3():
    assert(not is_unique("abc12344"))

def test_case_4():
    assert(is_unique("abc12345 "))