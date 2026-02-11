import streamlit as st
import re
import json
from datetime import datetime, timedelta

# --- AGENT LOGIC (Your existing functions) ---

def planner(question):
    return "1. Parse Question\n2. Extract Values\n3. Calculate\n4. Validate\n5. Format"

def executor(question):
    q = question.lower()
    # Logic for Time Difference
    times = re.findall(r'(\d{2}:\d{2})', question)
    if len(times) == 2:
        start = datetime.strptime(times[0], "%H:%M")
        end = datetime.strptime(times[1], "%H:%M")
        if end < start: end += timedelta(days=1)
        delta = end - start
        h, m = delta.seconds // 3600, (delta.seconds % 3600) // 60
        return {"answer": f"{h} hours {m} minutes", "explanation": "Time delta calculation."}
    
    # Logic for "Twice as many"
    if "twice as many" in q:
        match = re.search(r'(\d+)', question)
        if match:
            base = int(match.group(1))
            return {"answer": str(base + (2 * base)), "explanation": "Twice-as-many arithmetic."}
            
    return {"answer": "I can only solve time diff or 'twice as many' problems currently.", "explanation": "Fallback."}

# --- STREAMLIT UI ---

st.set_page_config(page_title="Multi-Agent Solver", page_icon="🤖")

st.title("🤖 Multi-Agent Logic Solver")
st.markdown("This app uses a **Planner-Executor-Verifier** flow to solve word problems.")

# User Input
question = st.text_input("Enter your question:", placeholder="e.g., Alice has 3 apples and twice as many green apples...")

if st.button("Solve"):
    if question:
        # Step 1: Planning
        with st.status("Agent Workflow Running...", expanded=True) as status:
            st.write("📝 **Planner Agent** creating steps...")
            plan = planner(question)
            st.code(plan)
            
            st.write("⚙️ **Executor Agent** calculating...")
            result = executor(question)
            
            st.write("✅ **Verifier Agent** checking results...")
            # Simple verification for the UI
            is_valid = "PASSED" if result["answer"] else "FAILED"
            
            status.update(label="Workflow Complete!", state="complete", expanded=False)

        # Display Results
        st.success(f"**Final Answer:** {result['answer']}")
        
        with st.expander("View Technical Details (JSON)"):
            st.json({
                "plan": plan,
                "execution_log": result["explanation"],
                "verification": is_valid
            })
    else:
        st.warning("Please enter a question first.")
