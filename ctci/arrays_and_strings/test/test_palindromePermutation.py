import pytest
from ctci.arrays_and_strings.palindromePermutation import is_palindrome_permutation

def test_case_example():
    assert(is_palindrome_permutation("Tact Coa"))

def test_case_2():
    assert(not is_palindrome_permutation("happy"))

def test_case_3():
    assert(is_palindrome_permutation("A nut for a jar of tuna"))

def test_case_4():
    assert(is_palindrome_permutation(""))

def test_case_5():
    assert(is_palindrome_permutation("a"))

def test_case_6():
    assert(is_palindrome_permutation("Ta31ct Co223a"))

def test_case_7():
    assert(is_palindrome_permutation("definitely not a palindrome"))

def test_case_8():
    assert(is_palindrome_permutation("lol"))

def test_case_9():
    assert(is_palindrome_permutation("aaaaaab"))

def test_case_10():
    assert(not is_palindrome_permutation("aaaaaaab"))