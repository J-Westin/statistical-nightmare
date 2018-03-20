import matplotlib.pyplot as plt

from anova import S_low, S_high, n_params

cols = "k", "b", "r", "g", "y"
lnwide = 3

def n_terms(Y, indices):
    n = n_params(Y)
    n_others = n - len(indices)
    return 2**n_others

def toppo(Y, indices):
    N = n_terms(Y, indices)
    S = S_high(Y, indices)
    return S/float(N)

def botto(Y, indices):
    N = n_terms(Y, indices)
    S = S_low(Y, indices)
    return S/float(N)

def normalized_gradient(Y, indices):
    return toppo(Y, indices) - botto(Y, indices)

def plot_normalized_gradient(Y, indices):
    c1 = cols[indices[0]]
    
    X = [-1, 1]
    Y = [botto(Y, indices), toppo(Y, indices)]
    plt.plot(X, Y, c1+"-", linewidth=lnwide)
    if len(indices) == 2:
        c2 = cols[indices[1]]
        plt.plot(X, Y, c2+"--", linewidth=lnwide)

def term_legend(location):
    for index in range(5):
        plt.plot([],[], cols[index], linewidth=lnwide, label="$x_" + str(index+1) + "$")
    plt.legend(loc=location)
