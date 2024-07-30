import numpy as np
import matplotlib.pyplot as plt

N = 20
x = np.linspace(0, 2 * np.pi, N, endpoint=False)
dx = 2 * np.pi / N

# Numerical derivative using the given formula
f_numerical = (np.sin(np.roll(x, -1)) - np.sin(x)) / dx

# Plotting
plt.plot(x, np.cos(x), 'r', label='Analytical derivative')
plt.plot(x, f_numerical, 'bo', label='Numerical derivative')
plt.xlabel('x')
plt.ylabel('f\'(x)')
plt.title('Numerical vs Analytical Derivative (First Order)')
plt.legend()
plt.show()


# b

def deriv_2nd(x, dx):
    return (np.sin(np.roll(x, -1)) - np.sin(np.roll(x, 1))) / (2 * dx)

def deriv_4th(x, dx):
    return (-np.sin(np.roll(x, 2)) + 8*np.sin(np.roll(x, 1)) - 8*np.sin(np.roll(x, -1)) + np.sin(np.roll(x, -2))) / (12 * dx)

# Numerical derivatives
f_numerical_2nd = deriv_2nd(x, dx)
f_numerical_4th = deriv_4th(x, dx)

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(x, np.cos(x), 'r', label='Analytical derivative')
plt.plot(x, f_numerical, 'bo', label='First order derivative')
plt.plot(x, f_numerical_2nd, 'g+', label='Second order derivative')
plt.plot(x, f_numerical_4th, 'ms', label='Fourth order derivative')
plt.xlabel('x')
plt.ylabel('f\'(x)')
plt.title('Numerical vs Analytical Derivative (Higher Order)')
plt.legend()
plt.show()
