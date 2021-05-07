import pytest
from ctci.arrays_and_strings.zero_matrix import zero_matrix

def test_case_1():
    assert(zero_matrix([[1,2,3,4],[3,4,5,3],[5,4,3,2],[4,3,1,1]]) == [[1,2,3,4],[3,4,5,3],[5,4,3,2],[4,3,1,1]])

def test_case_2():
    assert(zero_matrix([[1,2,3,4],[3,4,5,3],[5,4,3,2],[4,3,0,1]]) == [[1,2,0,4],[3,4,0,3],[5,4,0,2],[0,0,0,0]])

def test_case_1():
    assert(zero_matrix([[1,2,3,4],[3,4,5,3],[5,4,3,2],[0,0,0,0]]) == [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]])