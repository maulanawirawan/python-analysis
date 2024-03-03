# Proyek Analisis Data: Air Quality Dataset

## Deskripsi Proyek
Proyek ini bertujuan untuk menganalisis dataset kualitas udara dan mengeksplorasi hubungan antara suhu dan partikel PM2.5. Selain itu, proyek ini juga mencakup visualisasi tren kualitas udara sepanjang waktu dan pengelompokan data berdasarkan suhu dan PM2.5 menggunakan algoritma KMeans.

## Penulis
- **Nama:** Maulana Wirawan
- **Email:** awan.maraikoh@gmail.com
- **ID Dicoding:** Maulana Wirawan

## Packages/Library yang Digunakan
- pandas
- numpy
- matplotlib
- seaborn
- google.colab
- scipy.stats
- sklearn.cluster
- streamlit

## Metodologi
Proyek ini melibatkan beberapa tahapan, yaitu:
1. **Data Wrangling:** Proses ini melibatkan pengumpulan data, penilaian data awal, dan pembersihan data.
2. **Exploratory Data Analysis (EDA):** Pada tahap ini, dilakukan perhitungan koefisien korelasi Pearson antara suhu dan PM2.5 dan visualisasi tren kualitas udara sepanjang waktu.
3. **Clustering:** Menggunakan algoritma KMeans untuk mengelompokkan data berdasarkan suhu dan PM2.5.
4. **Streamlit Dashboard:** Membuat dashboard interaktif menggunakan Streamlit untuk memvisualisasikan hasil analisis.

## Hasil
Hasil dari proyek ini mencakup koefisien korelasi Pearson antara suhu dan PM2.5, visualisasi tren kualitas udara sepanjang waktu, visualisasi hasil clustering berdasarkan suhu dan PM2.5, dan dashboard interaktif.

## Catatan
Proyek ini masih dalam tahap pengembangan dan akan terus diperbarui dengan analisis dan visualisasi tambahan.

## Cara Menjalankan Dashboard
Untuk menjalankan dashboard, Anda perlu menginstal Streamlit dan menjalankan file `dashboard.py` menggunakan Streamlit. Anda juga perlu mengatur tunneling menggunakan localtunnel. Berikut adalah langkah-langkahnya:

1. Install Streamlit:
    ```
    !pip install streamlit -q
    ```

2. Jalankan file `dashboard.py`:
    ```
    !streamlit run dashboard.py & npx localtunnel --port 8501
    ```

3. Anda akan mendapatkan URL dari localtunnel yang dapat Anda gunakan untuk mengakses dashboard Anda.
