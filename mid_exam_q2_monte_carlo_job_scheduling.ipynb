import numpy as np

# Simulation parameters
N_jobs_per_type = 10000
day_length = 8        # hours per day
num_runs = 50         # Monte Carlo runs

# Define job properties
job_types = {
    0: {"lambda": 4, "service": lambda n: np.random.uniform(0, 2, n)},
    1: {"lambda": 6, "service": lambda n: np.random.uniform(1, 2, n)},
    2: {"lambda": 8, "service": lambda n: np.random.uniform(1, 5, n)},
}

def simulate_once():
    all_jobs = []

    # Generate arrivals and service times for each type
    for jtype, props in job_types.items():
        # Interarrival times (Exponential with mean = 1/lambda)
        interarrivals = np.random.exponential(1 / props["lambda"], N_jobs_per_type)
        arrival_times = np.cumsum(interarrivals)
        service_times = props["service"](N_jobs_per_type)

        for a, s in zip(arrival_times, service_times):
            all_jobs.append((a, s, jtype))

    # Sort all jobs by arrival time
    all_jobs.sort(key=lambda x: x[0]x[1])

    # Simulation variables
    current_time = 0
    day = 1
    day_end = day_length
    service_time_total = 0
    jobs_completed = 0
    jobs_per_day = []

    jobs_type_count = {0: 0, 1: 0, 2: 0}
    jobs_per_day_type = []

    # Process each job sequentially
    for arrival, service, jtype in all_jobs:
        # Wait until job arrives
        current_time = max(current_time, arrival)

        # Check if job fits in current day
        if current_time + service > day_end:
            # Move to next day
            jobs_per_day.append(jobs_completed)
            jobs_per_day_type.append(jobs_type_count.copy())
            jobs_type_count = {0: 0, 1: 0, 2: 0}

            day += 1
            current_time = (day - 1) * day_length  # start of next day
            day_end = day * day_length

        # Process job
        current_time += service
        service_time_total += service
        jobs_completed += 1
        jobs_type_count[jtype] += 1

    # Final day’s stats
    jobs_per_day.append(jobs_completed)
    jobs_per_day_type.append(jobs_type_count.copy())

    avg_service_time = service_time_total / (3 * N_jobs_per_type)
    total_days = day
    avg_jobs_per_type = {
        t: np.mean([d[t] for d in jobs_per_day_type])
        for t in jobs_type_count
    }

    return total_days, avg_service_time, avg_jobs_per_type

# Run Monte Carlo simulation
days_list = []
service_times = []
avg_jobs_type_runs = {0: [], 1: [], 2: []}

for _ in range(num_runs):
    d, s, avg_jobs_t = simulate_once()
    days_list.append(d)
    service_times.append(s)
    for t in avg_jobs_t:
        avg_jobs_type_runs[t].append(avg_jobs_t[t])

# Compute overall averages
avg_days = np.mean(days_list)
avg_service_time = np.mean(service_times)
avg_jobs_per_type_final = {t: np.mean(avg_jobs_type_runs[t]) for t in avg_jobs_type_runs}

print("----- Problem 2 Results (Monte Carlo) -----")
print(f"Average days to service all jobs: {avg_days:.2f}")
print(f"Average service time (hours): {avg_service_time:.3f}")
print("Average jobs per type handled per day:")
for t, val in avg_jobs_per_type_final.items():
    print(f"  Type {t}: {val:.2f} jobs/day")
