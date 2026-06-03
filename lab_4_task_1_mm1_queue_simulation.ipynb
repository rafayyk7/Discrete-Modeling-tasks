import simpy, random

# basic inputs

LAMBDA     = 5.0     # arrivals per hour
MU         = 8.0     # services per hour
SIM_HOURS  = 8.0     # total simulation time (hours)

random.seed(RNG_SEED)

# list for tracking what happens
wait_times   = []    # each customer's waiting time before service
system_times = []    # each customer's total time in system
total_service_time = 0.0  # for utilization
served = 0

# customer processing
def customer(env, name, server):
    """One customer: arrive -> wait if needed -> get served -> depart"""
    global total_service_time, served

# when customer arrives
    arrival_time = env.now

# request the single teller
    with server.request() as req:
        yield req

# measuring waiting time
        wait = env.now - arrival_time
        wait_times.append(wait)

# getting served
        service_time = random.expovariate(MU)
        total_service_time += service_time


        yield env.timeout(service_time)

# done with the service
    system_times.append(env.now - arrival_time)
    served += 1

# customer arriving randomly
def source(env, server):
    """Generate customers with exponential inter-arrival times (rate LAMBDA)"""
    i = 0
    while True:
        interarrival = random.expovariate(LAMBDA)
        yield env.timeout(interarrival)
        env.process(customer(env, f"Cust-{i}", server))
        i += 1

# run the simulation
env = simpy.Environment()
server = simpy.Resource(env, capacity=1)    # M/M/1 -> one teller
env.process(source(env, server))
env.run(until=SIM_HOURS)

# theoretical M/M/1 for comparison
rho  = LAMBDA / MU
L_th = rho / (1 - rho)
Lq_th = rho**2 / (1 - rho)
W_th  = 1 / (MU - LAMBDA)
Wq_th = rho / (MU - LAMBDA)

# simulation based results
lambda_hat = served / SIM_HOURS if SIM_HOURS > 0 else float("nan")
Wq_hat = sum(wait_times)/len(wait_times) if wait_times else float("nan")
W_hat  = sum(system_times)/len(system_times) if system_times else float("nan")
L_hat  = lambda_hat * W_hat if served else float("nan")
Lq_hat = lambda_hat * Wq_hat if served else float("nan")
rho_hat = total_service_time / SIM_HOURS

# print results
print("\n=== HBL GIK Teller — Simple M/M/1 ===")
print(f"Ran for: {SIM_HOURS} hours | Served: {served} customers")
print("\n-- Theory --")
print(f"ρ  (utilization)        = {rho:.3f}  (~{rho*100:.1f}%)")
print(f"L  (avg in system)       = {L_th:.3f}")
print(f"Lq (avg in queue)        = {Lq_th:.3f}")
print(f"W  (avg time in system)  = {W_th:.3f} h  (~{W_th*60:.1f} min)")
print(f"Wq (avg wait in queue)   = {Wq_th:.3f} h  (~{Wq_th*60:.1f} min)")
print("\n-- Simulation --")
print(f"ρ̂  (utilization)        = {rho_hat:.3f}  (~{rho_hat*100:.1f}%)")
print(f"L̂  (avg in system)       = {L_hat:.3f}")
print(f"L̂q (avg in queue)        = {Lq_hat:.3f}")
print(f"Ŵ  (avg time in system)  = {W_hat:.3f} h  (~{W_hat*60:.1f} min)")
print(f"Ŵq (avg wait in queue)   = {Wq_hat:.3f} h  (~{Wq_hat*60:.1f} min)")
