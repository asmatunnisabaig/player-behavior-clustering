# 🎮 Survival Arena Game

A browser-based survival game paired with a live machine learning pipeline that classifies player behavior in real time.

## What it does
- Players dodge incoming obstacles in an HTML5 Canvas game embedded in a Streamlit app
- Each round's stats (survival time, distance moved) are sent to a Supabase (PostgreSQL) database
- A K-Means clustering model (scikit-learn) groups all recorded sessions into playstyles — Quick Faller, Balanced Player, Long Survivor
- The dashboard shows the all-time best survival record and the most recent round's playstyle classification, auto-updating live

## Tech Stack
- **Frontend/Game:** HTML5 Canvas, JavaScript
- **Backend/Dashboard:** Python, Streamlit
- **Database:** Supabase (PostgreSQL)
- **Machine Learning:** scikit-learn (K-Means clustering, StandardScaler)
- **Deployment:** Streamlit Community Cloud

## Live Demo
🔗 [Play it here](https://player-behavior-clustering.streamlit.app/)

## What this demonstrates
- End-to-end data pipeline: raw event data → database → ML model → live dashboard
- Unsupervised learning applied to behavioral/gameplay data
- Full-stack integration across JavaScript, Python, and a cloud databasey
