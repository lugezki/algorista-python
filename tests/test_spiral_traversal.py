# test_spiral_traversal.py
from spiral_traversal import spiral_traverse
    
def test_spiral_traverse_3x3():
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    expected_output = [1, 2, 3, 6, 9, 8, 7, 4, 5]
    result = spiral_traverse(matrix)
    assert result == expected_output

def test_spiral_traverse_empty():
    matrix = []
    expected_output = []
    assert spiral_traverse(matrix) == expected_output

def test_spiral_traverse_single_element():
    matrix = [[42]]
    expected_output = [42]
    assert spiral_traverse(matrix) == expected_output

def test_spiral_traverse_single_row():
    matrix = [[1, 2, 3, 4]]
    expected_output = [1, 2, 3, 4]
    assert spiral_traverse(matrix) == expected_output

def test_spiral_traverse_single_column():
    matrix = [
        [1],
        [2],
        [3],
        [4]
    ]
    expected_output = [1, 2, 3, 4]
    assert spiral_traverse(matrix) == expected_output

def test_spiral_traverse_rectangular_more_rows():
    matrix = [
        [1, 2],
        [3, 4],
        [5, 6]
    ]
    expected_output = [1, 2, 4, 6, 5, 3]
    assert spiral_traverse(matrix) == expected_output

def test_spiral_traverse_rectangular_more_cols():
    matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8]
    ]
    expected_output = [1, 2, 3, 4, 8, 7, 6, 5]
    assert spiral_traverse(matrix) == expected_output, "Values are not matching"