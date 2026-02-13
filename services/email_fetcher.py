import os.path
import base64

from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

SCOPES = ["https://www.googleapis.com/auth/gmail.readonly"]

def fetch_emails():

    creds = None

    # Load saved login
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)

    # First time login
    if not creds or not creds.valid:
        flow = InstalledAppFlow.from_client_secrets_file(
            "credentials.json", SCOPES
        )
        creds = flow.run_local_server(port=0)

        with open("token.json", "w") as token:
            token.write(creds.to_json())

    service = build("gmail", "v1", credentials=creds)

    results = service.users().messages().list(
        userId="me", maxResults=5
    ).execute()

    messages = results.get("messages", [])

    emails = []

    for msg in messages:
        txt = service.users().messages().get(
            userId="me", id=msg["id"]
        ).execute()

        payload = txt["payload"]
        headers = payload["headers"]

        subject = ""
        for d in headers:
            if d["name"] == "Subject":
                subject = d["value"]

        emails.append(subject)

    return emails
