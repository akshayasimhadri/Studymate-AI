import streamlit as st
from datetime import date

from database.db import add_task

st.set_page_config(page_title="Add Task", page_icon="📝")

st.title("📝 Add Study Task")

st.markdown("Enter your study task details below.")

with st.form("task_form"):

    subject = st.text_input("📚 Subject")

    task_name = st.text_input("📝 Task Name")

    deadline = st.date_input(
        "📅 Deadline",
        min_value=date.today()
    )

    difficulty = st.selectbox(
        "💪 Difficulty",
        [
            "Easy",
            "Medium",
            "Hard"
        ]
    )

    estimated_hours = st.number_input(
        "⏳ Estimated Study Hours",
        min_value=1.0,
        max_value=100.0,
        value=2.0,
        step=0.5
    )

    submitted = st.form_submit_button("➕ Save Task")

if submitted:

    if subject == "" or task_name == "":

        st.error("Please fill all required fields.")

    else:

        # Simple priority calculation
        if difficulty == "Hard":
            priority = "High"
        elif difficulty == "Medium":
            priority = "Medium"
        else:
            priority = "Low"

        add_task(
            subject,
            task_name,
            str(deadline),
            difficulty,
            estimated_hours,
            priority
        )

        st.success("✅ Task Added Successfully!")

        st.balloons()