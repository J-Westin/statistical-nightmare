from random import normalvariate
from b_coefficients import *

def all_choices(inputs, n):
    """Generates all possible subsets of size 'n' from 'inputs'."""
    choices = []

    if n == 0:
        return [[]]

    else:
        for i in range( len(inputs) + 1 - n ):
            other_choices = all_choices(inputs[i+1:], n-1)
            for choice in other_choices:
                choices.append( [inputs[i]] + choice )
        return choices

def inputs_from_indices(all_inputs, indices):
    inputs = []
    for i in indices:
        inputs.append(all_inputs[i])
    return inputs

def product(factors):
    p = 1.
    for f in factors:
        p *= f
    return p

def y_general(inputs, coefficient_function):
    y = 0.
    index_set = range(len(inputs))

    for n in range(len(inputs) + 1):
        all_indices = all_choices(index_set, n)
        
        for term_indices in all_indices:
            x = inputs_from_indices(inputs, term_indices)
            b = coefficient_function(term_indices)

            current_term = product([b] + x)
            y += current_term

    return y

def y1(inputs):
    return y_general(inputs, y1_coefficient)

def y2(inputs):
    return y_general(inputs, y2_coefficient)

def y2_noisy(inputs):
    return y_general(inputs, y2_coefficient) + normalvariate(-0.5, 1.1)
