import streamlit as st
import time

# Title of the app
st.title("Study Sessions Collection")

# Asking the user initial questions
name = st.text_input("What is your name?")
assignment = st.text_input("What assignment are you currently working on?")
deadline = st.text_input("How many days is the assignment due?")
other_assignments = st.text_input("How many other assignments do you also have around that deadline?")
hours = st.text_input("How many hours do you think this assignment will take?")
difficulty = st.selectbox("On a scale of 1-5, how difficult is your assignment (5 being the most difficult)", [1, 2, 3, 4, 5])

# Button to submit the answers
if st.button("Submit"):
    # Save the answers to a dictionary (or a file/database if needed)
    user_data = {
        "Name": name,
        "Assignment": assignment,
        "Deadline": deadline,
        "Other Assignments": other_assignments,
        "Hours": hours,
        "Difficulty": difficulty
    }

    # Display the user's input
    st.write("Your answers:")
    st.json(user_data)

    # Optionally, save the data to a file
    with open("user_data.txt", "a") as f:
        f.write(f"{user_data}\n")

    st.success("Your answers have been saved! Start your session!")

# Initialize session state for the stopwatch if it's the first run
if 'stopwatch_running' not in st.session_state:
    st.session_state.stopwatch_running = False
    st.session_state.start_time = 0.0
    st.session_state.elapsed_time = 0.0
    st.session_state.question_time = 30  # Every 30 seconds for new questions
    st.session_state.questions_asked = []  # To track sets of questions


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


# Convert seconds to Hours:Minutes:Seconds format
def format_time(seconds):
    return time.strftime("%H:%M:%S", time.gmtime(seconds))

# Buttons to control the stopwatch
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

# Display stopwatch with real-time updates
placeholder = st.empty()
placeholder1 = st.empty()
while st.session_state.stopwatch_running:
    st.session_state.elapsed_time = time.time() - st.session_state.start_time
    placeholder.write(f"Elapsed Time: {st.session_state.elapsed_time:.2f} seconds")
    placeholder1.write(f"Elapsed Time (H:M:S): {format_time(st.session_state.elapsed_time)}")
    time.sleep(0.1)  # Update every 100 ms

# Display final elapsed time when not running
placeholder.write(f"Elapsed Time: {st.session_state.elapsed_time:.2f} seconds")
placeholder1.write(f"Elapsed Time (H:M:S): {format_time(st.session_state.elapsed_time)}")

# New questions
focus = st.selectbox("How focused were you in the last 30 minutes?", ["Very focused", "Somewhat focused", "Not focused"])
distractions = st.text_input("Were there any distractions? If yes, what were they?")
hours_periodic = st.text_input("How many more hours do you think this assignment will take?")
difficulty_periodic = st.selectbox("On a scale of 1-5, how difficult is your assignment so far (5 being the most difficult)", [1, 2, 3, 4, 5])

# Save answers and elapsed time
response_data = {
    "Elapsed Time": f"{st.session_state.elapsed_time:.2f} seconds",
    "Focus": focus,
    "Distractions": distractions,
    "Hours_Periodic": hours_periodic,
    "Difficulty_Periodic": difficulty_periodic
    }

if st.button("Save Responses"):
    with open("user_data.txt", "a") as f:
        f.write(f"{response_data}\n")
        st.success("Your responses have been saved! You can resume the session.")

st.session_state.questions_asked.append(response_data)


commented = ('''
# Check if 30 seconds have passed and pause the stopwatch
if st.session_state.elapsed_time >= st.session_state.question_time:
    # Auto-pause the stopwatch
    stop_stopwatch()
    st.session_state.question_time += 30  # Set the next interval

    # Notify the user of the break
    st.warning("Break Time! Please answer the following questions.")

    # New questions
    focus = st.selectbox("How focused were you in the last 30 seconds?", ["Very focused", "Somewhat focused", "Not focused"])
    distractions = st.text_input("Were there any distractions? If yes, what were they?")
    hours_periodic = st.text_input("How many more hours do you think this assignment will take?")
    difficulty_periodic = st.selectbox("On a scale of 1-5, how difficult is your assignment so far (5 being the most difficult)", [1, 2, 3, 4, 5])

    # Save answers and elapsed time
    response_data = {
        "Elapsed Time": f"{st.session_state.elapsed_time:.2f} seconds",
        "Focus": focus,
        "Distractions": distractions,
        "Hours_Periodic": hours_periodic,
        "Difficulty_Periodic": difficulty_periodic
    }

    if st.button("Save Responses"):
        with open("user_data.txt", "a") as f:
            f.write(f"{response_data}\n")
        st.success("Your responses have been saved! You can resume the session.")

    st.session_state.questions_asked.append(response_data)

    # Allow user to restart the stopwatch manually after submitting
    if st.button("Resume Stopwatch"):
        start_stopwatch()

''')