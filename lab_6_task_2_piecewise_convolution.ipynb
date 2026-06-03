import numpy as np

# -----------------------------------
# Define x[n] = sin(50n), 0 <= n <= 50
# -----------------------------------
x = [np.sin(50 * n) for n in range(51)]

# -----------------------------------
# Define h[n]
# n, 0 <= n <= 5
# 1, 5 < n <= 10
# 10, 10 < n <= 20
# -----------------------------------
h = []
for n in range(21):
    if 0 <= n <= 5:
        h.append(n)
    elif 5 < n <= 10:
        h.append(1)
    elif 10 < n <= 20:
        h.append(10)

Nx = len(x)
Nh = len(h)
Ny = Nx + Nh - 1

# -----------------------------------
# Manual convolution
# -----------------------------------
y_manual = [0] * Ny

for n in range(Ny):
    for k in range(Nx):
        if (n - k) >= 0 and (n - k) < Nh:
            y_manual[n] += x[k] * h[n - k]

# Corrected line: Convert 'val' to a standard float before rounding
y_manual_clean = [round(float(val), 4) for val in y_manual]

# -----------------------------------
# NumPy convolution
# -----------------------------------
y_conv = np.convolve(x, h)
y_conv_clean = [round(float(val), 4) for val in y_conv]

# -----------------------------------
# Print results
# -----------------------------------
print("Manual convolution (cleaned, 4 decimal places):")
print(y_manual_clean)

print("\nNumPy convolution (cleaned, 4 decimal places):")
print(y_conv_clean)
