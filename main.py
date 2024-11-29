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