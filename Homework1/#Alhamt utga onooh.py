#Alhamt utga onooh

import numpy as np
import pandas as pd

def calc_F(A, K, L):
    return A*(K**0.3)*(L**0.7)

A_utga = np.arange(1, 10.1, 0.1)
K_utga = np.arange(1, 10.1, 0.1)
L_utga = np.arange(1, 10.1, 0.1)

results =[]

for A in A_utga:
    for K in K_utga:
        for L in L_utga:
            F = calc_F(A, K, L)
            results.append((A, K, L, F))

df = pd.DataFrame(results, columns=["A", "K", "L", "F"])

print(df)


