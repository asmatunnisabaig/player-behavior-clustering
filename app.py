import streamlit as st
import pandas as pd
from supabase import create_client
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import streamlit.components.v1 as components
from streamlit_autorefresh import st_autorefresh

SUPABASE_URL = "https://ytemypogbyqfzsklmvbk.supabase.co"
SUPABASE_KEY = "sb_publishable_X2FrVLll9yB1YnC8-sPJ0A_GJMy9uyy"
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

with open("index.html", "r") as f:
    game_html = f.read()

components.html(game_html, height=450)

st_autorefresh(interval=3000, key="stats_refresh")

response = supabase.table("sessions").select("*").execute()
df = pd.DataFrame(response.data)

if not df.empty:
    st.metric("Longest survival time ever", f"{df['survival_time'].max():.1f}s")

    if len(df) >= 3:
        features = df[["survival_time", "distance_moved"]]
        scaled = StandardScaler().fit_transform(features)
        kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
        df["cluster"] = kmeans.fit_predict(scaled)

        cluster_order = df.groupby("cluster")["survival_time"].mean().sort_values().index.tolist()
        labels = {cluster_order[0]: "Quick Faller", cluster_order[1]: "Balanced Player", cluster_order[2]: "Long Survivor"}
        df["playstyle"] = df["cluster"].map(labels)

        st.metric("This round's playstyle", df.iloc[-1]["playstyle"])
else:
    st.info("Play your first round!")