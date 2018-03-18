import numpy as np

from assignment_number import asmt
from factorial_inputs import evaluate_factorial_design
from anova import ANOVA
from y_functions import y1, y2, y2_noisy

if asmt == 1:
    param_limits = [[-2.5,  2.0],
                    [-3.0, -2.0],
                    [-0.5,  1.5],
                    [-1.0,  1.0],
                    [-2.0,  2.1]]

if asmt == 3:
    param_limits = [[-3.5, 2.5],
                    [-1.4, 1.1],
                    [-2.4, 2.6],
                    [-1.9, 1.8],
                    [ 0.9, 3.1]]

out_y1       = evaluate_factorial_design(param_limits, y1)
out_y2       = evaluate_factorial_design(param_limits, y2)
out_y2_noisy = evaluate_factorial_design(param_limits, y2_noisy)

var_y1       = ANOVA(out_y1)
var_y2       = ANOVA(out_y2)
var_y2_noisy = ANOVA(out_y2_noisy)
