import numpy as np
import pandas as pd

# --- 1. Problem Inputs (from the Bagel problem) ---
# Customer distribution
cust_values = [8, 10, 12, 14]
cust_probs = [0.35, 0.30, 0.25, 0.10]

# Order size distribution (in dozens)
order_values = [1, 2, 3, 4]
order_probs = [0.4, 0.3, 0.2, 0.1]

# Costs and prices (per dozen)
sell_price = 8.40
bake_cost = 5.80
# "half-price"
salvage_price = 8.40 / 2

# --- 2. Simulation Settings ---
# Seed for repeatable results
np.random.seed(12345)
# "running 5 days"
days_to_simulate = 5
# Number of times to run the 5-day simulation for a stable average
n_simulations = 200

# --- Determine a good range to test for Q ---
# First, find the average daily demand to center our test range
avg_customers = np.dot(cust_values, cust_probs) # 10.2 customers
avg_order_size = np.dot(order_values, order_probs) # 2.0 dozen
avg_daily_demand = avg_customers * avg_order_size # 20.4 dozen

# Test baking quantities (Q) in steps of 5, as requested.
# We'll test from 5 to 60, which safely covers the average (20.4)
# and the theoretical max (14 customers * 4 dozen = 56).
candidate_Q = range(5, 61, 5)

# --- 3. Simulation Function ---
def simulate_period(Q):
    """
    Simulates one 5-day period for a given baking quantity (Q)
    and returns the total net profit for those 5 days.
    """
    total_profit = 0
    for _ in range(days_to_simulate):
        # 1. Find the number of customers for this day
        customers = np.random.choice(cust_values, p=cust_probs)

        # 2. Find the total demand (in dozens) from all customers
        # We simulate one order for each of the customers
        demand = np.sum(np.random.choice(order_values, size=customers, p=order_probs))

        # 3. Calculate how many were sold and how many were left over
        sales = min(demand, Q)
        leftovers = max(Q - demand, 0)

        # 4. Calculate the profit for this single day
        # (Revenue from sales) + (Revenue from salvage) - (Total cost of baking)
        daily_profit = (sales * sell_price) + (leftovers * salvage_price) - (Q * bake_cost)

        # 5. Add this day's profit to the 5-day total
        total_profit += daily_profit

    return total_profit

# --- 4. Run the Full Monte Carlo Simulation ---
results = []
print(f"Running {n_simulations:,} simulations for each baking quantity...")

# Loop through every possible Q we want to test
for Q in candidate_Q:
    # Run the 5-day simulation n_simulations times
    profits = [simulate_period(Q) for _ in range(n_simulations)]

    # Calculate the average profit for this Q and store it
    results.append((Q, np.mean(profits)))

# --- 5. Display the Final Results ---
# Convert results to a clean table
df = pd.DataFrame(results, columns=["Dozens_Baked_Daily (Q)", "Mean_5Day_Net_Profit"])

# Set formatting for currency
pd.set_option('display.float_format', lambda x: f'${x:,.2f}')

print("\n--- Simulation Results for Each Policy ---")
print(df.to_string(index=False))

# Find and print the best baking quantity
best_row = df.loc[df["Mean_5Day_Net_Profit"].idxmax()]
print("\n" + "="*40)
print("Optimal number of DOZEN bagels to bake:")
print(f"  Q = {int(best_row['Dozens_Baked_Daily (Q)'])} dozen bagels per day")
print(f"  Resulting in an average 5-day net profit of: ${best_row['Mean_5Day_Net_Profit']:.2f}")
print("="*40)
