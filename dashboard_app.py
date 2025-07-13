import streamlit as st
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Connect to SQLite
conn = sqlite3.connect("youtube_data.db")

# Load data
df = pd.read_sql("SELECT * FROM trending_videos", conn)

st.title("📊 YouTube Trending Dashboard")

# Metrics
st.metric("Total Videos", len(df))
st.metric("Total Views", f"{df['views'].sum():,}")
st.metric("Average Like Ratio", round(df['like_ratio'].mean(), 2))

# Bar chart: Top 5 by views
st.subheader("🔥 Top 5 Trending Videos (Views)")
top = df.sort_values("views", ascending=False).head(5)
fig, ax = plt.subplots()
ax.barh(top["title"], top["views"], color="orange")
ax.invert_yaxis()
st.pyplot(fig)

# Search by channel
st.subheader("🔍 Search by Channel")
channel = st.text_input("Enter channel name:")
if channel:
    results = df[df["channel"].str.contains(channel, case=False)]
    st.dataframe(results)

st.caption("Made by Aditya 💻")
