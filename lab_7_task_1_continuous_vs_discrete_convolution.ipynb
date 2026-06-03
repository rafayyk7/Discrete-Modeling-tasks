import numpy as np
import matplotlib.pyplot as plt
# Part 1: Setting up the Signals
def x_t(t):
    return 5 * np.cos(20 * np.pi * t)

def h_t(t):
    return np.where((t >= 0) & (t <= 2), 1, 0)
# Part 2: Simulating Continuous Time
t = np.linspace(0, 10, 20000)
dt = t[1] - t[0]

x_vals = x_t(t)
h_vals = h_t(t)

y_cont = np.convolve(x_vals, h_vals, mode='same') * dt
# Part 3: Sampling (Moving to Digital)
fs = 100
Ts = 1/fs

n = np.arange(0, int(10 * fs))
t_samp = n * Ts
# Part 3: Sampling (Moving to Digital)
Y1_n = np.interp(t_samp, t, y_cont)
# Method 2: Discrete Convolution ($Y_2$)
x_n = x_t(t_samp)
h_n = h_t(t_samp)

Y2_n = np.convolve(x_n, h_n, mode='same')
# Part 5: Plotting the Results
plt.figure(figsize=(12,4))
plt.stem(n, Y1_n, basefmt=" ")
plt.title("Y1[n] = Sampled Version of y(t)")
plt.xlabel("n")
plt.ylabel("Y1[n]")
plt.grid(True)
plt.show()

plt.figure(figsize=(12,4))
plt.stem(n, Y2_n, basefmt=" ")
plt.title("Y2[n] = Discrete Convolution x[n] * h[n]")
plt.xlabel("n")
plt.ylabel("Y2[n]")
plt.grid(True)
plt.show()

plt.figure(figsize=(12,5))
plt.plot(n, Y1_n, label="Y1[n] (sampled y(t))")
plt.plot(n, Y2_n, '--', label="Y2[n] (discrete convolution)")
plt.title("Comparison of Y1[n] and Y2[n]")
plt.xlabel("n")
plt.ylabel("Amplitude")
plt.grid(True)
plt.legend()
plt.show()
