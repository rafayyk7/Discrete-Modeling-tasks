import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom, norm

n = 500
p = 0.95
mu = n * p
sigma = np.sqrt(n * p * (1 - p))
x_cont = np.linspace(mu-4*sigma, mu+4*sigma, 500)
x = np.arange(460, 491)
binom_pmf = binom.pmf(x, n, p)
norm_pdf = norm.pdf(x_cont, mu, sigma)
#EXACT PROB
prob_exact_480 = binom.pmf(480, n, p)
prob_exact_range = binom.cdf(490, n, p) - binom.cdf(469, n, p)
#NORMAL
prob_approx_480 = norm.cdf(480.5, mu, sigma) - norm.cdf(479.5, mu, sigma)
prob_approx_range = norm.cdf(490.5, mu, sigma) - norm.cdf(469.5, mu, sigma)


plt.figure(figsize=(12, 6))
plt.plot(x_cont, norm_pdf, label='Normal PDF')
plt.bar(x, binom_pmf, width=1, alpha=0.7, label='Binomial PMF')


plt.xlabel("Number of Successes")
plt.ylabel("Probability")
plt.title("Binomial Distribution vs. Normal Approximation")
plt.legend()
plt.grid(True)
plt.show()

print(f"Exact Probability of 480 successes (Binomial): {prob_exact_480:.6f}")
print(f"Approximate Probability of 480 successes (Normal): {prob_approx_480:.6f}")
print(f"Exact Probability of 460 to 490 successes (Binomial): {prob_exact_range:.6f}")
print(f"Approximate Probability of 460 to 490 successes (Normal): {prob_approx_range:.6f}")
