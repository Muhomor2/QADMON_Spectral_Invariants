from qadmon_operator import qadmon_operator
from scipy.sparse.linalg import eigsh

def fibonacci(n):
    F = [1,1]
    for _ in range(n-2):
        F.append(F[-1]+F[-2])
    return F

def resonance_test(N=50000, depth=15):
    phi = (1 + 5**0.5)/2
    H = qadmon_operator(N)
    F = fibonacci(depth)
    results = []
    for k in range(2, depth):
        lam = eigsh(H, k=1, which='LM', return_eigenvectors=False)[0]
        results.append((F[k], lam, lam/(phi**F[k])))
    return results
