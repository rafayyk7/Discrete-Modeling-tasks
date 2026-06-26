import numpy as np

# ------------------------------
# Task 1 signals
# ------------------------------
x1 = [n**2 for n in range(11)]  # x[n] = n^2, 0<=n<=10
h1 = [n for n in range(6)]      # h[n] = n, 0<=n<=5

Nx1 = len(x1)
Nh1 = len(h1)
N1 = max(Nx1, Nh1)  # Circular convolution length (usually pick max of lengths)

# Zero-pad h1 to length N1
h1_padded = h1 + [0]*(N1 - Nh1)

# ------------------------------
# Manual circular convolution
# ------------------------------
y1_circ = [0]*N1

for n in range(N1):
    for k in range(N1):
        y1_circ[n] += x1[k % Nx1] * h1_padded[(n - k) % N1]

# ------------------------------
# NumPy circular convolution using FFT
# ------------------------------
y1_circ_fft = np.fft.ifft(np.fft.fft(x1, N1) * np.fft.fft(h1_padded, N1)).real
y1_circ_fft = [round(float(val), 4) for val in y1_circ_fft]

# ------------------------------
# Compare with linear convolution from Task 1
# ------------------------------
y1_linear = np.convolve(x1, h1)
y1_linear_clean = [round(float(val), 4) for val in y1_linear]

print("Task 1: Linear convolution:")
print(y1_linear_clean)
print("\nTask 1: Circular convolution (manual/FFT):")
print([round(val,4) for val in y1_circ])
print("\nTask 1: Circular convolution (FFT clean):")
print(y1_circ_fft)
