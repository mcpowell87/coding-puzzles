import pytest
from ctci.arrays_and_strings.rotate_matrix import rotate_left, rotate_right

# Rotate right
def test_case_1():
    assert(rotate_right([[1,2,3,4],[3,4,5,3],[5,4,3,2],[4,3,1,1]]) == [[4,5,3,1],[3,4,4,2],[1,3,5,3],[1,2,3,4]])

# Rotate left
def test_case_2():
     assert(rotate_left([[1,2,3,4],[3,4,5,3],[5,4,3,2],[4,3,1,1]]) == [[4,3,2,1],[3,5,3,1],[2,4,4,3],[1,3,5,4]])

# Rotate right 4 times
def test_case_3():
    rotate = rotate_right([[1,2,3,4],[3,4,5,3],[5,4,3,2],[4,3,1,1]])
    rotate = rotate_right(rotate)
    rotate = rotate_right(rotate)
    rotate = rotate_right(rotate)
    assert(rotate == [[1,2,3,4],[3,4,5,3],[5,4,3,2],[4,3,1,1]])

# Rotate left 4 times
def test_case_4():
    rotate = rotate_left([[1,2,3,4],[3,4,5,3],[5,4,3,2],[4,3,1,1]])
    rotate = rotate_left(rotate)
    rotate = rotate_left(rotate)
    rotate = rotate_left(rotate)
    assert(rotate == [[1,2,3,4],[3,4,5,3],[5,4,3,2],[4,3,1,1]])

# Rotate left then right
def test_case_4():
    rotate = rotate_left([[1,2,3,4],[3,4,5,3],[5,4,3,2],[4,3,1,1]])
    rotate = rotate_right(rotate)
    assert(rotate == [[1,2,3,4],[3,4,5,3],[5,4,3,2],[4,3,1,1]])

# Rotate right then left
def test_case_5():
    rotate = rotate_right([[1,2,3,4],[3,4,5,3],[5,4,3,2],[4,3,1,1]])
    rotate = rotate_left(rotate)
    assert(rotate == [[1,2,3,4],[3,4,5,3],[5,4,3,2],[4,3,1,1]])