from datetime import datetime, timedelta


def create_schedule(task, hours):

    schedule = []

    start = datetime.strptime("09:00", "%H:%M")

    remaining = hours

    while remaining > 0:

        end = start + timedelta(hours=1)

        schedule.append(
            {
                "Task": task,
                "Start": start.strftime("%I:%M %p"),
                "End": end.strftime("%I:%M %p"),
            }
        )

        start = end + timedelta(minutes=15)

        remaining -= 1

    return schedule