import streamlit as st
import pandas as pd
# Import the core function from your completed script
from assignment1 import solve_max_profit 

def main():
    st.set_page_config(page_title="Max Profit Optimizer", layout="centered")
    
    st.title("💰 Max Profit Problem Optimizer")
    st.markdown("### Dynamic Programming Solution for Land Development")
    
    # -----------------------------------------------------------
    # 1. Input Widget
    # -----------------------------------------------------------
    st.subheader("Time Constraint Input")
    
    # Use a number input for the total time unit 'n'
    n = st.number_input(
        "Enter the Total Time Unit (n):", 
        min_value=1, 
        value=13, # Defaulting to the largest test case
        step=1,
        help="This represents the total time available for sequential building."
    )
    
    # -----------------------------------------------------------
    # 2. Calculation and Output
    # -----------------------------------------------------------
    if n > 0:
        # Call the core DP function from assignment1.py
        max_profit, solution_str = solve_max_profit(n)
        
        st.success(f"Calculation for Time Unit: **{n}** Complete!")
        
        # Display the Max Earnings prominently
        st.subheader("Max Achievable Earnings")
        st.metric(label="Total Profit", value=f"${max_profit:,}")
        
        # Display the Optimal Mix
        st.subheader("Optimal Building Mix (T: Theatre, P: Pub, C: Commercial Park)")
        st.code(solution_str, language='text')

        # -----------------------------------------------------------
        # 3. Visualization (Bonus)
        # -----------------------------------------------------------
        # Extract counts from the solution string for visualization
        try:
            parts = solution_str.split()
            counts = {
                'Theatre (5 units)': int(parts[1]),
                'Pub (4 units)': int(parts[3]),
                'Commercial Park (10 units)': int(parts[5])
            }
            
            # Create a DataFrame for a bar chart
            df = pd.DataFrame(list(counts.items()), columns=['Property', 'Count'])
            
            if df['Count'].sum() > 0:
                st.subheader("Building Count Distribution")
                st.bar_chart(df.set_index('Property'))
            
        except Exception as e:
            st.warning("Could not generate visualization.")

    else:
        st.warning("Time Unit (n) must be a positive integer.")

if __name__ == "__main__":
    main()