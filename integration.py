import numpy as np
import matplotlib.pyplot as plt
from math import sin, cos, tan, pi

def f(x):
    return 5*sin(x)

def trapezium_integration(a, b, num_points):

    dx = (b-a)/num_points
    area = 0.5*f(a) + 0.5*f(b)
    area += sum([f(a+k*dx) for k in range(1, num_points)])
    area *= dx

    return area

def simpsons_integration(a, b, num_points):

    dx = (b-a)/num_points
    area = f(a) + f(b)
    area += 4*sum([f(a+k*dx) for k in range(1, num_points, 2)])
    area += 2*sum([f(a+k*dx) for k in range(2, num_points, 2)])
    area *= (1/3)*dx

    return area



x_min, x_max = 0.0, pi
n_min, n_max = 10, 300
dn = 10
n_values = list(range(n_min, n_max+1, dn))

plt.figure(figsize=(15, 5))

trapezium_results = [trapezium_integration(x_min, x_max, n) for n in n_values]
simpsons_results = [simpsons_integration(x_min, x_max, n) for n in n_values]

trapezium_error = [(10 - val)/10 for val in trapezium_results]
simpsons_error = [(10 - val)/10 for val in simpsons_results]

plt.plot(n_values, trapezium_error)
plt.plot(n_values, simpsons_error)

plt.show()

print(trapezium_results[-1])
print(simpsons_results[-1])

