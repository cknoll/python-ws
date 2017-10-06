

import numpy as np
import scipy as sc
from matplotlib import pyplot as plt

from ipydex import IPS

# adapted from source: http://www.scipy.org/Cookbook/LinearRegression


#####################################################

# Regression

#####################################################




# Linear regression example
# This is a very simple example of using two scipy tools 
# for linear regression, polyfit and stats.linregress

# Sample data creation
# number of points 
n = 10
t = np.linspace(-5, 5, n)
# parameters
a, b, c, = 0.02, 0.8, -1
x = sc.polyval([a, b, c], t) # see polyval-docstring

np.random.seed(6)
# add some noise
x_noise = x + 0.4*sc.randn(n)

# Linear regression -polyfit - polyfit can be used other orders polys
(ar, br) = sc.polyfit(t,x_noise,1)
xr = sc.polyval([ar,br],t)

# Quadratische Regression:
q2, q1, q0 = sc.polyfit(t, x_noise, 2)
xqr = sc.polyval([q2, q1, q0],t)


# image size expected in inch -> convert
mm = 1./25.4 #mm to inch
fs = [90*mm, 60*mm]
plt.figure(figsize=fs) # user-defined size
plt.ylim(-5.1, 5.1)

plt.plot(t, x_noise, 'ro') # data
plt.savefig('bsp3_1.pdf')
plt.plot(t, xr, lw=2) # lw = linewidth
plt.savefig('bsp3_2.pdf')
plt.plot(t, xqr, lw=2)
plt.savefig('bsp3_3.pdf')


#####################################################

#Interpolation

#####################################################



# see also: http://docs.scipy.org/doc/scipy/reference/tutorial/interpolate.html


# for didactic purpose this import is not located at the beginning

from scipy.interpolate import interp1d

func1 = interp1d(t, x_noise) # kind = 'linear' is default
func0 = interp1d(t, x_noise, kind='nearest') # order 0 is 'nearest' (neighbor)
func3 = interp1d(t, x_noise, kind=3) # cubic spline

t_highres = np.linspace(t[0], t[-1], 100)

xi0 = func0(t_highres)
xi1 = func1(t_highres)
xi3 = func3(t_highres)

# plot
# new figure
plt.figure(figsize=fs) # user-defined image size
plt.ylim(-5.1, 5.1)

plt.plot(t, x_noise, 'ro',) # data
plt.plot(t_highres, xi0, 'bo', ms = 2)
plt.savefig('bsp3_4.pdf')
plt.plot(t_highres, xi1, 'g', lw = 1.3)
plt.savefig('bsp3_5.pdf')
plt.plot(t_highres, xi3, 'k-', lw = 2)
plt.savefig('bsp3_6.pdf')


#####################################################

# "Smoothing Spline"
#http://www.scipy.org/Cookbook/Interpolation

#####################################################




from scipy.interpolate import splrep, splev
# spline parameters
s = 0.4 # smoothness parameter
k = 2 # spline order
nest = -1 # estimate of number of knots needed (-1 = maximal)

tck = splrep(t, x_noise,s=s,k=k)

tck2 = splrep(t, x_noise,s=0.0,k=k)

# evaluate spline, including interpolated points
t_highres = np.linspace(t[0],t[-1],100)
xspline = splev(t_highres,tck)

xspline2 = splev(t_highres,tck2)

# plot
# new figure
plt.figure(figsize=fs) # user-defined image size
plt.ylim(-5.1, 5.1)

plt.plot(t, x_noise, 'ro') # data
plt.plot(t_highres, xspline, lw = 1.5)
plt.savefig('bsp3_7.pdf')
plt.plot(t_highres, xspline2, 'g--', lw = 2)
plt.savefig('bsp3_8.pdf')

plt.show()
