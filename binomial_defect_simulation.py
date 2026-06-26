import numpy as np

N = 100000
rng = np.random.default_rng(1)
n = 100

# (a) p=0.01, reject if >=2 defectives
p_a = 0.01
P0 = (1-p_a)**n
P1 = n*p_a*(1-p_a)**(n-1)
analytical_a = 1 - (P0+P1)
sim_a = np.mean(rng.binomial(n, p_a, N) >= 2)

print("Problem 2(a)")
print("Analytical:", analytical_a)
print("Simulated :", sim_a)

# (b) p=0.05, accept if <=1 defective
p_b = 0.05
P0 = (1-p_b)**n
P1 = n*p_b*(1-p_b)**(n-1)
analytical_b = P0+P1
sim_b = np.mean(rng.binomial(n, p_b, N) <= 1)

print("\nProblem 2(b)")
print("Analytical:", analytical_b)
print("Simulated :", sim_b)
