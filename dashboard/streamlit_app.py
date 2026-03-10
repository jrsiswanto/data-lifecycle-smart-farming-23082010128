import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.graph_objects as go

# Set Page
st.set_page_config(page_title="Soil Monitoring Dashboard", layout="wide")
st.title("🌱 Smart Farming: Soil Management Dashboard")

# 1. Load Data
@st.cache_data
def load_data():
    # Gunakan link Raw GitHub Anda di sini
    url = "data/raw/Smart_Farming_Sensor_Data.csv"
    df = pd.read_csv(url)
    
    # PERBAIKAN: Paksa semua nama kolom jadi huruf kecil dan hapus spasi
    df.columns = df.columns.str.strip().str.lower()
    return df

df = load_data()

# Sekarang avg_ph = df['ph'].mean() tidak akan error lagi 
# karena 'PH' atau 'ph ' sudah diubah menjadi 'ph'

df = load_data()

# --- ROW 1: GAUGE & ALERT ---
col1, col2 = st.columns(2)

with col1:
    st.subheader("📍 Current Soil pH (Gauge)")
    avg_ph = df['ph'].mean()
    fig_gauge = go.Figure(go.Indicator(
        mode = "gauge+number",
        value = avg_ph,
        title = {'text': "Average pH Level"},
        gauge = {'axis': {'range': [0, 14]},
                 'bar': {'color': "darkblue"},
                 'steps' : [
                     {'range': [0, 6], 'color': "red"},
                     {'range': [6, 8], 'color': "green"},
                     {'range': [8, 14], 'color': "yellow"}]}
    ))
    st.plotly_chart(fig_gauge, use_container_width=True)

with col2:
    st.subheader("⚠️ Alert System")
    # Logika Alert: Jika pH terlalu asam atau kelembaban rendah
    low_ph = df[df['ph'] < 5].shape[0]
    if low_ph > 0:
        st.error(f"ALERT: Terdeteksi {low_ph} sampel tanah dengan pH sangat asam (di bawah 5.0)!")
    else:
        st.success("Kondisi pH tanah stabil.")
    
    st.info("Rekomendasi: Lakukan pengapuran jika indikator berwarna merah.")

# --- ROW 2: HEATMAP & TREND ---
col3, col4 = st.columns(2)

with col3:
    st.subheader("🔥 Nutrient Heatmap")
    fig_heat, ax_heat = plt.subplots()
    sns.heatmap(df[['N', 'P', 'K', 'ph', 'temperature', 'humidity', 'rainfall']].corr(), 
                annot=True, cmap='YlGnBu', ax=ax_heat)
    st.pyplot(fig_heat)

with col4:
    st.subheader("📈 Nutrient Distribution (Time Series Proxy)")
    # Karena data soil biasanya tidak punya kolom 'Date', 
    # kita gunakan Index sebagai urutan pengambilan data (Proxy Time Series)
    fig_line, ax_line = plt.subplots()
    st.line_chart(df[['N', 'P', 'K']].head(100)) 
    st.caption("Menampilkan tren 100 sampel data pertama sebagai urutan waktu.")

st.divider()
st.write("Data Source: data/raw/smartfarmingsensor/soil_measures.csv")
