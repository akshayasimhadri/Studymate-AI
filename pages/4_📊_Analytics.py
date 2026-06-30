import streamlit as st
import pandas as pd
import plotly.express as px
from database.db import get_tasks

st.set_page_config(
    page_title="Analytics",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Study Analytics")

tasks = get_tasks()

if len(tasks) == 0:
    st.info("No data available.")
    st.stop()

columns = [
    "ID",
    "Subject",
    "Task",
    "Deadline",
    "Difficulty",
    "Hours",
    "Priority",
    "Status"
]

df = pd.DataFrame(tasks, columns=columns)

st.subheader("📈 Study Hours by Subject")

hours_df = df.groupby("Subject")["Hours"].sum().reset_index()

fig1 = px.bar(
    hours_df,
    x="Subject",
    y="Hours",
    title="Study Hours"
)

st.plotly_chart(fig1, use_container_width=True)

st.divider()

st.subheader("🔥 Tasks by Priority")

priority_df = df.groupby("Priority").size().reset_index(name="Count")

fig2 = px.pie(
    priority_df,
    names="Priority",
    values="Count",
    title="Priority Distribution"
)

st.plotly_chart(fig2, use_container_width=True)

st.divider()

st.subheader("✅ Task Status")

status_df = df.groupby("Status").size().reset_index(name="Count")

fig3 = px.bar(
    status_df,
    x="Status",
    y="Count",
    title="Task Status"
)

st.plotly_chart(fig3, use_container_width=True)

st.divider()

st.subheader("📚 Subject Distribution")

subject_df = df.groupby("Subject").size().reset_index(name="Tasks")

fig4 = px.pie(
    subject_df,
    names="Subject",
    values="Tasks",
    title="Tasks by Subject"
)

st.plotly_chart(fig4, use_container_width=True)

st.divider()

total = len(df)
completed = len(df[df["Status"] == "Completed"])

score = round((completed / total) * 100, 2)

st.metric(
    "🎯 Productivity Score",
    f"{score}%"
)

if score >= 80:
    st.success("Excellent consistency! 🎉")
elif score >= 50:
    st.warning("You're making good progress. Keep going!")
else:
    st.error("Let's improve your study consistency.")
    