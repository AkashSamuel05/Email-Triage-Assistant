import os
import base64

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

SCOPES = ["https://www.googleapis.com/auth/gmail.readonly"]


# -----------------------------
# AUTHENTICATION
# -----------------------------
def get_gmail_service():
    creds = None

    BASE_DIR = os.path.abspath(os.getcwd())
    token_path = os.path.join(BASE_DIR, "token.json")
    cred_path = os.path.join(BASE_DIR, "credentials.json")

    # Load saved login
    if os.path.exists(token_path):
        creds = Credentials.from_authorized_user_file(token_path, SCOPES)

    # If not valid → login
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            if not os.path.exists(cred_path):
                raise Exception("credentials.json not found in project root")

            flow = InstalledAppFlow.from_client_secrets_file(
                cred_path, SCOPES
            )
            creds = flow.run_local_server(port=0)

        # Save token
        with open(token_path, "w") as token:
            token.write(creds.to_json())

    return build("gmail", "v1", credentials=creds)


# -----------------------------
# FETCH EMAILS
# -----------------------------
def fetch_emails():
    try:
        service = get_gmail_service()

        results = service.users().messages().list(
            userId="me",
            maxResults=5
        ).execute()

        messages = results.get("messages", [])
        emails = []

        for msg in messages:
            msg_data = service.users().messages().get(
                userId="me",
                id=msg["id"]
            ).execute()

            payload = msg_data["payload"]
            headers = payload.get("headers", [])

            subject = "No Subject"

            for h in headers:
                if h["name"] == "Subject":
                    subject = h["value"]

            emails.append(subject)

        return emails

    except Exception as e:
        print("Gmail Error:", e)
        return ["Unable to fetch Gmail — Check API connection"]
