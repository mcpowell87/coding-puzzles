import pytest
from ctci.arrays_and_strings.string_compression import compress

def test_case_1():
    assert(compress("aabcccccaaa") == "a2b1c5a3")

def test_case_2():
    assert(compress("aaaaaaaa") == "a8")

def test_case_3():
    assert(compress("abcdef") == "abcdef")