import numpy as np
from math import log

from factorial_inputs import bin_fixed_length, dollar
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

def P_i(Y, indices, percent=False):
    if percent: factor = 100.
    else: factor = 1.
    return factor * S_i(Y, indices)/S_T(Y)

def ANOVA_partial(Y, order, display=False):
    index_inputs = all_choices(range(5), order)
    interaction_set = [P_i(Y, indices) for indices in index_inputs]

    if display:
        pct = [round(S*100., 2) for S in interaction_set]
        for i in range(len(pct)):
            P_name = " P_"
            for index in index_inputs[i]:
                P_name = P_name + str(index+1)
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

def S_E(Y, percent=True):
    error = 1. - sum(ANOVA_full(Y, display=False)[1])
    if percent: return error*100.
    else: return error

def latex_interaction(Y, indices, percent=True):
    name = "P_{"
    for i in indices:
        name = name + str(i+1)
    name = name + "}"
    value = P_i(Y, indices, percent=percent)
    if percent:
        bonus = "\\ \\%"
    else:
        bonus = ""
    
    return dollar(name + " = " + str(round(value, 2)) + bonus)

def latex_interaction_table(Y, max_order=-1):
    n = n_params(Y)
    orders = range(1, n+1)

    if max_order == -1:
        columns = orders
    else:
        columns = range(1, max_order+1)
    
    index_city = [all_choices(range(n), column) for column in columns]
    longest = max([len(indices) for indices in index_city])

    for i in range(longest):
        line = " & "
        for column in columns:
            try:
                indices = index_city[column-1][i]
                line = line + latex_interaction(Y, indices, percent=True) + " & "
            except IndexError:
                line = line + "$-$ & "
        print line[:-3] + "\\\\"

    print "\\hline"
    last_line = "Total & "

    for column in columns:
        contribution = interaction_contribution(Y, column)*100.
        last_line = last_line + dollar(str(round(contribution, 2)) + "\\ \\%") + " & "

    print last_line[:-3] + "\\\\"
    
    return
