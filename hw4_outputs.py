import numpy as np
import matplotlib.pyplot as plt

from assignment_number import asmt
from factorial_inputs import *
from anova import *
from y_functions import y1, y2, y2_noisy
from gradient_lines import *
from response_surface import *

if asmt == 1:
    param_limits = [[-2.5,  2.0],
                    [-3.0, -2.0],
                    [-0.5,  1.5],
                    [-1.0,  1.0],
                    [-2.0,  2.1]]

if asmt == 2:
    param_limits = [[-3.0, -2.0],
                    [-1.0,  2.0],
                    [ 1.5,  2.5],
                    [-2.0,  2.0],
                    [-1.8,  1.0]]

if asmt == 3:
    param_limits = [[-3.5, 2.5],
                    [-1.4, 1.1],
                    [-2.4, 2.6],
                    [-1.9, 1.8],
                    [ 0.9, 3.1]]


#### ~~~ Uncomment blocks and run the script to generate outputs ~~~ ####

#### FACTORIAL DESIGN FOR Y1

out_y1       = evaluate_factorial_design(param_limits, y1)
##latex_output_table(out_y1)
##print
##latex_interaction_table(out_y1)
##print

#### FACTORIAL DESIGN FOR Y2

out_y2       = evaluate_factorial_design(param_limits, y2)
##latex_output_table(out_y2)
##print
##latex_interaction_table(out_y2, max_order=2)
##print

#### GRADIENT LINES

##plt.subplot(121)
##plt.title("Linear Terms")
##for indices in all_choices(range(5), 1):
##    plot_normalized_gradient(out_y2, indices)
##plt.xlabel("<-- x_min      x_max -->")
##plt.ylabel("Average $S_i^-$ and $S_i^+$")
##
##plt.subplot(122)
##plt.title("Two-Term Interactions")
##term_legend(2)
##for indices in all_choices(range(5), 2):
##    plot_normalized_gradient(out_y2, indices)
##plt.xlabel("<-- x_min      x_max -->")
##plt.ylabel("Average $S_{ij}^-$ and $S_{ij}^+$")
##
##plt.show()

#### FACTORIAL DESIGN FOR NOISY Y2

out_y2_noisy = evaluate_factorial_design(param_limits, y2_noisy)
##latex_output_table(out_y2_noisy)
##print
##latex_interaction_table(out_y2_noisy, max_order=2)

#### RESPONSE SURFACE VERIFICATION WITH NOISELESS Y2

input_set = factorial_input_set(param_limits)
##print response_surface_coefficients(input_set, y2)

#### RESPONSE SURFACE FOR NOISY Y2

##latex_coefficient_table(input_set, y2_noisy)
##print

#### RESPONSE SURFACES FOR MONTE CARLO EXPERIMENTS

##for xp in range(4):
##    N = 16*10**xp
##    monty_table(param_limits, N, y2_noisy)
##    print
