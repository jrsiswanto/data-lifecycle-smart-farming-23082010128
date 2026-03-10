# Proyek Data Lifecycle Management: Smart Farming Sensor Monitoring

Proyek ini disusun untuk memenuhi tugas mata kuliah **Manajemen Siklus Hidup Data** (Data Lifecycle Management) pada Semester 6. Proyek ini mendemonstrasikan pengelolaan data dari tahap akuisisi hingga visualisasi dan tata kelola (governance).

## Identitas Mahasiswa
* **Nama:** Jonatan Risa Siswanto
* **NIM:** 23082010128
* **Mata Kuliah:** Big data & Iot
* **Semester:** 6 (Genap)
* **Program Studi:** Sistem Informasi

---

## 🚀 Link Dashboard Publik
Akses dashboard interaktif melalui tautan berikut:
👉 [Smart Farming Dashboard - Streamlit](https://data-lifecycle-smart-farming-23082010128-kffozgpsflunh96bs9bbp.streamlit.app/)

---

## 📊 Penjelasan Data Lifecycle (6 Tahapan)

Proyek ini mengikuti metodologi Data Lifecycle Management (DLM) sebagai berikut:

### 1. Data Acquisition (Akuisisi Data)
Data diperoleh dari sensor IoT pertanian yang mencatat tingkat kelembaban tanah (`moisture0` - `moisture4`) berdasarkan urutan waktu (tahun, bulan, hari, jam, menit, detik). Dataset disimpan dalam format CSV dengan nama `Smart_Farming_Sensor_Data.csv`.

### 2. Data Storage (Penyimpanan Data)
Data disimpan secara terstruktur di dalam repositori GitHub dengan folderisasi yang rapi:
* `data/raw/`: Menyimpan dataset mentah.
* `dashboard/`: Menyimpan skrip aplikasi visualisasi.
Penyimpanan ini memastikan integritas data tetap terjaga dan mudah diakses untuk audit.

### 3. Data Processing (Pemrosesan Data)
Proses pembersihan data dilakukan menggunakan Python (Pandas) meliputi:
* **Normalisasi Kolom:** Mengubah semua nama kolom menjadi huruf kecil dan menghapus spasi (strip) untuk mencegah error saat pemanggilan data.
* **Handling Missing Values:** Memastikan tidak ada data sensor yang kosong agar analisis tetap akurat.

### 4. Data Analysis (Analisis Data)
Melakukan agregasi statistik sederhana seperti perhitungan rata-rata kelembaban dari berbagai titik sensor untuk menentukan kondisi kesehatan tanah secara umum.

### 5. Data Visualization (Visualisasi Data)
Implementasi dashboard menggunakan Streamlit dengan 4 komponen utama:
* **Gauge Meter:** Menunjukkan angka rata-rata kelembaban sensor utama secara visual.
* **Alert System:** Memberikan indikator status (Normal, Peringatan, atau Kritis) berdasarkan nilai sensor.
* **Heatmap Correlation:** Menganalisis hubungan antar sensor moisture untuk mendeteksi konsistensi data.
* **Time Series Trend:** Grafik garis yang menunjukkan fluktuasi data seiring berjalannya waktu pengambilan sampel.

### 6. Data Governance (Tata Kelola Data)
Tahap ini memastikan kualitas data tetap tinggi melalui penilaian skor kualitas:
* **Accuracy:** 100% (Data sesuai dengan input asli sensor).
* **Completeness:** 100% (Dataset lengkap tanpa baris kosong).
* **Timeliness:** High (Data tersusun berdasarkan urutan waktu yang valid).
* **Accessibility:** Link dashboard tersedia secara publik untuk transparansi data.

---
