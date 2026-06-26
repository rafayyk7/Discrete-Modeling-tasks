import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom, norm

# Params
n, p = 800, 0.98
q = 1 - p
mu, sigma = n*p, np.sqrt(n*p*q)

sr_gt_97_exact   = binom.sf(775, n, p)
rng_770_782_exact = binom.cdf(782, n, p) - binom.cdf(769, n, p)
fail_le_19_exact = binom.cdf(19, n, q)
exact_1pct_fail  = binom.pmf(8, n, q)


sr_gt_97_norm    = 1 - norm.cdf(775.5, mu, sigma)
rng_770_782_norm = norm.cdf(782.5, mu, sigma) - norm.cdf(769.5, mu, sigma)

mu_f, sigma_f = n*q, np.sqrt(n*p*q)
fail_le_19_norm = norm.cdf(19.5, mu_f, sigma_f)
exact_1pct_fail_norm = norm.cdf(8.5, mu_f, sigma_f) - norm.cdf(7.5, mu_f, sigma_f)


print(f"Success rate > 97%  | Exact: {sr_gt_97_exact:.6f} | Normal: {sr_gt_97_norm:.6f}")
print(f"770–782 successes    | Exact: {rng_770_782_exact:.6f} | Normal: {rng_770_782_norm:.6f}")
print(f"Failures ≤ 19        | Exact: {fail_le_19_exact:.6f} | Normal: {fail_le_19_norm:.6f}")
print(f"Exactly 1% fail (8)  | Exact: {exact_1pct_fail:.6f} | Normal: {exact_1pct_fail_norm:.6f}")

x = np.arange(int(mu - 5*sigma), int(mu + 5*sigma) + 1)
plt.figure(figsize=(10,5))
plt.bar(x, binom.pmf(x, n, p), width=1, alpha=0.6, label="Binomial PMF")
plt.plot(x, norm.pdf(x, mu, sigma), lw=2, label="Normal PDF")
plt.xlabel("Successful Handovers"); plt.ylabel("Probability")
plt.title("n=800, p=0.98  —  Binomial vs Normal")
plt.legend(); plt.grid(alpha=0.3); plt.tight_layout(); plt.show()
