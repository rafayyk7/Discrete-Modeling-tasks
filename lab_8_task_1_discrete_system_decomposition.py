# ----------------------------------------------------------------------
# NOTE: This script requires the 'control' and 'pandas' libraries.
# To install them, open your terminal or command prompt and run:
#     pip install control pandas
# ----------------------------------------------------------------------

import numpy as np
import control as C
import matplotlib.pyplot as plt
import pandas as pd

# # ---------------------------------
# # 1. Input signal
# # ---------------------------------
N = 25
t = np.arange(0, N, 1)
# Create step signal using concatenate as shown in class
x = np.concatenate(([np.ones(10), np.zeros(N-10)]))

# # ---------------------------------
# # 2. Original system H(z)
# # ---------------------------------
# H(z) = (1 - 0.25z^-1) / (1 - 0.25z^-1 - 0.125z^-2)
# Converted to z domain: (z^2 - 0.25z) / (z^2 - 0.25z - 0.125)
# Note: We pad numerator with 0 to represent z^2 and z^1 terms correctly
num = [1, -0.25]
den = [1, -0.25, -0.125]
Ts = 1  # Sample time

H = C.TransferFunction(num, den, Ts)

# Original system response
t_out, y_orig = C.forced_response(H, T=t, U=x)

# # ---------------------------------
# # 3. Cascade decomposition
# # ---------------------------------
# H(z) = H1(z) * H2(z)
# H1(z) = (1 - 0.25 z^-1) / (1 - 0.5 z^-1)  -> (z - 0.25)/(z - 0.5)
# H2(z) = 1 / (1 + 0.25 z^-1)               -> z / (z + 0.25)

# Define transfer functions for each stage
H1 = C.TransferFunction([1, -0.25], [1, -0.5], Ts)
H2 = C.TransferFunction([1, 0], [1, 0.25], Ts)

# Simulate sequentially
t1, y1 = C.forced_response(H1, T=t, U=x)       # Output of stage 1
t2, y_cascade = C.forced_response(H2, T=t, U=y1) # Input to stage 2 is output of stage 1

# # ---------------------------------
# # 4. Parallel decomposition
# # ---------------------------------
# H(z) = A/(1 - 0.5 z^-1) + B/(1 + 0.25 z^-1)
# Calculated Residues:
A = 1
B = -1.25

Hpar1 = C.TransferFunction([A], [1, -0.5], Ts)
Hpar2 = C.TransferFunction([B], [1, 0.25], Ts)

t3, y_par1 = C.forced_response(Hpar1, T=t, U=x)
t4, y_par2 = C.forced_response(Hpar2, T=t, U=x)

y_parallel = y_par1 + y_par2

# # ---------------------------------
# # 5. Plot all results
# # ---------------------------------
plt.figure()
plt.stem(t,x)
plt.title("Input Signal x[n]")

plt.figure()
plt.stem(t_out, y_orig)
plt.title("Original System Output")

plt.figure()
plt.stem(t_out, y_cascade)
plt.title("Cascade Decomposition Output")

plt.figure()
plt.stem(t, y_parallel)
plt.title("Parallel Decomposition Output")

plt.show()
# # ---------------------------------
# # 6. Comparative Table (Requirement)
# # ---------------------------------
df = pd.DataFrame({
    'n': t,
    'y_original': y_orig.flatten(),
    'y_cascade': y_cascade.flatten(),
    'y_parallel': y_parallel.flatten()
})

print("\n--- Comparative Analysis Table ---")
print(df.to_string(index=False))

# Verification
print("\nMatch (Orig vs Cascade):", np.allclose(y_orig, y_cascade))
print("Match (Orig vs Parallel):", np.allclose(y_orig, y_parallel))
