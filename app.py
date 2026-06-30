import streamlit as st
from database.schema import initialize_database

initialize_database()

st.set_page_config(
    page_title="StudyMate AI",
    page_icon="🎓",
    layout="wide"
)

st.title("🎓 StudyMate AI")

st.subheader("Your Intelligent Study & Deadline Companion")

st.markdown("---")

st.markdown("""
### 🚀 Features

- 📝 Add Study Tasks
- 🤖 AI Study Planner
- 📅 Smart Schedule
- ⚠️ Deadline Risk Analysis
- 📊 Analytics Dashboard
- 🎯 Productivity Insights

---

### 💡 How It Works

1. Add your study tasks.
2. Let AI analyze your workload.
3. Receive a personalized study plan.
4. Track your progress.
5. Never miss a deadline again!

---

👈 Use the sidebar to navigate through the app.
""")