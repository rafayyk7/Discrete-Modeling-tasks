import simpy
import random
import math


RNG_SEED = 42
random.seed(RNG_SEED)
LAMBDA = 10.0    # average arrivals per minute
MU = 15.0        # average services per minute
SIM_TIME = 60.0  # total simulation time (minutes)

# Lists to store results
waiting_times = []
system_times = []
total_service_time = 0.0
served_requests = 0


#  Request Process
def request(env, name, base_station):
    """Each request arrives, waits if needed, gets served, then leaves."""
    global total_service_time, served_requests

    arrival_time = env.now
    # Request access to the base station (server)
    with base_station.request() as req:
        yield req  # wait until base station is free

        # Calculate waiting time before service
        wait = env.now - arrival_time
        waiting_times.append(wait)

        # Generate random service time (exponential)
        service_time = random.expovariate(MU)
        total_service_time += service_time

        # Stay busy for that duration
        yield env.timeout(service_time)

    # Record total time in system
    total_time = env.now - arrival_time
    system_times.append(total_time)
    served_requests += 1


# Arrival Generator
def generate_requests(env, base_station):
    """Generates new requests following Poisson arrivals."""
    i = 0
    while True:
        interarrival = random.expovariate(LAMBDA)  # time between arrivals
        yield env.timeout(interarrival)
        env.process(request(env, f"Req-{i}", base_station))
        i += 1


# Simulation
env = simpy.Environment()
base_station = simpy.Resource(env, capacity=1)
env.process(generate_requests(env, base_station))
env.run(until=SIM_TIME)

# Theoretical Results
rho = LAMBDA / MU
Wq_theory = rho / (MU - LAMBDA)
W_theory = 1 / (MU - LAMBDA)
service_mean = 1 / MU

# Simulation Averages
avg_wait = sum(waiting_times) / len(waiting_times)
avg_total = sum(system_times) / len(system_times)
utilization = total_service_time / SIM_TIME

#  Results
print("\n=== Cellular Network (M/M/1) ===")
print(f"Simulated for {SIM_TIME} minutes")
print(f"Requests served: {served_requests}")

print("\n-- Theoretical --")
print(f"Utilization (ρ)         = {rho:.3f} ({rho*100:.1f}%)")
print(f"Avg waiting time (Wq)   = {Wq_theory:.4f} min (~{Wq_theory*60:.1f} sec)")
print(f"Avg system time (W)     = {W_theory:.4f} min (~{W_theory*60:.1f} sec)")
print(f"Service mean (1/μ)      = {service_mean:.4f} min (~{service_mean*60:.1f} sec)")

print("\n-- Simulation --")
print(f"Utilization (ρ̂)         = {utilization:.3f} ({utilization*100:.1f}%)")
print(f"Avg waiting time (Ŵq)   = {avg_wait:.4f} min (~{avg_wait*60:.1f} sec)")
print(f"Avg system time (Ŵ)     = {avg_total:.4f} min (~{avg_total*60:.1f} sec)")


P_wait_gt_1 = rho * math.exp(-(MU - LAMBDA) * 1)
print(f"\nP(Wq > 1 min) = {P_wait_gt_1:.4f} (~{P_wait_gt_1*100:.2f}%)")
