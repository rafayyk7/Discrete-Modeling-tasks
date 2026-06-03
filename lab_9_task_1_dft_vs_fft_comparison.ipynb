import numpy as np
import matplotlib.pyplot as plt

# Define a 16-point signal (example: simple sine + cosine combination)
N = 16
n = np.arange(N)
signal = np.sin(2 * np.pi * n / N) + 0.5 * np.cos(4 * np.pi * n / N)

# --- Step 1: Manual DFT implementation ---
def dft(x):
    N = len(x)
    X = np.zeros(N, dtype=complex)
    for k in range(N):
        for n in range(N):
            X[k] += x[n] * np.exp(-2j * np.pi * k * n / N)
    return X

manual_dft = dft(signal)

# --- Step 2: FFT using numpy ---
fft_result = np.fft.fft(signal)

# --- Step 3: Compare results ---
print("Manual DFT:\n", manual_dft)
print("\nFFT Result:\n", fft_result)

# Check if they are (almost) equal
print("\nAre they equal? ", np.allclose(manual_dft, fft_result))

# --- Step 4: Visualization (Optional but recommended) ---
plt.figure(figsize=(10, 9))

# Plot the input time-domain signal
plt.subplot(3, 1, 1)
plt.stem(n, signal)
plt.title("Input Signal: sin(2πn/16) + 0.5cos(4πn/16)")
plt.xlabel("n")
plt.ylabel("Amplitude")
plt.grid(True)

# Plot the magnitude of the Manual DFT
plt.subplot(3, 1, 2)
plt.stem(n, np.abs(manual_dft))
plt.title("Manual DFT Magnitude |X[k]|")
plt.xlabel("k (Frequency Bin)")
plt.ylabel("Magnitude")
plt.grid(True)

# Plot the magnitude of the NumPy FFT
plt.subplot(3, 1, 3)
plt.stem(n, np.abs(fft_result))
plt.title("NumPy FFT Magnitude |X[k]|")
plt.xlabel("k (Frequency Bin)")
plt.ylabel("Magnitude")
plt.grid(True)

plt.tight_layout()
plt.show()
