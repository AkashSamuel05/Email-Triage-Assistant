def check_followup(text):

    keywords = ["reply", "respond", "waiting", "feedback"]

    for k in keywords:
        if k in text.lower():
            return True

    return False
