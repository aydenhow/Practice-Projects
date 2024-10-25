# estimate_pi.py #
# Estimates Pi via three methods.

import numpy as np

pi_sum = 0
iterations = int(input("Enter number of iterations: "))
for n in range(iterations):
    pi_sum += ((-1)**n)/(2*n + 1) * (4/(5**(2*n + 1)) - 1/(239**(2*n+1)))
pi_estimate = 4 * pi_sum

print(f"Summation estimate with n={iterations} is {pi_estimate}")
print("NumPy estimate: " + str(np.pi))

print("Difference: " + '{:0.2e}'.format(pi_estimate - np.pi) + ', ' + '{:0.2e}'.format((pi_estimate - np.pi) / pi_estimate) + '%')

print('Messy estimation (explicit constant using sqrt): ' + str((66*np.sqrt(2))/(33*np.sqrt(29)-148)))
