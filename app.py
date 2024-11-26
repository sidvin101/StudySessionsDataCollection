import streamlit as st
import time

st.title("Study Sessions Collection")

st.markdown("""
### Instructions

Welcome to the Study Sessions Collection app! This app helps you manage your study sessions by tracking the time spent on assignments, periodically collecting your responses about progress, and saving your session data.

1. **Enter your assignment details**: Provide your name and other details.
2. **Start the timer**: Press the "Start" button to begin tracking time for your assignment.
3. **Periodically update your progress**: Every 30 Minutes, stop the stopwatch and answer the questios, hitting submit afterwards. Don't worry if you over or underestimate the time
4. **Repeat**: I want to have 6 periods or 3 hours total of your dataset
5. **Final Submission**: Once you are done, please navigate to this form and submit the user_data.txt: https://forms.gle/dgWeGCHfn5q6JXCV9

Once you're ready, start by filling out the details about your assignment!
""")

# Asking the user initial questions
name = st.text_input("What is your name?")
class_id = st.text_input("What class is this assignment for?")
assignment = st.text_input("What assignment are you currently working on?")
deadline = st.text_input("How many days is the assignment due?")
other_assignments = st.text_input("How many other assignments do you also have around that deadline?")
hours = st.text_input("How many hours do you think this assignment will take?")
difficulty = st.selectbox("On a scale of 1-5, how difficult is your assignment (5 being the most difficult)", [1, 2, 3, 4, 5])

# Button to submit the answers
if st.button("Submit"):
    # Save the answers 
    user_data = {
        "Name": name,
        "Class": class_id,
        "Assignment": assignment,
        "Deadline": deadline,
        "Other Assignments": other_assignments,
        "Hours": hours,
        "Difficulty": difficulty
    }

    # Display the user's input
    st.write("Your answers:")
    st.json(user_data)

    # Save the data to a file
    with open("user_data.txt", "a") as f:
        f.write(f"{user_data}\n")

    st.success("Your answers have been saved! Start your session!")

# Initialize session state for stopwatch
if 'stopwatch_running' not in st.session_state:
    st.session_state.stopwatch_running = False
    st.session_state.start_time = 0.0
    st.session_state.elapsed_time = 0.0
    st.session_state.questions_asked = []  
    st.session_state.period = 1  

# Stopwatch functions
def start_stopwatch():
    if not st.session_state.stopwatch_running:
        st.session_state.stopwatch_running = True
        st.session_state.start_time = time.time() - st.session_state.elapsed_time

def stop_stopwatch():
    if st.session_state.stopwatch_running:
        st.session_state.elapsed_time = time.time() - st.session_state.start_time
        st.session_state.stopwatch_running = False

def reset_stopwatch():
    st.session_state.stopwatch_running = False
    st.session_state.elapsed_time = 0.0


# Time Format
def format_time(seconds):
    return time.strftime("%H:%M:%S", time.gmtime(seconds))

# Stopwatch Button
col1, col2, col3 = st.columns(3)
with col1:
    if st.button("Start"):
        start_stopwatch()
with col2:
    if st.button("Stop"):
        stop_stopwatch()
with col3:
    if st.button("Reset"):
        reset_stopwatch()

# Display stopwatch 
placeholder = st.empty()
placeholder1 = st.empty()
while st.session_state.stopwatch_running:
    st.session_state.elapsed_time = time.time() - st.session_state.start_time
    placeholder1.write(f"Elapsed Time (H:M:S): {format_time(st.session_state.elapsed_time)}")
    time.sleep(0.1) 

# Display final elapsed time g
placeholder1.write(f"Elapsed Time (H:M:S): {format_time(st.session_state.elapsed_time)}")

# Display period count
st.write(f"Current Period: {st.session_state.period}")

# New questions per period
difficulty_periodic = st.selectbox("On a scale of 1-5, how difficult is your assignment so far (5 being the most difficult)", [1, 2, 3, 4, 5])
efficiency_score = st.selectbox("On a scale of 1-5, how would you rate your efficiency during this study session?", [1, 2, 3, 4, 5])

# Save answers
response_data = {
    "Period": st.session_state.period,  
    "Difficulty_Periodic": difficulty_periodic,
    "Efficiency_Score": efficiency_score  #
}

if st.button("Save Responses"):
    st.session_state.period += 1  

    with open("user_data.txt", "a") as f:
        f.write(f"{response_data}\n")
        st.success("Your responses have been saved! You can resume the session.")

    st.session_state.questions_asked.append(response_data)
