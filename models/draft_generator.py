def generate_draft(text):

    if "meeting" in text.lower():
        return "Thank you for the meeting invitation. I will attend."

    if "deadline" in text.lower():
        return "Acknowledged. I will complete it on time."

    return "Thank you for your email. I will get back to you."
