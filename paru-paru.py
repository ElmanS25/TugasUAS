import pickle
import numpy as np
import streamlit as st

model = pickle.load(open('paru-paru.sav','rb'))

st.title('Prediksi Terkena Penyakit Paru-Paru')
col1, col2 = st.columns(2)

with col1:
   Usia	= st.number_input('Umur Pasien')
   Jenis_Kelamin = st.number_input('Jenis Kelamin Pasien')
   Merokok = st.number_input('Pasien yang Merokok')
   Bekerja = st.number_input('Pasien yang Bekerja')
   Rumah_Tangga	= st.number_input('Pasien yang sudah Menikah')
   
with col2:
   Aktivitas_Begadang = st.number_input('Pasien yang melakukan aktivitas Begadang')
   Aktivitas_Olahraga = st.number_input('Pasien yang melakukan aktivitas Olahraga')
   Asuransi = st.number_input('Pasien yang memiliki asuransi')
   Penyakit_Bawaan = st.number_input('Pasien yang memiliki penyakit bawaan')

predik = ''
if st.button('Hasil Prediksi'):
    predik = model.predict([[Usia, Aktivitas_Begadang, Jenis_Kelamin, Aktivitas_Olahraga, Merokok, Asuransi, Bekerja, Penyakit_Bawaan, Rumah_Tangga]])

    if(predik[0] == 1):
        predik = 'Kemungkinan Pasien yang terkena Penyakit Paru-Paru'
    else:
        predik = 'Kemungkinan Pasien yang tidak terkena Penyakit Paru-Paru'
st.success(predik)