from assignment_number import asmt

if asmt == 1:
    cft = [ 2., 3., 2., -1., 1., .3, .4, -.3, .2, -.1]

if asmt == 2:
    cft = [ 2., -1.5, -2., 1.3, 1.8, -.7, -.3, .5, .18, -.2]

if asmt == 3:
    cft = [-7., 4., -.14, 1.8, 1.3, -1.7, .25, .45, -.28, .2]

def y1_coefficient(indices):
    n = len(indices)

    if n == 0:
        return cft[0]
    elif n == 1:
        b_i = cft[1:6]
        return b_i[indices[0]]
    elif n == 2:
        return cft[6]
    elif n == 3:
        return cft[7]
    elif n == 4:
        return cft[8]
    elif n == 5:
        return cft[9]
    else:
        raise ValueError("Too many factor indices provided.")


##def y1_coefficient(indices):
##    n = len(indices)
##
##    if n == 0:
##        return -7.
##    elif n == 1:
##        b_i = [4, -.14, 1.8, 1.3, -1.7]
##        return b_i[indices[0]]
##    elif n == 2:
##        return 0.25
##    elif n == 3:
##        return 0.45
##    elif n == 4:
##        return -0.28
##    elif n == 5:
##        return 0.2
##    else:
##        raise ValueError("Too many factor indices provided.")

def y2_coefficient(indices):
    n = len(indices)

    if n in [3, 4, 5]:
        return 0.
    else:
        return y1_coefficient(indices)
