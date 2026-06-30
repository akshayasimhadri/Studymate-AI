from datetime import datetime


def days_left(deadline):

    today = datetime.today().date()

    deadline = datetime.strptime(
        deadline,
        "%Y-%m-%d"
    ).date()

    return (deadline - today).days


def productivity_score(total, completed):

    if total == 0:
        return 0

    return round((completed / total) * 100, 2)