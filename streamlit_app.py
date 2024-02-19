import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import pearsonr
from sklearn.cluster import KMeans

# Fungsi untuk membaca data
def load_data():
    data = pd.read_csv('/content/drive/MyDrive/analisis python dicoding bangkit/Air-quality-dataset/PRSA_Data_20130301-20170228/PRSA_Data_Aotizhongxin_20130301-20170228.csv')
    return data

# Fungsi untuk membersihkan data
def clean_data(data):
    data = data.dropna()
    return data

# Fungsi untuk melakukan analisis data
def run_analysis(data):
    # Korelasi antara Suhu dan PM2.5
    corr, _ = pearsonr(data['TEMP'], data['PM2.5'])
    st.write('Koefisien Korelasi Pearson antara Suhu dan PM2.5: %.3f' % corr)

    # Tren Kualitas Udara (PM2.5) Sepanjang Waktu
    data['date'] = pd.to_datetime(data[['year', 'month', 'day', 'hour']])
    data.set_index('date', inplace=True)
    st.line_chart(data['PM2.5'].resample('M').mean())

    # Clustering Berdasarkan Suhu dan PM2.5
    kmeans = KMeans(n_clusters=3, random_state=0).fit(data[['TEMP', 'PM2.5']])
    data['cluster'] = kmeans.labels_
    st.write(data)

# Fungsi utama aplikasi Streamlit
def main():
    st.title('Proyek Analisis Data')

    data = load_data()
    data = clean_data(data)

    if st.button('Jalankan Analisis'):
        run_analysis(data)

if __name__ == "__main__":
    main()
