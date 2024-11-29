import numpy as np

def test_generate_normal_array():
    result = generate_normal_array((2, 3), mean=0, std_dev=1)
    assert result.shape == (2, 3), "Array shape mismatch"
    assert np.abs(np.mean(result)) < 1, "Mean is not approximately 0"
    assert np.abs(np.std(result) - 1) < 1, "Standard deviation is not approximately 1"
    print("test_generate_normal_array passed!")