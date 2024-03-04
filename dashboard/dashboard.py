import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency
sns.set(style='dark')
st.set_option('deprecation.showPyplotGlobalUse', False)

bike_sharing_df = pd.read_csv("main_data.csv")
bike_sharing_df['dteday'] = pd.to_datetime(bike_sharing_df['dteday'])
bike_sharing_df['year'] = bike_sharing_df['dteday'].dt.year

# Menghitung total peminjaman sepeda sepanjang tahun 2011 dan 2012
total_rentals_2011 = bike_sharing_df[bike_sharing_df['year'] == 2011]['cnt'].sum()
total_rentals_2012 = bike_sharing_df[bike_sharing_df['year'] == 2012]['cnt'].sum()

# Menghitung jumlah peningkatan
peningkatan = total_rentals_2012 - total_rentals_2011

# Menghitung persentase peningkatan
persentase_peningkatan = (peningkatan / total_rentals_2011) * 100

st.header('Visualisasi Tren Peminjaman Sepeda Tahun 2011 ke 2012 :sparkles:')

# Visualisasi tren peminjaman sepeda dari tahun 2011 ke 2012
plt.figure(figsize=(10, 5))
plt.plot([2011, 2012], [total_rentals_2011, total_rentals_2012], marker='o')
plt.title('Tren Peminjaman Sepeda (2011-2012)')
plt.xlabel('Tahun')
plt.ylabel('Jumlah Peminjaman Sepeda')
plt.grid(True)
st.pyplot()
st.write("Total Peminjaman Sepeda Tahun 2011:", total_rentals_2011)
st.write("Total Peminjaman Sepeda Tahun 2012:", total_rentals_2012)
st.write("Jumlah Peningkatan Peminjaman Sepeda:", peningkatan)
st.write("Persentase Peningkatan Peminjaman Sepeda:", persentase_peningkatan, "%")

# Korelasi antara Suhu Lingkungan dan Jumlah Peminjaman Sepeda
correlation = bike_sharing_df['temp'].corr(bike_sharing_df['cnt'])


st.header('Korelasi Suhu Lingkungan Dengan Jumlah Peminjaman Sepeda :sparkles:')

# Visualisasi korelasi menggunakan seaborn
sns.regplot(x=bike_sharing_df["temp"], y=bike_sharing_df["cnt"])
plt.title('Korelasi antara Suhu Lingkungan dan Jumlah Peminjaman Sepeda')
plt.xlabel('Suhu Lingkungan (Normalized)')
plt.ylabel('Jumlah Peminjaman Sepeda')
plt.grid(True)
st.pyplot()

st.write("Korelasi antara Suhu Lingkungan dan Jumlah Peminjaman Sepeda:", correlation)