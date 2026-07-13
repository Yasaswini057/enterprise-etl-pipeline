import os
from dotenv import load_dotenv

load_dotenv()

print("Username:", os.getenv("SF_USERNAME"))
print("Password Loaded:", os.getenv("SF_PASSWORD") is not None)
print("Token Loaded:", os.getenv("SF_SECURITY_TOKEN") is not None)