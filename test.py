import numpy as np
from main import generate_normal_array

def test_generate_normal_array():
    result = generate_normal_array((2, 3), mean=0, std_dev=1)
    assert result.shape == (2, 3), "Array shape mismatch"
    assert np.abs(np.mean(result)) < 1, "Mean is not approximately 0"
    assert np.abs(np.std(result) - 1) < 1, "Standard deviation is not approximately 1"
    print("test_generate_normal_array passed!")

    def test_solving_Cramer_rule():
        coeff_matrix = np.array([[2, -1, 5], [1, 1, -3], [3, 2, 4]])
    const_matrix = np.array([5, 1, 6])
    result = solve_cramers_rule(coeff_matrix, const_matrix)
    expected = [1, -1, 2]
    assert np.allclose(result, expected), f"Expected {expected}, got {result}"

    # Test with a singular matrix
    singular_matrix = np.array([[1, 1], [2, 2]])
    try:
        solve_cramers_rule(singular_matrix, np.array([3, 6]))
    except ValueError as e:
        assert str(e) == "The coefficient matrix is singular, and the system cannot be solved."
    else:
        assert False, "Expected ValueError for singular matrix"
    print("test_solve_cramers_rule passed!")