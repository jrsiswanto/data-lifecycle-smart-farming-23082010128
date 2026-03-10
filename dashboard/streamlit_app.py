import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.graph_objects as go

st.set_page_config(page_title="Smart Farming Dashboard", layout="wide")
st.title("🌱 Smart Farming: Sensor Monitoring Dashboard")

@st.cache_data
def load_data():
    # Masukkan link RAW GitHub Anda di sini
    url = "data/raw/Smart_Farming_Sensor_Data.csv"
    df = pd.read_csv(url)
    df.columns = df.columns.str.strip().str.lower()
    return df

df = load_data()

if not df.empty:
    # --- 1. GAUGE CHART (Visualisasi Utama) ---
    st.subheader("📍 1. Rata-rata Kelembaban (Moisture 0)")
    avg_val = df['moisture0'].mean()
    
    fig_gauge = go.Figure(go.Indicator(
        mode = "gauge+number",
        value = avg_val,
        gauge = {'axis': {'range': [0, 1]}, # Karena data Anda skala desimal (0.1 - 0.5)
                 'bar': {'color': "royalblue"},
                 'steps' : [
                     {'range': [0, 0.3], 'color': "red"},
                     {'range': [0.3, 0.7], 'color': "green"},
                     {'range': [0.7, 1], 'color': "blue"}]}
    ))
    st.plotly_chart(fig_gauge, use_container_width=True)

    # --- 2. ALERT SYSTEM (Kriteria Peringatan) ---
    st.subheader("⚠️ 2. Status Sistem & Alert")
    if avg_val < 0.2:
        st.error("KONDISI KRITIS: Kelembaban sangat rendah! Sistem Irigasi WAJIB AKTIF.")
    elif 0.2 <= avg_val <= 0.5:
        st.success("KONDISI AMAN: Kelembaban tanah dalam rentang optimal untuk tanaman.")
    else:
        st.warning("PERINGATAN: Tanah terlalu basah, risiko pembusukan akar.")

    col1, col2 = st.columns(2)

    with col1:
        # --- 3. HEATMAP (Korelasi antar Sensor) ---
        st.subheader("🔥 3. Heatmap Korelasi Sensor")
        fig_heat, ax_heat = plt.subplots()
        # Mengambil kolom moisture saja untuk korelasi
        moisture_cols = [c for c in df.columns if 'moisture' in c]
        sns.heatmap(df[moisture_cols].corr(), annot=True, cmap='YlGnBu', ax=ax_heat)
        st.pyplot(fig_heat)

    with col2:
        # --- 4. TIME SERIES / TREND (Perubahan Seiring Waktu) ---
        st.subheader("📈 4. Tren Kelembaban (Time Series)")
        # Kita ambil 100 data terakhir untuk melihat tren
        df_trend = df[moisture_cols].tail(100)
        st.line_chart(df_trend)
        st.caption("Menampilkan tren fluktuasi dari 5 sensor moisture berbeda.")

else:
    st.error("Gagal membaca database. Pastikan link RAW sudah benar.")
