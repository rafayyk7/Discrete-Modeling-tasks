import numpy as np
import matplotlib.pyplot as plt

# Simulate 1000 dice rolls
rolls = np.random.randint(1, 7, size=1000)

# Count occurrences of each face (1–6)
values, counts = np.unique(rolls, return_counts=True)

# Calculate probabilities
probabilities = counts / 1000

# Display probabilities
for val, prob in zip(values, probabilities):
    print(f"Face {val}: Probability = {prob:.3f}")

# Plot the probabilities
plt.bar(values, probabilities, tick_label=values)
plt.xlabel("Dice Face")
plt.ylabel("Probability")
plt.title("Dice Roll Probabilities (1000 simulations)")
plt.show()
