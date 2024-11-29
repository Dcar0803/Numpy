import numpy as np

def generate_normal_array(shape,mean,std_dev):

    """Generate a NumPy array with a specified shape, filled with normally distributed numbers having a given mean and standard deviation.

    Parameters: 

        shape(tuple): The shape of the array
        mean(float): The mean of the normal distribution.
        std_dev(float): The standard deviatoin of the nromal distribution.
    
    Returns:
        np.ndarray: Array of normally distributed numbers 
    """

    return np.random.normal(loc= mean, scale=std_dev,size = shape)

def solve_ccramers_rule(coeff_matrix, const_matrix):
     det_coeff = np.linalg.det(coeff_matrix)
     if det_coeff == 0:
        raise ValueError("The coefficient matrix is singular, and the system cannot be solved.")
     
     solutions = []
     for i in range(coeff_matrix.shape[1]):
        temp_matrix = coeff_matrix.copy()
        temp_matrix[:, i] = const_matrix
        solutions.append(np.linalg.det(temp_matrix) / det_coeff)
     return solutions