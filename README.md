# 📊 YouTube Trending Data Pipeline

A simple real-time data pipeline that fetches trending YouTube videos using the YouTube Data API, stores them in a SQL database, and visualizes them in a Streamlit dashboard.

---

## 🔧 Tools Used
- Python
- YouTube Data API
- SQLite (SQL)
- pandas
- Streamlit
- matplotlib

---

## 🔄 How It Works
1. `realtime_to_sql.py` fetches trending videos and saves them to a SQL database.
2. `dashboard_app.py` loads that data and shows:
   - Top viewed videos
   - Like ratio
   - Search by channel

---

## ▶️ Run This Project

```bash
pip install -r requirements.txt
python realtime_to_sql.py
streamlit run dashboard_app.py
