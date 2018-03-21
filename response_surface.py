import numpy as np
from factorial_inputs import dollar, random_input_set
from anova import all_choices

def X_line(inputs):
    line = [1.] + list(inputs)
    for pair in all_choices(inputs, 2):
        line.append(pair[0]*pair[1])

    return np.array(line)

def X_matrix(input_set):
    lines = [X_line(inputs) for inputs in input_set]
    return np.matrix(np.vstack(tuple(lines)))

def response_surface_coefficients(input_set, y_function):
    X = X_matrix(input_set)
    Y = np.matrix([y_function(inputs) for inputs in input_set]).T

    U, S, V = np.linalg.svd(X, full_matrices=0)
    U, S, V = np.mat(U), np.mat(np.diag(S)), np.mat(V)
    X_plus = V.T * S.I * U.T

    B = X_plus * Y
    return np.array(B.T)[0]

def latex_coefficient_table(input_set, y_function):
    cft = response_surface_coefficients(input_set, y_function)
    lines = [" & "] * 5
    lines[0] = dollar("b_0 = " + str(round(cft[0], 2))) + lines[0]

    for i in range(1, 6):
        b_value = str(round(cft[i],2))
        lines[i-1] = lines[i-1] + dollar("b_" + str(i) + " = " + b_value) + " & "

    indices = all_choices(range(5), 2)

    for i in range(6, len(cft)):
        pair = indices[i-6]
        name = "b_{" + str(pair[0]+1) + str(pair[1]+1) + "} = "
        line_nr = pair[1]
        lines[line_nr] = lines[line_nr] + dollar(name + str(round(cft[i],2))) + " & "

    for i in range(4):
        lines[3-i] = lines[3-i] + "&"*i + "\\\\"
    lines[4] = lines[4][:-3] + "\\\\"

    print "Constant & Linear & \\multicolumn{4}{c}{Two-term} \\\\ \\hline"
    for line in lines:
        print line

def compact_coefficient_table(input_set, y_function):
    cft = response_surface_coefficients(input_set, y_function)
    lines = [" & "] * 5
    lines[0] = dollar("b_0 = " + str(round(cft[0], 2))) + lines[0]

    for i in range(1, 6):
        b_value = str(round(cft[i],2))
        lines[i-1] = lines[i-1] + dollar("b_" + str(i) + " = " + b_value) + " & "

    sigma_bij = np.linalg.norm(np.array(cft[6:]) - 0.25)
    lines[0] = lines[0] + dollar("\\sigma(b_{ij}) = " + str(round(sigma_bij, 2)))
    for i in range(len(lines)):
        lines[i] = lines[i] + " \\\\"
    
    print "Constant & Linear & Two-term (Deviation from 0.25) \\\\ \\hline"
    for line in lines:
        print line



def monty_table(minmax_settings, number, y_function):
    input_set = random_input_set(minmax_settings, number)
    compact_coefficient_table(input_set, y_function)
