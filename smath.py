import numpy as np

def V(*args):
    """Shorthand for a vector. Wrapper around
       numpy.array. Works on 1-d arrays with
       individual arguments, or on nd-arrays
       with iterable arguments as axes.
    """
    return np.array(args)

