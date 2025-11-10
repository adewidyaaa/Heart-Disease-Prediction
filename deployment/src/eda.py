import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
from PIL import Image
import streamlit as st

def run():
    # Title
    st.title('Aplikasi Prediksi Penyakit Jantung')

    # Subheader
    st.subheader('Berisikan Exploratory Data Analysis (EDA) mengenai Analisis Variabel yang Mempengaruhi Penyakit Jantung')

    # Gambar
    data = Image.open('./src/Heart.jpeg')
    col1, col2, col3 = st.columns([1,2,1])  # kolom kiri, tengah, kanan
    with col2:  # tampilkan di kolom tengah
        st.image(data, caption= 'EDA untuk Aplikasi Prediksi Penyakit Jantung')

    # DataFrame
    df = pd.read_csv('./src/Heart-Disease- dataset.csv')
    st.dataframe(df)

    # EDA 1
    st.write('### Persentase Penyakit Jantung Berdasarkan Aktivitas Olahraga')
    exercise_heart = pd.crosstab(df['Exercise'], df['Heart_Disease'], normalize='index') * 100
    fig = plt.figure(figsize=(12,6))
    sns.barplot(
    data=exercise_heart.reset_index().melt(id_vars='Exercise'),
    x='Exercise', y='value', hue='Heart_Disease')
    st.pyplot(fig)

    # Insight EDA 1
    st.write('##### Insight Exercise vs Heart Disease :')
    st.write('- Orang yang berolahraga cenderung memiliki risiko penyakit jantung lebih rendah')
    st.write('- Persentase orang dengan penyakit jantung lebih kecil di kelompok yang olahraga (<10%) dibandingkan yang tidak olahraga (>10%)')
    st.write('- Sebagian besar responden, tidak memiliki penyakit jantung')

    # EDA 2
    st.write('### Persentase Penyakit Jantung Berdasarkan Riwayat Kanker Kulit')
    skin_heart = pd.crosstab(df['Skin_Cancer'], df['Heart_Disease'], normalize='index') * 100
    skin_heart = skin_heart.reset_index().melt(id_vars='Skin_Cancer')
    fig = plt.figure(figsize=(12,6))
    sns.barplot(data=skin_heart, x='Skin_Cancer', y='value', hue='Heart_Disease')
    st.pyplot(fig)

    # Insight EDA 2
    st.write('##### Insight Skin Cancer vs Heart Disease :')
    st.write('- Persentase penyakit jantung lebih tinggi pada orang yang memiliki riwayat kanker kulit dibanding yang tidak')
    st.write('- Adanya kemungkinan hubungan positif antara riwayat Skin Cancer dan risiko Heart Disease')

    # EDA 3
    st.write('### Persentase Penyakit Jantung Berdasarkan Riwayat Depresi')
    depression = pd.crosstab(df['Depression'], df['Heart_Disease'], normalize='index') * 100
    depression = depression.reset_index().melt(id_vars='Depression')
    fig = plt.figure(figsize=(12,6))
    sns.barplot(data=depression, x='Depression', y='value', hue='Heart_Disease')
    st.pyplot(fig)

    # Insight EDA 3
    st.write('##### Insight Depression vs Heart Disease :')
    st.write('- Persentase penyakit jantung tidak jauh berbeda antara orang yang pernah memiliki riwayat depresi ataupun tidak. Tetapi, orang yang pernah memiliki riwayat depresi, memiliki kemungkinan sedikit lebih tinggi dibandingkan yang tidak')
    st.write('- Adanya kemungkinan bahwa depresi tidak meningkatkan kemungkinan penyakit jantung')

    # EDA 4
    st.write('### Persentase Penyakit Jantung Berdasarkan Status Diabetes')
    diabetes = pd.crosstab(df['Diabetes'], df['Heart_Disease'], normalize='index') * 100
    diabetes = diabetes.reset_index().melt(id_vars='Diabetes')
    fig = plt.figure(figsize=(12,6))
    sns.barplot(data=diabetes, x='Diabetes', y='value', hue='Heart_Disease')
    st.pyplot(fig)

    # Insight EDA 4
    st.write('##### Insight Diabetes vs Heart Disease :')
    st.write('- Kelompok orang dengan riwayat diabetes memiliki kemungkinan penyakit jantung tertinggi (>20%)')
    st.write('- Orang dengan pre-diabetes memiliki kemungkinan penyakit jantung lebih tinggi dibandingkan mereka tanpa riwayat diabetes, meski tidak setinggi orang dengan diabetes penuh')
    st.write('- Ibu hamil dengan diabetes selama kehamilan memiliki kemungkinan penyakit jantung terendah dibandingkan kelompok lain.')
    st.write('- Terdapat korelasi positif antara diabetes dan penyakit jantung: orang dengan riwayat diabetes cenderung memiliki kemungkinan penyakit jantung lebih tinggi.')

     # EDA 5
    st.write('### Persentase Penyakit Jantung Berdasarkan Gender')
    sex_counts = df.groupby('Sex')['Heart_Disease'].value_counts().unstack().fillna(0)
    fig, axes = plt.subplots(1, 2, figsize=(12,6))
    colors = ['#66b3ff','#ff6666']
    labels = ['No', 'Yes']
    for ax, sex in zip(axes, sex_counts.index):
        ax.pie(sex_counts.loc[sex], 
            labels=labels, 
            autopct='%1.1f%%', 
            startangle=90, 
            colors=colors)
        ax.set_title(f'Penyakit Jantung pada Gender = {sex}')
    st.pyplot(fig)

    # Insight EDA 5
    st.write('##### Insight Gender vs Heart Disease :')
    st.write('- Persentase pria yang memiliki penyakit jantung lebih tinggi dibandingkan wanita')
    st.write('- Hal ini menunjukkan adanya korelasi positif antara jenis kelamin laki-laki dan kemungkinan penyakit jantung')

    # EDA 6
    st.write('### Persentase Penyakit Jantung Berdasarkan Usia')
    age_counts = df.groupby('Age_Category')['Heart_Disease'].value_counts().unstack().fillna(0)
    age_counts_yes = age_counts['Yes']
    age_counts_sorted = age_counts_yes.sort_values(ascending=False)
    fig = plt.figure(figsize=(12,8))
    sns.barplot(x=age_counts_sorted.values, y=age_counts_sorted.index, palette="Reds_r")
    st.pyplot(fig)

    # Insight EDA 6
    st.write('##### Insight Age vs Heart Disease :')
    st.write('- Persentase penyakit jantung paling tinggi terdapat pada kelompok dengan usia 80 tahun keatas')
    st.write('- Persentase penyakit jantung paling rendah terdapat pada kelompok dengan rentang usia 18-24 tahun')
    st.write('- Dari data terlihat adanya tren positif antara usia dan kemungkinan penyakit jantung, artinya semakin tua usia seseorang, semakin tinggi kemungkinan untuk memiliki penyakit jantung')

     # EDA 7
    st.write('### Persentase Penyakit Jantung Status Merokok')
    smoke_prop = df.groupby('Smoking_History')['Heart_Disease'].value_counts(normalize=True).unstack().fillna(0)
    smoke_yes = smoke_prop['Yes']
    fig = plt.figure(figsize=(8,8))
    plt.pie(smoke_yes, 
        labels=smoke_yes.index, # type: ignore 
        autopct='%1.1f%%', 
        startangle=90, 
        colors=plt.cm.Reds_r.colors if hasattr(plt.cm.Reds_r, 'colors') else ['#ff9999','#ff6666','#ff3333','#cc0000'],  # type: ignore
        wedgeprops=dict(width=0.4)) 
    st.pyplot(fig)

    # Insight EDA 7
    st.write('##### Insight Smoking History vs Heart Disease :')
    st.write('- Persentase penyakit jantung pada orang yang merokok adalah 67.3%')
    st.write('- Persentase penyakit jantung pada orang yang tidak merokok adalah 32,7%')
    st.write('- Dari data terlihat adanya tren positif antara riwayat merokok dan kemungkinan penyakit jantung, artinya merokok meningkatkan kemungkinan seseorang akan terkena penyakit jantung')


if __name__ == '__main__':
    run()