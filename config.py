from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Database
DATABASE = os.getenv("DATABASE", "emails.db")

# Model path
MODEL_PATH = "models/"
