import pandas as pd

def solve_max_profit(n):
    # Building properties: (Name, Build_Time, Earning_per_time)
    items = [
        ("T", 5, 1500),  # Theatre
        ("P", 4, 1000),  # Pub
        ("C", 10, 2000) # Commercial Park
    ]

    # Initialize DP array: dp[t] stores max profit achieved at time t
    dp_only_build = [0] * (n + 1)
    
    # path[t] stores the index of the building that leads to dp[t]
    path_only_build = [-1] * (n + 1)
    
    # Dynamic Programming loop
    for t in range(1, n + 1):
        # We can stop development at any time t' <= n, so the max profit at 't' should 
        # at least be the max profit from the previous step (t-1), which accounts 
        # for not building anything at the current step.
        dp_only_build[t] = dp_only_build[t-1] 
        path_only_build[t] = path_only_build[t-1] # Retain previous best path
        
        for i, (name, build_time, earning_per_time) in enumerate(items):
            if t >= build_time:
                prev_time = t - build_time
                
                # Profit from the new building 'i' completed at time 't'
                # Profit = Earning_per_time * (Total_Time - Completion_Time)
                current_building_profit = earning_per_time * (n - t)
                
                new_profit = dp_only_build[prev_time] + current_building_profit
                
                if new_profit > dp_only_build[t]:
                    dp_only_build[t] = new_profit
                    path_only_build[t] = i
    
    # Max profit is the highest value in the dp array, which will be dp[n] 
    # due to the inclusion of dp[t] = dp[t-1] transition.
    max_profit = dp_only_build[n]
    t_final = n # The optimal time is tracked through the path up to n.

    # Reconstruct the solution (counts of T, P, C)
    counts = {"T": 0, "P": 0, "C": 0}
    
    current_t = t_final
    while current_t > 0 and path_only_build[current_t] != -1:
        item_index = path_only_build[current_t]
        
        # Check if a building was actually placed (item_index corresponds to an item)
        # Note: If path[t] == path[t-1], it means no building was placed at t.
        # This reconstruction logic is complex due to the dp[t] = dp[t-1] step.
        
        # A simpler reconstruction: Iterate backwards from t_final and only consider
        # the time steps where an item was placed.
        
        # Let's re-run the reconstruction using the logic that passed the tests:
        # Trace back the buildings that were *explicitly* built.
        
        # Rerun DP to find the time that gave the max profit for the final building
        dp_build_only = [0] * (n + 1)
        path_build_only = [-1] * (n + 1)
        
        for t in range(1, n + 1):
            for i, (name, build_time, earning_per_time) in enumerate(items):
                if t >= build_time:
                    prev_time = t - build_time
                    current_building_profit = earning_per_time * (n - t)
                    new_profit = dp_build_only[prev_time] + current_building_profit
                    
                    if new_profit > dp_build_only[t]:
                        dp_build_only[t] = new_profit
                        path_build_only[t] = i
        
        max_profit = max(dp_build_only)
        t_final = dp_build_only.index(max_profit)
        
        current_t = t_final
        while current_t > 0 and path_build_only[current_t] != -1:
            item_index = path_build_only[current_t]
            name, build_time, _ = items[item_index]
            counts[name] += 1
            current_t -= build_time

    solution_str = f"T: {counts['T']} P: {counts['P']} C: {counts['C']}"

    return max_profit, solution_str

# Test cases:
# Test Case 1: Time Unit: 7 -> Earnings: $3000, Solution: T: 1 P: 0 C: 0
# Test Case 2: Time Unit: 8 -> Earnings: $4500, Solution: T: 1 P: 0 C: 0
# Test Case 3: Time Unit: 13 -> Earnings: $16500, Solution: T: 2 P: 0 C: 0

def run_tests():
    test_cases = [7, 8, 13]
    results = []
    
    for n in test_cases:
        max_profit, solution_str = solve_max_profit(n)
        results.append({
            "Input Time (n)": n,
            "Calculated Max Earnings": max_profit,
            "Calculated Solution": solution_str
        })
    
    return pd.DataFrame(results)

if __name__ == '__main__':
    print("--- Test Results ---")
    print(run_tests())
    print("\\nNote: The Max Profit problem requires Dynamic Programming because the value of a building")
    print("depends on its completion time (Completion_Time = sum of all preceding build times).")