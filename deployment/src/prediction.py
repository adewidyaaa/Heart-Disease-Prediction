import pandas as pd
import numpy as np
import pickle
import streamlit as st
from PIL import Image

# Load best model yag telah disave
with open('./src/best_model.pkl','rb') as model_file:
  loaded_model = pickle.load(model_file)



def run():

    # Title
    st.write('### HEART DISEASE PREDICTION')

    # Gambar
    
    data = Image.open('./src/predict.jpeg')
    col1, col2, col3 = st.columns([1,2,1])  # kolom kiri, tengah, kanan
    with col2:  # tampilkan di kolom tengah
        st.image(data)

    # Pembuatan Form
    with st.form(key='heart-disease-predict'):
        gh = st.selectbox('General Health',('Poor', 'Fair', 'Good', 'Very Good', 'Excellent'), help= 'Kondisi kesehatan saat ini')
        cu = st.selectbox('Checkup',('Never','5 or more years ago','Within the past 5 years', 'Within the past 2 years', 'Within the past year'), help='Riwayat Pemeriksaan Kesehatan')
        ex = st.selectbox('Exercise', ('Yes','No'))
        st.markdown('---')

        sc = st.selectbox('Skin Cancer', ('Yes','No'))
        oc = st.selectbox('Other Cancer', ('Yes','No'))
        dep = st.selectbox('Depression', ('Yes','No'))
        db = st.selectbox('Diabetes', ('Yes','Yes, but female told only during pregnancy','No', 'No, pre-diabetes or borderline diabetes',))
        ar = st.selectbox('Arthritis', ('Yes','No'))
        st.markdown('---')
        
        sex = st.selectbox('Sex', ('Male','Female'))
        hc = st.number_input('Height (cm)',min_value=90, max_value=220)
        wk = st.number_input('Weight (kg)',min_value=30.0, max_value=120.0,format="%.1f",step=0.1)
        bmi = st.number_input('BMI',min_value=10.0, max_value=80.0,format="%.1f",step=0.1, help='Nilai BMI (Body Mass Index)')
        ag = st.selectbox('Age Category', ('18-39','40-59','60-79','80+'), help='Kategori Usia')
        st.markdown('---')

        sh = st.selectbox('Smoking History', ('Yes','No'))
        ac = st.number_input('Alcohol Consumption',min_value=0, max_value=50)
        fc = st.number_input('Fruit Consumption',min_value=0, max_value=50)
        gvc = st.number_input('Green Vegetables Consumption',min_value=0, max_value=50)
        fpc = st.number_input('Fried Potato Consumption',min_value=0, max_value=50)
        
        submitted = st.form_submit_button('Predict')


    data_inf = {
    'General_Health': gh,
    'Checkup': cu,
    'Exercise': ex,
    'Skin_Cancer': sc,
    'Other_Cancer': oc,
    'Depression': dep,
    'Diabetes': db,
    'Arthritis': ar,
    'Sex': sex,
    'Height_(cm)' : hc,
    'Weight_(kg)' : wk,
    'BMI': bmi,
    'Age_Group': ag,
    'Smoking_History': sh,
    'Alcohol_Consumption': ac,
    'Fruit_Consumption' : fc,
    'Green_Vegetables_Consumption' : gvc,
    'FriedPotato_Consumption' : fpc
    }


    if submitted:
        data_inf = pd.DataFrame([data_inf])
        st.dataframe(data_inf)

        # Hasil prediksi
        y_pred = loaded_model.predict(data_inf)
        pred_label = 'Yes' if y_pred == 1 else 'No'
        st.write('# Heart Disease Prediction :', pred_label)



if __name__ == '__main__':
    run()