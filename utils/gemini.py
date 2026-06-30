import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.0-flash")


def ai_task_priority(subject, task, deadline, difficulty, hours):

    prompt = f"""
You are an expert productivity assistant.

Analyze this task.

Subject: {subject}
Task: {task}
Deadline: {deadline}
Difficulty: {difficulty}
Estimated Hours: {hours}

Return ONLY ONE WORD.

Critical
High
Medium
Low
"""

    try:

        response = model.generate_content(prompt)

        priority = response.text.strip()

        if priority not in ["Critical", "High", "Medium", "Low"]:
            priority = "Medium"

        return priority

    except:

        if difficulty == "Hard":
            return "High"

        elif difficulty == "Medium":
            return "Medium"

        return "Low"


def generate_study_plan(task, subject, deadline, difficulty, hours):

    prompt = f"""
You are StudyMate AI.

Create a personalized study plan.

Subject: {subject}

Task: {task}

Deadline: {deadline}

Difficulty: {difficulty}

Estimated Study Hours: {hours}

Generate:

1. Priority

2. Day-wise Schedule

3. Task Breakdown

4. Deadline Risk

5. Productivity Tips

6. Motivation

Return in Markdown.
"""

    try:

        response = model.generate_content(prompt)

        return response.text

    except:

        return f"""
# 📚 AI Study Plan

## Priority
{ai_task_priority(subject, task, deadline, difficulty, hours)}

## Day-wise Schedule

Day 1
- Read concepts

Day 2
- Practice problems

Day 3
- Revise

## Task Breakdown

- Read
- Notes
- Practice
- Revision

## Deadline Risk

Medium

## Productivity Tips

- Study in 50-minute sessions.
- Turn off notifications.
- Drink enough water.
- Revise daily.
- Sleep well.

## Motivation

Keep going. Small daily progress leads to success.
"""