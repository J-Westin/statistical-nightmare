import numpy as np
from math import log

def bin_fixed_length(n, length):
    """
    Converts an integer 'n' to a binary string of length 'length'.
    """
    nb = bin(n)[2:]
    if len(nb) > length:
        raise ValueError("Binary representation too long")

    while len(nb) < length:
        nb = "0" + nb

    return nb

def bin_to_plusminus(bitstring):
    """
    Converts a string of bits (e.g. "01011") to a string of comma-separated
    plusses and minuses (e.g. "-,+,-,+,+").
    """
    s = ""
    for bit in list(bitstring):
        if int(bit):
            s = s + "+,"
        else:
            s = s + "-,"
    return s[:-1]

def generate_inputs(minmax_settings, bitstring):
    """
    Generates a parameter set, where each parameter is chosen from two possible values.
    """
    inputs = []
    for i in range(len(bitstring)):
        inputs.append(minmax_settings[i][int(bitstring[i])])

    return inputs

def factorial_input_set(minmax_settings):
    """
    Generates a set of all possible input settings selected from two values.
    """
    n_params = len(minmax_settings)
    input_set = []
    for k in range(2**n_params):
        kb = bin_fixed_length(k, n_params)
        input_set.append(generate_inputs(minmax_settings, kb))

    return np.array(input_set)

def evaluate_factorial_design(minmax_inputs, y):
    """
    Evaluates the factorial design for a given function y.
    """
    factorial_inputs = factorial_input_set(minmax_inputs)
    outputs = []

    for inputs in factorial_inputs:
        outputs.append( y(inputs) )

    return np.array(outputs)

def dollar(string):
    return "$" + string + "$"

def latex_output_table(Y):
    N = len(Y)
    n = int(round(log(N, 2)))

    line = ""
    line_columns = 0
    
    for k in range(N):
        inputs = dollar(bin_to_plusminus(bin_fixed_length(k, n)))
        output = dollar(str(round(Y[k], 2)))

        line = line + inputs + " & " + output + " & "
        line_columns += 1

        if line_columns == 4:
            print line[:-3] + "\\\\"
            line = ""
            line_columns = 0

    return
            
        
