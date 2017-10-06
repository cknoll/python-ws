from scipy.integrate import odeint
import numpy as np
def rhs(z,t):
    """ rhs = right hand side [function] """
    z1, z2  = z # unpacking state
    z1_dot = z2
    z2_dot = 0.9*(1-z1**2)*z2  - z1
    return [z1_dot, z2_dot]

tt = np.arange(0, 100,.01) # 100s dt = 0.1
z0 = [3, 0]   # initial state for [z1, z2]
zz = odeint(rhs, z0, tt) # call integration algorithm

from matplotlib import pyplot as plt

plt.plot(zz[:, 0], zz[:, 1])
plt.show()
