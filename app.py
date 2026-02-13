from flask import Flask, render_template, request
from database.db import create_table, connect_db

from services.email_fetcher import fetch_emails
from services.smart_folders import assign_folder

from models.classifier import classify_email
from models.priority import detect_priority
from models.summarizer import summarize_email
from models.draft_generator import generate_draft
from models.meeting_extractor import extract_meeting
from models.followup import check_followup

app = Flask(__name__)

create_table()


# -------------------------------
# HOME DASHBOARD
# -------------------------------

@app.route("/")
def dashboard():

    emails = []
    stats = {"total": 0}

    try:
        emails = fetch_emails()
        stats["total"] = len(emails)
    except:
        emails = ["Unable to fetch emails"]

    return render_template("dashboard.html", emails=emails, stats=stats)

# -------------------------------
# VIEW SINGLE EMAIL
# -------------------------------
@app.route("/view/<int:index>")
def view_email(index):

    emails = fetch_emails()

    if index >= len(emails):
        return "Email not found"

    email = emails[index]

    category = classify_email(email)
    priority = detect_priority(email)
    summary = summarize_email(email)
    draft = generate_draft(email)
    meeting = extract_meeting(email)
    followup = check_followup(email)
    folder = assign_folder(category)

    result = {
        "content": email,
        "category": category,
        "priority": priority,
        "summary": summary,
        "draft": draft,
        "meeting": meeting,
        "followup": followup,
        "folder": folder
    }

    return render_template("view_email.html", result=result)



# -------------------------------
# ANALYZE EMAIL PAGE
# -------------------------------
@app.route("/analyze", methods=["GET", "POST"])
def analyze():

    results = None

    if request.method == "POST":
        email = request.form.get("email_text")

        category = classify_email(email)
        priority = detect_priority(email)
        summary = summarize_email(email)
        draft = generate_draft(email)
        meeting = extract_meeting(email)
        followup = check_followup(email)
        folder = assign_folder(category)

        conn = connect_db()
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO emails(content,category,priority,summary) VALUES(?,?,?,?)",
            (email, category, priority, summary)
        )

        conn.commit()
        conn.close()

        results = {
            "content": email,
            "category": category,
            "priority": priority,
            "summary": summary,
            "draft": draft,
            "meeting": meeting,
            "followup": followup,
            "folder": folder
        }

    return render_template("analyze.html", results=results)


# -------------------------------
# EMAIL HISTORY PAGE
# -------------------------------
@app.route("/history")
def history():

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM emails")
    data = cursor.fetchall()

    conn.close()

    return render_template("history.html", emails=data)


# -------------------------------
# ABOUT PAGE
# -------------------------------
@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=True)
