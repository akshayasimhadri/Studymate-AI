import streamlit as st
from database.db import get_tasks
from utils.gemini import generate_study_plan

st.set_page_config(
    page_title="AI Study Planner",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI Study Planner")

st.write(
    "Generate a personalized study plan using Google Gemini AI."
)

tasks = get_tasks()

if len(tasks) == 0:
    st.warning("Please add at least one task first.")
    st.stop()

task_names = [f"{task[2]} ({task[1]})" for task in tasks]

selected_task = st.selectbox(
    "Select a Task",
    task_names
)

selected_index = task_names.index(selected_task)

task = tasks[selected_index]

subject = task[1]
task_name = task[2]
deadline = task[3]
difficulty = task[4]
hours = task[5]

st.divider()

col1, col2 = st.columns(2)

with col1:
    st.info(f"**Subject:** {subject}")
    st.info(f"**Task:** {task_name}")
    st.info(f"**Deadline:** {deadline}")

with col2:
    st.info(f"**Difficulty:** {difficulty}")
    st.info(f"**Estimated Hours:** {hours}")
    st.info(f"**Priority:** {task[6]}")

st.divider()

if st.button("🚀 Generate AI Study Plan"):

    with st.spinner("StudyMate AI is creating your personalized plan..."):

        result = generate_study_plan(
            task_name,
            subject,
            deadline,
            difficulty,
            hours
        )

    st.success("Study Plan Generated Successfully!")

    st.markdown(result)