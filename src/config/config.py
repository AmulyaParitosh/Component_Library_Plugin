import os

from dotenv import load_dotenv

load_dotenv()

class Config:
	API_URL = "http://127.0.0.1:5000"
	GITHUB_ACCESS_TOKEN = os.getenv("ACCESS_TOKEN", "")
