import re

def extract_meeting(text):

    date = re.findall(r"\d{1,2}/\d{1,2}/\d{4}", text)
    time = re.findall(r"\d{1,2}:\d{2}", text)

    return {
        "date": date[0] if date else None,
        "time": time[0] if time else None
    }
