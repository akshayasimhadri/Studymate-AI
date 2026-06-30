import streamlit as st
import sqlite3
import os

st.set_page_config(
    page_title="Settings",
    page_icon="⚙️",
    layout="wide"
)

st.title("⚙️ Settings")

st.divider()

st.subheader("📖 About StudyMate AI")

st.info("""
StudyMate AI is an AI-powered productivity companion that helps students:

✅ Plan their studies

✅ Prioritize assignments

✅ Generate AI study plans

✅ Track deadlines

✅ Improve productivity

Built using:

• Streamlit

• Google Gemini AI

• SQLite

• Plotly
""")

st.divider()

st.subheader("🔑 Gemini API")

if os.getenv("GEMINI_API_KEY"):
    st.success("Gemini API Key Loaded Successfully")
else:
    st.error("Gemini API Key Not Found")

st.divider()

st.subheader("💾 Database")

if st.button("Reset Database"):

    conn = sqlite3.connect("data/studymate.db")
    cursor = conn.cursor()

    cursor.execute("DELETE FROM tasks")

    conn.commit()
    conn.close()

    st.success("Database Reset Successfully!")

st.divider()

st.subheader("👨‍💻 Developer")

st.write("StudyMate AI")
st.write("Built for AI Productivity Hackathon")

st.divider()

st.subheader("🚀 Version")

st.write("Version 1.0")