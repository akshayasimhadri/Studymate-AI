from datetime import datetime


def calculate_priority(deadline, difficulty, estimated_hours):
    """
    Returns:
    Critical
    High
    Medium
    Low
    """

    today = datetime.today().date()
    deadline = datetime.strptime(deadline, "%Y-%m-%d").date()

    days_left = (deadline - today).days

    score = 0

    if days_left <= 1:
        score += 5
    elif days_left <= 3:
        score += 4
    elif days_left <= 7:
        score += 3
    else:
        score += 1

    if difficulty == "Hard":
        score += 3
    elif difficulty == "Medium":
        score += 2
    else:
        score += 1

    if estimated_hours >= 8:
        score += 3
    elif estimated_hours >= 4:
        score += 2
    else:
        score += 1

    if score >= 10:
        return "Critical"
    elif score >= 8:
        return "High"
    elif score >= 5:
        return "Medium"
    else:
        return "Low"