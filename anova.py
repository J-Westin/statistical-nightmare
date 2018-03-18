import numpy as np
from math import log

from factorial_inputs import bin_fixed_length

def n_params(Y):
    return int(round(log(len(Y), 2)))

def S_T(Y):
    y_bar = sum(Y)/float(len(Y))
    return sum([(y - y_bar)**2. for y in Y])

def S_i(Y, i):
    N = len(Y)
    n = n_params(Y)
    
    y_lo, y_hi = 0., 0.

    for k in range(N):
        bitstring = bin_fixed_length(k, n)
        
        if bitstring[i] == "1":
            y_hi += Y[k]
        elif bitstring[i] == "0":
            y_lo += Y[k]
        else:
            raise ValueError("Invalid digit in bit string.")

    return ((y_hi - y_lo)**2. )/float(N)

def S_i_set(Y):
    return [S_i(Y, i) for i in range(n_params(Y))]

def S_E(Y):
    return S_T(Y) - sum(S_i_set(Y))

def ANOVA(Y, display=True):
    P = np.array(S_i_set(Y))/S_T(Y)

    if display:
        pct = [round(p*100., 2) for p in P]
        for n in range(n_params(Y)):
            print " P_" + str(n), "=", pct[n], "%"
        print

    return P
