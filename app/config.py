from dotenv import load_dotenv, find_dotenv
import os

# Load .env automatically
load_dotenv(find_dotenv())

# Secrets / Config
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
MONGODB_URI = os.getenv("MONGODB_URI")

if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY is missing in .env")

if not MONGODB_URI:
    raise ValueError("MONGODB_URI is missing in .env")