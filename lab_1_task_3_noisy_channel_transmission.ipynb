 import numpy as np
import matplotlib.pyplot as plt

def transmit_with_noise(message, noise_level):
    n_bits = len(message)
    noise = np.random.rand(n_bits) < noise_level
    received = np.copy(message)
    received[noise] = 1 - received[noise]
    errors = np.sum(message != received)
    prob_error = errors / n_bits
    return prob_error

n_bits = 100
message = np.random.randint(0, 2, n_bits)

noise_levels = np.arange(0, 1.05, 0.05)
error_probabilities = []

for nl in noise_levels:
    pe = transmit_with_noise(message, nl)
    error_probabilities.append(pe)

plt.figure(figsize=(10, 6))
plt.plot(noise_levels, error_probabilities)
plt.xlabel("Noise Level")
plt.ylabel("Probability of Error")
plt.title("Probability of Error vs. Noise Level")
plt.grid(True)
plt.show()
