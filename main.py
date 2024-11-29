import numpy as np

def generate_normal_array(shape,mean,std_dev):

    return np.normal(loc= mean, scale=std_dev,size = shape)