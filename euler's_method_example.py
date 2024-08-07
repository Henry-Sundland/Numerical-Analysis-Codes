import numpy as np
import matplotlib.pyplot as plt

# Define the ODE as a function
def f(t, y):
    return -2 * y

# Euler's method implementation
def euler_method(f, t0, y0, h, num_steps):
    t_values = np.zeros(num_steps + 1)
    y_values = np.zeros(num_steps + 1)
    
    t_values[0] = t0
    y_values[0] = y0
    
    for i in range(num_steps):
        y_values[i + 1] = y_values[i] + h * f(t_values[i], y_values[i])
        t_values[i + 1] = t_values[i] + h
    
    return t_values, y_values

# Initial conditions
t0 = 0
y0 = 1
h = 0.01
num_steps = int(2 / h)

# Solve the ODE using Euler's method
t_values, y_values = euler_method(f, t0, y0, h, num_steps)

# Analytical solution for comparison
t_analytical = np.linspace(0, 2, 100)
y_analytical = np.exp(-2 * t_analytical)

# Plot the results
plt.plot(t_values, y_values, 'o-', label="Euler's Method")
plt.plot(t_analytical, y_analytical, '-', label="Analytical Solution")
plt.xlabel('t')
plt.ylabel('y')
plt.title("Solving ODE using Euler's Method")
plt.legend()
plt.grid(True)
plt.show()
