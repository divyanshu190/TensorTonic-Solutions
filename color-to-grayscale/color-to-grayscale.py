import numpy as np
def color_to_grayscale(image):
    """
    Convert an RGB image to grayscale using luminance weights.
    """
    # Write code here
    image = np.array(image, dtype = float)
    temp = np.array([0.299, 0.587, 0.114])
    return (image @ temp).tolist()