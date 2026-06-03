import math

# --- 1. The Random Number Generator ---
# Corrected: The 'return' statement is now outside the loop.
def lcg(a, c, m, seed, n):
    """Generates a list of n uniform random numbers between 0 and 1."""
    numbers = []
    x = seed
    for _ in range(n):
        x = (a * x + c) % m
        numbers.append(x / m)
    return numbers

# --- 2. The Exponential Time Converter ---
# Corrected: Added a safety check to prevent math errors.
def exponential_variable(r, rate=1.0):
    """
    Generates an exponential random variable.
    The 'rate' is the key parameter that defines the mean (mean = 1 / rate).
    """
    # Safety check: math.log(0) is an error, so prevent r from being 1.0.
    if r >= 1.0:
        r = 0.999999
    return -(1 / rate) * math.log(1 - r)

# --- 3. Simulation Setup ---
packets = 1000

# LCG parameters
a = 17
c = 43
# Corrected: 'm' must be strictly GREATER THAN the numbers needed (2000).
m = 2001 # Using a prime number > 2000 is a safe choice.
seed = 123

# --- Key Assumption ---
# Since no data was given, we must assume a rate. rate=1.0 implies a mean of 1.0.
# We will use different rates to make the simulation more interesting.
arrival_rate_assumed = 0.8 # Average arrivals per time unit (implies mean time = 1.25)
service_rate_assumed = 1.0 # Average services per time unit (implies mean time = 1.0)

print(f"INFO: Running simulation with assumed arrival rate = {arrival_rate_assumed}")
print(f"INFO: Running simulation with assumed service rate = {service_rate_assumed}\n")

# --- 4. Generate Random Data ---
# Generate 2000 uniform random numbers
rand_nums = lcg(a, c, m, seed, 2 * packets)

# Create inter-arrival and service times from the random numbers
interarrival_times = [exponential_variable(r, rate=arrival_rate_assumed) for r in rand_nums[:packets]]
service_times = [exponential_variable(r, rate=service_rate_assumed) for r in rand_nums[packets:]]

# --- 5. The Main Simulation Loop ---
arrival_time_log = []
service_end_log = []
waiting_time_log = []

current_arrival_time = 0.0
server_free_time = 0.0

for i in range(packets):
    # Calculate when this packet arrives
    current_arrival_time += interarrival_times[i]
    arrival_time_log.append(current_arrival_time)

    # Determine when service can begin (after arrival AND after server is free)
    service_start_time = max(current_arrival_time, server_free_time)

    # Calculate wait time and when service ends
    wait = service_start_time - current_arrival_time
    service_end_time = service_start_time + service_times[i]

    # Log results for this packet and update server status
    waiting_time_log.append(wait)
    service_end_log.append(service_end_time)
    server_free_time = service_end_time

# --- 6. Calculate and Print Final Results ---
# Calculate the actual averages from the simulation run
avg_interarrival = sum(interarrival_times) / packets
avg_service = sum(service_times) / packets
avg_wait = sum(waiting_time_log) / packets
avg_system_time = avg_wait + avg_service

# Calculate rates and utilization from the simulation results
simulated_arrival_rate = 1 / avg_interarrival
simulated_service_rate = 1 / avg_service
utilization_factor = simulated_arrival_rate / simulated_service_rate

# Use Little's Law to find the average number of packets
avg_packets_in_queue = simulated_arrival_rate * avg_wait
avg_packets_in_system = simulated_arrival_rate * avg_system_time

print(f"Average Inter-arrival Time: {avg_interarrival:.4f}")
print(f"Average Service Time: ...... {avg_service:.4f}")
print(f"Average Waiting Time: ...... {avg_wait:.4f}")
print(f"Average Time in System: .... {avg_system_time:.4f}")
print("---------------------------------------------")
print(f"Utilization Factor: ......... {utilization_factor:.4f} (or {utilization_factor:.2%})")
print(f"Avg Packets in Queue (Lq): . {avg_packets_in_queue:.4f}")
print(f"Avg Packets in System (L): .. {avg_packets_in_system:.4f}")
