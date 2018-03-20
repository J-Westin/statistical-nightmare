import numpy as np
import matplotlib.pyplot as plt

from assignment_number import asmt
from factorial_inputs import *
from anova import *
from y_functions import y1, y2, y2_noisy
from gradient_lines import *

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

out_y1       = evaluate_factorial_design(param_limits, y1)
latex_output_table(out_y1)
print
latex_interaction_table(out_y1)
print

out_y2       = evaluate_factorial_design(param_limits, y2)
latex_output_table(out_y2)
print
latex_interaction_table(out_y2, max_order=2)
print

plt.subplot(121)
plt.title("Linear Terms")
for indices in all_choices(range(5), 1):
    plot_normalized_gradient(out_y2, indices)
plt.xlabel("<-- x_min      x_max -->")
plt.ylabel("Average $S_i^-$ and $S_i^+$")

plt.subplot(122)
plt.title("Two-Term Interactions")
term_legend(2)
for indices in all_choices(range(5), 2):
    plot_normalized_gradient(out_y2, indices)
plt.xlabel("<-- x_min      x_max -->")
plt.ylabel("Average $S_{ij}^-$ and $S_{ij}^+$")

plt.show()

out_y2_noisy = evaluate_factorial_design(param_limits, y2_noisy)
latex_output_table(out_y2_noisy)
print
latex_interaction_table(out_y2_noisy, max_order=2)


##dummy = raw_input("Press ENTER")
