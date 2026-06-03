# ------------------------------
# Task 2 signals
# ------------------------------
x2 = [np.sin(50*n) for n in range(51)]
h2 = []
for n in range(21):
    if 0 <= n <= 5:
        h2.append(n)
    elif 5 < n <= 10:
        h2.append(1)
    elif 10 < n <= 20:
        h2.append(10)

Nx2 = len(x2)
Nh2 = len(h2)
N2 = max(Nx2, Nh2)  # Circular convolution length

# Zero-pad h2 to length N2
h2_padded = h2 + [0]*(N2 - Nh2)

# ------------------------------
# Manual circular convolution
# ------------------------------
y2_circ = [0]*N2
for n in range(N2):
    for k in range(N2):
        y2_circ[n] += x2[k % Nx2] * h2_padded[(n - k) % N2]

# ------------------------------
# NumPy circular convolution using FFT
# ------------------------------
y2_circ_fft = np.fft.ifft(np.fft.fft(x2, N2) * np.fft.fft(h2_padded, N2)).real
y2_circ_fft = [round(float(val), 4) for val in y2_circ_fft]

# ------------------------------
# Compare with linear convolution from Task 2
# ------------------------------
y2_linear = np.convolve(x2, h2)
y2_linear_clean = [round(float(val), 4) for val in y2_linear]

print("\nTask 2: Linear convolution:")
print(y2_linear_clean)
print("\nTask 2: Circular convolution (manual/FFT):")
print([round(val,4) for val in y2_circ])
print("\nTask 2: Circular convolution (FFT clean):")
print(y2_circ_fft)
