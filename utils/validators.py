def validate_task(subject, task):

    if subject.strip() == "":
        return False

    if task.strip() == "":
        return False

    return True