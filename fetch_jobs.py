import requests, json
from dotenv import load_dotenv
import os
import sys
load_dotenv()
sys.stdout.reconfigure(encoding="utf-8")
FORUM_ID = os.getenv("FORUM_ID")
FORUM_URL = os.getenv("FORUM_URL")
TOKEN = os.getenv("TOKEN")

H = {"Authorization" : f"Bot {TOKEN}"}
r = requests.get(FORUM_URL, headers=H)
data = r.json()

threads = [t for t in data["threads"] if t["parent_id"] == FORUM_ID]
for t in threads: print(t["name"])