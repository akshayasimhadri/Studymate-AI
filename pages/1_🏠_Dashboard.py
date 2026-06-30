import streamlit as st
import pandas as pd
from database.db import get_tasks, update_status, delete_task

st.set_page_config(
    page_title="Dashboard",
    page_icon="🎓",
    layout="wide"
)

st.title("🎓 StudyMate AI")
st.caption("Your AI-Powered Productivity Companion")

tasks = get_tasks()

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

total = len(df)

completed = len(df[df["Status"] == "Completed"])

pending = len(df[df["Status"] == "Pending"])

critical = len(df[df["Priority"] == "Critical"])

progress = 0

if total != 0:
    progress = completed / total

# ------------------- HERO -------------------

st.markdown("## 📊 Productivity Overview")

c1, c2, c3, c4 = st.columns(4)

c1.metric("📚 Total Tasks", total)

c2.metric("✅ Completed", completed)

c3.metric("⌛ Pending", pending)

c4.metric("🔥 Critical", critical)

st.progress(progress)

st.write(f"### Productivity Score : **{round(progress*100)}%**")

st.divider()

# ------------------- AI SUMMARY -------------------

st.markdown("## 🤖 AI Summary")

if pending == 0:

    st.success("🎉 Amazing! You have completed all your tasks.")

elif critical > 0:

    st.error(
        "⚠️ You have critical tasks that should be completed immediately."
    )

elif pending > 5:

    st.warning(
        "📅 Your workload is increasing. Consider studying today."
    )

else:

    st.info(
        "😊 You're on track. Keep maintaining your consistency!"
    )

st.divider()

# ------------------- NEXT TASK -------------------

st.markdown("## 🚀 Next Recommended Task")

pending_df = df[df["Status"] == "Pending"]

if len(pending_df) != 0:

    order = {
        "Critical": 4,
        "High": 3,
        "Medium": 2,
        "Low": 1
    }

    pending_df = pending_df.copy()

    pending_df["Rank"] = pending_df["Priority"].map(order)

    best = pending_df.sort_values(
        by="Rank",
        ascending=False
    ).iloc[0]

    st.success(
        f"""
### 🎯 {best['Task']}

📚 Subject : **{best['Subject']}**

🔥 Priority : **{best['Priority']}**

📅 Deadline : **{best['Deadline']}**

⏳ Estimated Hours : **{best['Hours']}**
"""
    )

st.divider()

# ------------------- TASK TABLE -------------------

st.markdown("## 📋 Your Tasks")

if total == 0:

    st.info("No tasks available.")

else:

    for row in df.itertuples():

        with st.expander(
            f"{row.Task} ({row.Priority})"
        ):

            st.write(f"**Subject:** {row.Subject}")

            st.write(f"**Deadline:** {row.Deadline}")

            st.write(f"**Difficulty:** {row.Difficulty}")

            st.write(f"**Estimated Hours:** {row.Hours}")

            st.write(f"**Status:** {row.Status}")

            col1, col2 = st.columns(2)

            if row.Status == "Pending":

                if col1.button(
                    "✅ Complete",
                    key=f"c{row.ID}"
                ):

                    update_status(
                        row.ID,
                        "Completed"
                    )

                    st.rerun()

            if col2.button(
                "🗑 Delete",
                key=f"d{row.ID}"
            ):

                delete_task(row.ID)

                st.rerun()

st.divider()

# ------------------- MOTIVATION -------------------

quotes = [

    "🚀 Small progress every day leads to big success.",

    "📚 The secret of getting ahead is getting started.",

    "💪 Stay focused. Stay consistent.",

    "🌟 Success is built one task at a time.",

    "🎯 Finish today's work today."
]

import random

st.markdown("## 💡 Daily Motivation")

st.success(random.choice(quotes))