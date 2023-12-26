import numpy as np
import matplotlib.pyplot as plt
from math import sin, cos, pi

def f(x):
    return sin(x**4 - 2*x + 1)+cos(x**3)

def integrate(x_min, x_max, num_points):

    dx = (x_max-x_min)/num_points

    x_vals = [x_min+k*dx for k in range(num_points+1)]
    y_vals = [f(x) for x in x_vals]

    area = 0.5*f(x_min) + 0.5*f(x_max) + sum(y_vals[1:])
    area *= dx

    return area, x_vals, y_vals

x_min = 0.0
x_max = 1.0
num_points_integrate = 10
num_points_plot = 10_000

plt.figure(figsize=(15, 5))

x_plot = np.linspace(x_min, x_max, num_points_plot)
y_plot = [f(x) for x in x_plot]
plt.plot(x_plot, y_plot, c = 'blue')  

area, x_vals, y_vals = integrate(x_min, x_max, num_points_integrate)
plt.plot(x_vals, y_vals, c = 'orange')
plt.scatter(x_vals, y_vals, c = 'orange')
plt.show()

print(area)

