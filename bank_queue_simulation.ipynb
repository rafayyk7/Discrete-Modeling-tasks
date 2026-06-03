import math
import random

# --- Helper Function for Exponential Times ---
def get_exponential_time(mean):
    """
    Generates a random time from an exponential distribution
    given its mean.
    """
    # Uses the inverse transform method
    return -mean * math.log(1.0 - random.random())

# --- 1. Simulation Parameters ---
# We will use minutes as our time unit
SIMULATION_END_TIME = 120  # 2 hours = 120 minutes
MEAN_INTERARRIVAL = 6.0    # 60 min / 10 customers
MEAN_SERVICE = 7.5         # 60 min / 8 customers

# Set a seed for repeatable results
random.seed(42)

# --- 2. Simulation Variables ---
current_time = 0.0
server_free_time = 0.0

# Lists to store data for our analysis
all_wait_times = []
all_system_times = []

# Counters
customers_arrived = 0
customers_served_by_cutoff = 0

print(f"--- Simulating Bank Queue for {SIMULATION_END_TIME} Minutes ---")
print(f"Mean arrival: {MEAN_INTERARRIVAL} min, Mean service: {MEAN_SERVICE} min\n")

# --- 3. The Simulation Loop ---
# We will generate new customer arrivals as long as their arrival
# time is within the 120-minute simulation window.
while current_time <= SIMULATION_END_TIME:

    # 1. Get the time until the next customer arrives
    interarrival_time = get_exponential_time(MEAN_INTERARRIVAL)
    current_time += interarrival_time

    # 2. If their arrival is after the cutoff, stop the simulation
    if current_time > SIMULATION_END_TIME:
        break

    customers_arrived += 1

    # 3. Get this customer's service time
    service_time = get_exponential_time(MEAN_SERVICE)

    # 4. Determine when their service can begin
    # It's the LATER of when they arrive OR when the server is free
    service_start_time = max(current_time, server_free_time)

    # 5. Calculate key metrics for this customer
    wait_time = service_start_time - current_time
    service_end_time = service_start_time + service_time
    system_time = service_end_time - current_time # (wait + service)

    # 6. Store the results
    all_wait_times.append(wait_time)
    all_system_times.append(system_time)

    # 7. Update the server's status
    server_free_time = service_end_time

    # Check if they were served within the 2-hour window
    if service_end_time <= SIMULATION_END_TIME:
        customers_served_by_cutoff += 1

# --- 4. Evaluating Parameters ---
avg_wait_time = sum(all_wait_times) / len(all_wait_times)
avg_system_time = sum(all_system_times) / len(all_system_times)

# Find out how many people are still in the system at 120 minutes
# (This includes people waiting + the person being served)
customers_in_system_at_cutoff = 0
if server_free_time > SIMULATION_END_TIME:
    # Find how many people arrived but had not finished service
    num_not_finished = 0
    for i in range(len(all_wait_times)):
        arrival = current_time - (len(all_wait_times) - 1 - i) * MEAN_INTERARRIVAL # This is an approximation
        service_end = arrival + all_system_times[i]
        if service_end > SIMULATION_END_TIME:
            num_not_finished += 1
    # A simpler metric:
    customers_in_system_at_cutoff = customers_arrived - customers_served_by_cutoff


print("--- Simulation Results ---")
print(f"Total customers who arrived in 2 hours: {customers_arrived}")
print(f"Customers served before 2-hour mark:  {customers_served_by_cutoff}")
print(f"Avg. Wait Time for arrived customers:  {avg_wait_time:.2f} minutes")
print(f"Avg. Time in System for customers:    {avg_system_time:.2f} minutes")
print(f"Customers still in bank at 120 min: {customers_in_system_at_cutoff}")
print(f"Server is busy until (minute):        {server_free_time:.2f}")
