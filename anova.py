import numpy as np
from math import log

from factorial_inputs import bin_fixed_length
from y_functions import all_choices

def n_params(Y):
    return int(round(log(len(Y), 2)))

def S_T(Y):
    y_bar = sum(Y)/float(len(Y))
    return sum([(y - y_bar)**2. for y in Y])

def S_minmax(Y, indices, bit):
    N = len(Y)
    n = n_params(Y)
    S = 0.

    for k in range(N):
        bitstring = bin_fixed_length(k, n)
        if not bit in [int(bitstring[i]) for i in indices]:
            S += Y[k]

    return S

def S_low(Y, indices):
    return S_minmax(Y, indices, 1)

def S_high(Y, indices):
    return S_minmax(Y, indices, 0)

def S_i(Y, indices):
    factor = 1. / len(Y)
    return factor * ((S_high(Y, indices) - S_low(Y, indices))**2. )

def ANOVA_partial(Y, order, display=False):
    index_inputs = all_choices(range(5), order)
    interaction_set = []
    ST = S_T(Y)
    
    for indices in index_inputs:
        interaction_set.append(S_i(Y, indices)/ST)

    if display:
        pct = [round(S*100., 2) for S in interaction_set]
        for i in range(len(pct)):
            P_name = " P_"
            for index in index_inputs[i]:
                P_name = P_name + str(index)
            print P_name, "=", pct[i], "%"
        print

    return index_inputs, interaction_set

def interaction_contribution(Y, order):
    return sum(ANOVA_partial(Y, order, display=False)[1])

def contribution_summary(Y, max_order=-1, display=True):
    if max_order == -1:
        max_order = n_params(Y)

    contributions = [interaction_contribution(Y, order) for order in range(1, max_order+1)]

    if display:
        order = 1
        for contrib in contributions:
            print " Order", order, "contribution:", round(contrib*100., 2), "%"
            order += 1

    return contributions

def ANOVA_full(Y, display=False):
    index_inputs = []
    interaction_set = []

    for order in range(1, n_params(Y) + 1):
        i, S_i = ANOVA_partial(Y, order, display=display)
        index_inputs = index_inputs + i
        interaction_set = interaction_set + S_i

    return index_inputs, interaction_set

def S_E(Y):
    return S_T(Y) - sum(ANOVA_full(Y, display=False)[1])
