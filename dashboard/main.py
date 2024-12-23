import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

day_df = pd.read_csv("new_day_df.csv")

with st.sidebar:
    # Pict
    st.image("cat.jpg")
    
    # Text
    st.text("Submisi Data Analisis")
    st.text("Dicoding Username: relrel111")
    

st.header('Bike Sharing Analysis')

st.subheader('Bagaimana faktor cuaca memengaruhi jumlah peminjaman sepeda?')
fig = plt.figure(figsize=(10,6))
colors_ = ["#D3D3D3", "#72BCD4", "#D3D3D3", "#D3D3D3", "#D3D3D3"]
sns.barplot(
    x='weathersit',
    y='cnt',
    data=day_df,
    palette=colors_)

plt.title('Pengaruh Cuaca Terhadap Jumlah Peminjaman Sepeda')
plt.xlabel('Kondisi Cuaca')
plt.ylabel('Jumlah Pengguna Sepeda')
st.pyplot(fig)

st.subheader('Waktu Paling Populer untuk Peminjaman Sepeda.')
fig = plt.figure(figsize=(10,6))
colors_ = ["#D3D3D3", "#72BCD4", "#D3D3D3", "#D3D3D3", "#D3D3D3"]
sns.barplot(
    x='workingday',
    y='cnt',
    data=day_df,
    palette=colors_)

plt.title('Waktu Paling Populer Untuk Peminjaman Sepeda')
plt.xlabel(None)
plt.ylabel('Jumlah Pengguna Sepeda')
st.pyplot(fig)