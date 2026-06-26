import numpy as np
import math

# Number of simulations
N = 100000
rng = np.random.default_rng(0)

# (a) λ = 1 (0.20 * 5). Unsatisfactory if errors >= 2
lam_a = 1
analytical_a = 1 - (math.exp(-lam_a) + lam_a*math.exp(-lam_a))
sim_a = np.mean(rng.poisson(lam_a, N) >= 2)

print("Problem 1(a)")
print("Analytical:", analytical_a)
print("Simulated :", sim_a)

# (b) λ = 1.25 (0.25 * 5). Accepted if errors <= 1
lam_b = 1.25
analytical_b = math.exp(-lam_b)*(1+lam_b)
sim_b = np.mean(rng.poisson(lam_b, N) <= 1)

print("\nProblem 1(b)")
print("Analytical:", analytical_b)
print("Simulated :", sim_b)

