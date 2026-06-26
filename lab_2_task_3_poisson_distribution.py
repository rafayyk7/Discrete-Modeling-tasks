import numpy as np
from math import exp, factorial

lam = 2.0
k = 3
t = 500000

analytical = exp(-lam) * (lam ** k) / factorial(k)
samples = np.random.poisson(lam, t)
simulated = np.mean(samples == k)

print("Analytical = ", analytical)
print("Simulated = ", simulated)
