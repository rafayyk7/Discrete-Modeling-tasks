import math
# --- Part 1: The Random Number Generator ---

def lcg_random_generator(count, seed=123, a=17, c=43, m=1000):
    """
    Generates a list of pseudo-random numbers using a Linear Congruential Generator (LCG).

    The formula is: X_{n+1} = (a * X_n + c) % m

    Args:
        count (int): The number of random integers to generate.
        seed (int): The starting value for the sequence.
        a (int): The multiplier.
        c (int): The increment.
        m (int): The modulus.

    Returns:
        list: A list of 'count' random integers between 0 and m-1.
    """
    random_numbers = []
    x = seed  # Start with the initial seed
    for _ in range(count):
        x = (a * x + c) % m
        random_numbers.append(x)
    return random_numbers

# --- Part 2: Helper Functions to Interpret Random Digits ---

def get_interarrival_from_digit(random_digit):
    """
    Takes a random digit (1-999) and returns the corresponding inter-arrival time.
    This is based on Table 5.1 from the problem description.
    """
    if 1 <= random_digit <= 125: return 1
    elif 126 <= random_digit <= 250: return 2
    elif 251 <= random_digit <= 375: return 3
    elif 376 <= random_digit <= 500: return 4
    elif 501 <= random_digit <= 625: return 5
    elif 626 <= random_digit <= 750: return 6
    elif 751 <= random_digit <= 875: return 7
    else: return 8 # Corresponds to digits 876 - 999

def get_service_from_digit(random_digit):
    """
    Takes a random digit (1-100) and returns the corresponding service time.
    This is based on Table 5.2 from the problem description.
    """
    if 1 <= random_digit <= 10: return 1
    elif 11 <= random_digit <= 30: return 2
    elif 31 <= random_digit <= 60: return 3
    elif 61 <= random_digit <= 85: return 4
    elif 86 <= random_digit <= 95: return 5
    else: return 6 # Corresponds to digits 96 - 100 (or 00)

# --- Part 3: The Main Simulation ---

def simulate_grocery_store():
    """
    Runs the full simulation for the grocery store checkout.
    """
    print("🛒 Simulating the Grocery Store using LCG...")

    NUM_CUSTOMERS = 100

    # Step 1: Generate all the random numbers we will need for the entire simulation.
    # We need two numbers per customer: one for arrival, one for service.
    total_random_numbers_needed = NUM_CUSTOMERS * 2
    lcg_sequence = lcg_random_generator(count=total_random_numbers_needed, seed=12345)

    # Step 2: Initialize variables to track simulation statistics.
    total_wait_time = 0.0
    total_service_time = 0.0
    total_interarrival_time = 0.0
    current_arrival_time = 0.0
    cashier_free_time = 0.0 # Time when the cashier becomes available

    # Step 3: Loop through each customer to process them.
    for i in range(NUM_CUSTOMERS):
        # --- LCG Integration ---
        # Get a raw number from our generated LCG sequence for inter-arrival time
        interarrival_lcg_num = lcg_sequence[2*i]
        # Scale it to the required range of 1-999 for the probability table
        interarrival_digit = (interarrival_lcg_num % 999) + 1

        # Get the next raw number for service time
        service_lcg_num = lcg_sequence[2*i + 1]
        # Scale it to the required range of 1-100 for its probability table
        service_digit = (service_lcg_num % 100) + 1

        # Determine the actual times from these scaled LCG digits
        interarrival = get_interarrival_from_digit(interarrival_digit)
        service = get_service_from_digit(service_digit)

        # The first customer has no inter-arrival time relative to the start
        if i == 0:
            interarrival = 0

        # --- Core Queueing Logic ---
        # Calculate when this customer arrives
        current_arrival_time += interarrival

        # Service can only begin after the customer arrives AND the cashier is free
        service_start_time = max(current_arrival_time, cashier_free_time)

        # Calculate how long this customer had to wait
        wait_time = service_start_time - current_arrival_time

        # Calculate when this customer's service will be finished
        service_end_time = service_start_time + service

        # The cashier is now busy until this new time
        cashier_free_time = service_end_time

        # --- Update Totals ---
        total_wait_time += wait_time
        total_service_time += service
        if i > 0: # Don't include the first customer's "0" interarrival in the average
            total_interarrival_time += interarrival

    # --- Step 4: Calculate final results from the simulation totals ---
    avg_interarrival = total_interarrival_time / (NUM_CUSTOMERS - 1)
    avg_service = total_service_time / NUM_CUSTOMERS
    avg_wait = total_wait_time / NUM_CUSTOMERS

    # Utilization = (Total time cashier was busy) / (Total simulation duration)
    utilization = total_service_time / cashier_free_time

    # Theoretical new utilization if service times were 20% faster
    new_utilization = (avg_service * 0.8) / avg_interarrival

    # --- Step 5: Print a clear summary of the results ---
    print("\n" + "="*50)
    print("TASK 1: GROCERY STORE SIMULATION RESULTS")
    print("="*50)
    print(f"1. Average Time Between Arrivals: {avg_interarrival:.4f} minutes")
    print(f"   -> Implied Arrival Rate (λ): {1/avg_interarrival:.4f} customers/min")
    print("-" * 50)
    print(f"2. Average Service Time: {avg_service:.4f} minutes")
    print(f"   -> Implied Service Rate (μ): {1/avg_service:.4f} customers/min")
    print("-" * 50)
    print(f"3. Average Customer Waiting Time in Queue: {avg_wait:.4f} minutes")
    print("-" * 50)
    print(f"4. Utilization Factor of Checkout: {utilization:.2%}")
    print(f"   -> Utilization if Service Time reduced by 20%: {new_utilization:.2%}")
    print("="*50)

# --- Run the simulation ---
simulate_grocery_store()
