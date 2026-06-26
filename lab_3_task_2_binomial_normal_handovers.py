import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom, norm

n = 800
p = 0.98
mu = n * p
sigma = np.sqrt(n * p * (1 - p))

x_cont = np.linspace(mu - 4*sigma, mu + 4*sigma, 500)
x = np.arange(760, 801)

# Binomial PMF & Normal PDF
binom_pmf = binom.pmf(x, n, p)
norm_pdf  = norm.pdf(x_cont, mu, sigma)

# Exact probabilities (Binomial)
# Success rate > 97%
prob_sr_gt_97_exact = binom.sf(775, n, p)

# successful handovers between 770 and 782
prob_770_782_exact = binom.cdf(782, n, p) - binom.cdf(769, n, p)

# Fewer than 20 handovers unsuccessful
q = 1 - p
prob_fail_lt20_exact = binom.cdf(19, n, q)

# Exactly 1% fail
prob_exact_1pct_fail = binom.pmf(8, n, q)

# Normal approximation probabilities (with continuity correction)
# success rate > 97% (X >= 776)
prob_sr_gt_97_norm = 1 - norm.cdf(775.5, mu, sigma)

# 770 <= X <= 782
prob_770_782_norm = norm.cdf(782.5, mu, sigma) - norm.cdf(769.5, mu, sigma)

# (c) failures P(Y <= 19)
mu_f = n * q
sigma_f = np.sqrt(n * p * q)
prob_fail_lt20_norm = norm.cdf(19.5, mu_f, sigma_f)

# (d) exactly 8 failures
prob_1pct_fail_norm = norm.cdf(8.5, mu_f, sigma_f) - norm.cdf(7.5, mu_f, sigma_f)

# 7) Plot (bars = binomial PMF of successes, curve = normal approx)
plt.figure(figsize=(12, 6))
plt.bar(x, binom_pmf, width=1, alpha=0.7, label='Binomial PMF (successes)')
plt.plot(x_cont, norm_pdf, label='Normal PDF (approx)', linewidth=2)
plt.xlabel("Number of Successful Handovers")
plt.ylabel("Probability")
plt.title("Task 2: Binomial vs Normal Approximation (n=800, p=0.98)")
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()

# 8) Print results
print(f"Success rate > 97%  (Exact Binomial): {prob_sr_gt_97_exact:.6f}")
print(f"Success rate > 97%  (Normal Approx.): {prob_sr_gt_97_norm:.6f}")

print(f"P(770 ≤ successes ≤ 782)  (Exact): {prob_770_782_exact:.6f}")
print(f"P(770 ≤ successes ≤ 782)  (Normal): {prob_770_782_norm:.6f}")

print(f"P(failures ≤ 19)  (Exact): {prob_fail_lt20_exact:.6f}")
print(f"P(failures ≤ 19)  (Normal): {prob_fail_lt20_norm:.6f}")

print(f"P(exactly 1% fail = 8 failures)  (Exact): {prob_exact_1pct_fail:.6f}")
print(f"P(exactly 1% fail = 8 failures)  (Normal): {prob_1pct_fail_norm:.6f}")
