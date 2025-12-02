import numpy as np
from qadmon_operator import qadmon_operator
from scipy.sparse.linalg import eigsh

phi = (1 + np.sqrt(5))/2

def compute_kappa(N=100000):
    H = qadmon_operator(N)
    lam = eigsh(H, k=1, which='LM', return_eigenvectors=False)[0]
    return lam / phi**N
