import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import pearsonr
from sklearn.cluster import KMeans

# Load data
def load_data(source):
    if source == 'Google Drive':
        data = pd.read_csv('/content/drive/MyDrive/analisis python dicoding bangkit/Air-quality-dataset/PRSA_Data_20130301-20170228/PRSA_Data_Aotizhongxin_20130301-20170228.csv')
    else:
        data = pd.read_csv('/content/PRSA_Data_Aotizhongxin_20130301-20170228.csv')
    return data.dropna()

# Sidebar
st.sidebar.header('Pilihan')
source = st.sidebar.selectbox('Pilih sumber data', ['Google Drive', 'Local Path'])
data = load_data(source)

# Main 
st.header('Analisis Data Udara')
if st.sidebar.checkbox('Tampilkan data mentah'):
    st.subheader('Data mentah')
    st.write(data)

if st.sidebar.checkbox('Tampilkan deskripsi data'):
    st.subheader('Deskripsi data')
    st.write(data.describe())

if st.sidebar.checkbox('Tampilkan korelasi suhu dan PM2.5'):
    st.subheader('Korelasi antara Suhu dan PM2.5')
    plt.figure(figsize=(10, 6))
    plt.scatter(data['TEMP'], data['PM2.5'])
    plt.title('Korelasi antara Suhu dan PM2.5')
    plt.xlabel('Suhu')
    plt.ylabel('PM2.5')
    st.pyplot(plt.gcf())
    corr, _ = pearsonr(data['TEMP'], data['PM2.5'])
    st.write('Koefisien Korelasi Pearson antara Suhu dan PM2.5: %.3f' % corr)

# New: Column selector for analysis
column_to_analyze = st.sidebar.selectbox('Pilih kolom untuk analisis', data.columns)
st.write(f'Anda memilih {column_to_analyze}')

# New: Interactive histogram
st.subheader(f'Histogram {column_to_analyze}')
bins = st.sidebar.slider('Jumlah bins', 5, 50, 25)
plt.hist(data[column_to_analyze], bins=bins)
plt.title(f'Histogram {column_to_analyze}')
plt.xlabel(column_to_analyze)
plt.ylabel('Frekuensi')
st.pyplot(plt.gcf())

# New: Boxplot for selected column
st.subheader(f'Boxplot {column_to_analyze}')
sns.boxplot(x=data[column_to_analyze])
st.pyplot(plt.gcf())
