
from numpy import *

def lagrange(x, i, X):
    """
    Returns the ith Lagrange basis function, evaluated at x,
    generated by the interpolation points X
    """
    return prod([(x-X[j])/(X[i]-X[j]) for j in range(len(X)) if i != j], axis=0)