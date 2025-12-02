import numpy as np
from scipy.sparse import diags

def qadmon_operator(N, gamma_star=np.sqrt(np.pi/3)):
    phi = (1 + np.sqrt(5)) / 2
    idx = np.arange(N)
    diag = np.mod(idx * phi, 1.0)
    off = gamma_star * np.ones(N - 1)
    H = diags([diag, off, off], [0, -1, 1], format="csr")
    return H
