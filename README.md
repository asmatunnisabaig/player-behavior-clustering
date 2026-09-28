# 🎮 Survival Arena Game

A browser-based survival game paired with a live machine learning pipeline that classifies player behavior in real time.

## What it does
- Players dodge incoming obstacles in an HTML5 Canvas game embedded in a Streamlit app
- Each round's stats (survival time, distance moved) are sent to a Supabase (PostgreSQL) database
- A K-Means clustering model (scikit-learn) groups recorded sessions into playstyles (Quick Faller, Balanced Player, Long Survivor) using two features: survival time and average speed (distance moved ÷ survival time)
- A silhouette score is shown alongside the classification to quantify how well-separated the clusters are

## How the ML works
- **Features:** survival time and average speed. Average speed was engineered because raw distance moved simply grows with survival time and adds no independent signal.
- **StandardScaler:** K-Means relies on distance between points, so features on different scales (seconds vs. pixels per second) would let one dominate. Scaling puts both on the same footing.
- **K-Means (k=3):** there are no pre-labeled playstyles to predict, so an unsupervised method is used to discover natural groupings in the data.
- **Labeling:** clusters are ranked by mean survival time and named Quick Faller, Balanced Player, and Long Survivor.
- **Validation:** silhouette score is computed on every refresh.

## Limitations
- Cluster boundaries are relative to all recorded sessions, so labels shift as more data comes in.
- Clusters are only statistically meaningful with a reasonable number of sessions.
- Supabase row-level security is disabled for demo simplicity, so this is not production-grade.

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
