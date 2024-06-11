import pyswarms as ps
from pyswarms.utils.functions import single_obj as fx
from pyswarms.utils.plotters import plot_cost_history
import matplotlib.pyplot as plt
import math
import numpy as np


def endurance(args):
    x, y, z, u, v, w = args
    return math.exp(-2*(y-math.sin(x))**2)+math.sin(z*u)+math.cos(v*w)


x_max = np.ones(6)
x_min = np.zeros(6)
my_bounds = (x_min, x_max)


def f(swarms):
    n_particles = swarms.shape[0]
    j = np.zeros(n_particles)
    for i in range(n_particles):
        j[i] = endurance(swarms[i])
    return -j



options = {'c1': 0.5, 'c2': 0.3, 'w':0.9}
optimizer = ps.single.GlobalBestPSO(n_particles=10, dimensions=6,
options=options, bounds=my_bounds)
optimizer.optimize(f, iters=1000)

plot_cost_history(cost_history=optimizer.cost_history)
plt.show()
