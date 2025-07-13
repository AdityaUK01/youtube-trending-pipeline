from googleapiclient.discovery import build
import pandas as pd
import sqlite3
from datetime import datetime

# Your API Key here
API_KEY = "AIzaSyCYbffFHME6upTCEclfOTo0DvR8rUueB44"
REGION_CODE = "IN"
MAX_RESULTS = 10

# Step 1: Fetch from YouTube API
youtube = build("youtube", "v3", developerKey=API_KEY)
request = youtube.videos().list(
    part="snippet,statistics",
    chart="mostPopular",
    regionCode=REGION_CODE,
    maxResults=MAX_RESULTS
)
response = request.execute()

# Step 2: Extract video data
videos = []
for item in response["items"]:
    video = {
        "title": item["snippet"]["title"],
        "channel": item["snippet"]["channelTitle"],
        "views": int(item["statistics"].get("viewCount", 0)),
        "likes": int(item["statistics"].get("likeCount", 0)),
        "tags": ", ".join(item["snippet"].get("tags", [])),
        "published": item["snippet"]["publishedAt"]
    }
    videos.append(video)

# Step 3: Create DataFrame and clean
df = pd.DataFrame(videos)
df['published'] = pd.to_datetime(df['published'])
df['like_ratio'] = (df['likes'] / df['views']).round(2)

# Step 4: Save to SQLite
conn = sqlite3.connect('youtube_data.db')
df.to_sql('trending_videos', conn, if_exists='replace', index=False)

# Step 5: Sample query
result = pd.read_sql("SELECT title, views FROM trending_videos ORDER BY views DESC LIMIT 3", conn)
print("✅ Top 3 trending videos:\n", result)

conn.close()
