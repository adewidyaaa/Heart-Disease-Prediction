# Heart Disease Prediction

## Repository Outline

```
1. description.md - Penjelasan gambaran umum project
2. P1M2_ade_widya.ipynb - Notebook yang berisi pengolahan data dengan python yang berisikan preprocessing, EDA dan model
3. P1M2_ade_widya_inf.ipynb - Notebook untuk inferensi/prediksi menggunakan model yang sudah dilatih
4. P1M2_ade_widya_conceptual.txt - Jawaban terkait pertanyaan conceptual problems
5. best_model.pkl - File model Random Forest terbaik hasil training
6. url.txt - File berisi berbagai link url yang digunakan
7. Heart-Disease-dataset.csv - Dataset BRFSS yang digunakan untuk training dan EDA
8. deployment - Folder berisi script atau file terkait deployment aplikasi prediksi
```

## Problem Background
Penyakit jantung merupakan salah satu penyebab utama kematian global. Banyak kasus baru terdiagnosis ketika sudah parah, sehingga deteksi dini sangat penting. Project ini bertujuan memprediksi kemungkinan seseorang memiliki penyakit jantung menggunakan data BRFSS untuk membantu identifikasi individu berisiko tinggi dan mendukung intervensi dini.

## Project Output
Project ini menghasilkan :
- Visualisasi terkait EDA dengan bar chart dan pie chart
- Model prediksi penyakit jantung berbasis Random Forest.
- Evaluasi performa model (recall dan confusion matrix).
- Insight faktor risiko utama seperti diabetes, usia lanjut, merokok, jenis kelamin.
- Deployment interaktif melalui Hugging Face Spaces.


## Data
- Sumber: BRFSS (Behavioral Risk Factor Surveillance System)
- Fitur: Faktor gaya hidup dan kondisi kesehatan pasien
- Target: Kemungkinan penyakit jantung (Yes/No)
- Deskripsi : 19 kolom dan 308.854 baris
- Karakteristik: Tidak ada missing value, preprocessing sudah dilakukan

## Method
- Exploratory Data Analysis (EDA): Menilai hubungan faktor risiko dengan penyakit jantung
- Modelling: Random Forest dengan hyperparameter tuning
- Evaluasi: Recall sebagai metrik utama untuk mengurangi risiko melewatkan pasien berisiko tinggi
- Deployment: Hugging Face Spaces untuk prediksi interaktif

## Stacks
- Bahasa Pemrograman: Python
- Library: pandas, numpy, matplotlib, seaborn, plotly, pillow, scikit-learn, imbalanced-learn, feature-engine, phik, xgboost, streamlit, pickle
- Tools: VS Code, GitHub, Hugging Face Spaces

## Reference
Deployment : Hugging Face Space (https://huggingface.co/spaces/adewidya/heart-disease-prediction)

---
