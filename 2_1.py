import numpy as np
import matplotlib.pyplot as plt

N = 20
x = np.linspace(0, 2 * np.pi, N, endpoint=False)
dx = 2 * np.pi / N

# Numerical derivative using the given formula
f_x = np.sin(x)
f_prime_numerical = (np.roll(f_x, -1) - f_x) / dx
f_prime_numerical = (np.sin(np.roll(x, -1)) - np.sin(x)) / dx
f_prime_analytical = np.cos(x)


# Plotting
plt.plot(x, f_prime_analytical, 'r', label='Analytical derivative')
plt.plot(x, f_numerical, 'bo', label='Numerical derivative')
plt.xlabel('x')
plt.ylabel('f\'(x)')
plt.title('Numerical vs Analytical Derivative (First Order)')
plt.legend()
plt.show()


# b
# Second-order finite difference coefficients
def second_order_finite_difference(f_x, dx):
    return (np.roll(f_x, -1) - np.roll(f_x, 1)) / (2 * dx)

# Fourth-order finite difference coefficients
def fourth_order_finite_difference(f_x, dx):
    return (-np.roll(f_x, 2) + 8 * np.roll(f_x, 1) - 8 * np.roll(f_x, -1) + np.roll(f_x, -2)) / (12 * dx)

# Sixth-order finite difference coefficients
def sixth_order_finite_difference(f_x, dx):
    return (np.roll(f_x, 3) - 9 * np.roll(f_x, 2) + 45 * np.roll(f_x, 1) - 45 * np.roll(f_x, -1) + 9 * np.roll(f_x, -2) - np.roll(f_x, -3)) / (60 * dx)

# Compute numerical derivatives using different schemes
f_prime_second_order = second_order_finite_difference(f_x, dx)
f_prime_fourth_order = fourth_order_finite_difference(f_x, dx)
f_prime_sixth_order = sixth_order_finite_difference(f_x, dx)

# Plot the results
plt.figure(figsize=(10, 6))
plt.plot(x, f_prime_analytical_values, label='Analytical derivative')
plt.plot(x, f_prime_numerical, 'o', label='First-order numerical (N=20)')
plt.plot(x, f_prime_second_order, 'x', label='Second-order numerical (N=20)')
plt.plot(x, f_prime_fourth_order, 's', label='Fourth-order numerical (N=20)')
plt.plot(x, f_prime_sixth_order, 'd', label='Sixth-order numerical (N=20)')
plt.xlabel('x')
plt.ylabel('f\'(x)')
plt.legend()
plt.title('Numerical vs Analytical Derivative using Different Schemes')
plt.show()

def deriv_2nd(x, dx):
    return (np.sin(np.roll(x, -1)) - np.sin(np.roll(x, 1))) / (2 * dx)

def deriv_4th(x, dx):
    return (-np.sin(np.roll(x, 2)) + 8*np.sin(np.roll(x, 1)) - 8*np.sin(np.roll(x, -1)) + np.sin(np.roll(x, -2))) / (12 * dx)

def deriv_6th(f_x, dx):
    return (np.roll(f_x, 3) - 9 * np.roll(f_x, 2) + 45 * np.roll(f_x, 1) - 45 * np.roll(f_x, -1) + 9 * np.roll(f_x, -2) - np.roll(f_x, -3)) / (60 * dx)


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
