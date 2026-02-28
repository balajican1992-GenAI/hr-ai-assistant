from dotenv import load_dotenv, find_dotenv
import os
import certifi

# Load .env automatically
load_dotenv(find_dotenv())

# Secrets / Config
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

CA_BUNDLE_PATH = (
    os.getenv("SSL_CERT_FILE")
    or os.getenv("REQUESTS_CA_BUNDLE")
    or certifi.where()
)

os.environ.setdefault("SSL_CERT_FILE", CA_BUNDLE_PATH)
os.environ.setdefault("REQUESTS_CA_BUNDLE", CA_BUNDLE_PATH)
os.environ.setdefault("CURL_CA_BUNDLE", CA_BUNDLE_PATH)

if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY is missing in .env")
