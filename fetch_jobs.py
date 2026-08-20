import os, json, requests
from dotenv import load_dotenv
load_dotenv(override=True)
TOKEN = os.environ["DISCORD_TOKEN"]
GUILD_ID = "1034068769343033344"
FORUM_ID = "1537837461562982493"

H = {"Authorization": f"Bot {TOKEN}"}
url = f"https://discord.com/api/v10/guilds/{GUILD_ID}/threads/active"

r = requests.get(url, headers=H)
r.raise_for_status()          # 失敗したらここで止まる
data = r.json()

jobs = [
    {"title": t["name"]}
    for t in data["threads"]
]

with open("jobs.json", "w", encoding="utf-8") as f:
    json.dump({"jobs": jobs}, f, ensure_ascii=False, indent=2)
