import streamlit as st
import pandas as pd
import numpy as np

from data_preprocessing import (
    data_preprocessing,
    encoder_Course,
    encoder_Gender,
    encoder_Marital_status,
    encoder_Daytime_evening_attendance,
    encoder_Debtor,
    encoder_Displaced,
    encoder_Educational_special_needs,
    encoder_International,
    encoder_Scholarship_holder,
    encoder_Tuition_fees_up_to_date,
)

from prediction import prediction

# Mapping untuk biner (0 = Tidak, 1 = Iya)
binary_options = {"Tidak": 0, "Iya": 1}
gender_options = {"Laki-laki": 0, "Perempuan": 1}

# Konfigurasi Streamlit
st.set_page_config(page_title="🎓 Student Status Prediction", layout="centered")
st.title("🎓 Student Status Prediction Dashboard")
st.markdown("Masukkan data mahasiswa untuk memprediksi statusnya: **Enrolled**, **Graduate**, atau **Dropout**.")

# Form input
with st.form("prediction_form"):
    st.subheader("📋 Formulir Data Mahasiswa")

    col1, col2 = st.columns(2)

    with col1:
        gender_label = st.selectbox("Gender", list(gender_options.keys()))
        marital_status = st.selectbox("Marital Status", encoder_Marital_status.classes_)
        course = st.selectbox("Course", encoder_Course.classes_)
        attendance = st.selectbox("DayTime Attendance Time?", list(binary_options.keys()))
        debtor_label = st.selectbox("Debtor", list(binary_options.keys()))
        displaced_label = st.selectbox("Displaced", list(binary_options.keys()))

    with col2:
        special_needs_label = st.selectbox("Educational Special Needs", list(binary_options.keys()))
        international_label = st.selectbox("International Student", list(binary_options.keys()))
        scholarship_label = st.selectbox("Scholarship Holder", list(binary_options.keys()))
        tuition_paid_label = st.selectbox("Tuition Fees Up To Date", list(binary_options.keys()))
        admission_grade = st.number_input("Admission Grade", min_value=0.0, max_value=200.0, step=0.1)
        previous_grade = st.number_input("Previous Qualification Grade", min_value=0.0, max_value=200.0, step=0.1)
        age = st.number_input("Age at Enrollment", min_value=15, max_value=60)

    submitted = st.form_submit_button("🔍 Prediksi")

# Eksekusi prediksi jika tombol diklik
if submitted:
    try:
        input_dict = {
            "Gender": [gender_options[gender_label]],
            "Marital_status": [marital_status],
            "Course": [course],
            "Daytime_evening_attendance": [binary_options[attendance]],
            "Debtor": [binary_options[debtor_label]],
            "Displaced": [binary_options[displaced_label]],
            "Educational_special_needs": [binary_options[special_needs_label]],
            "International": [binary_options[international_label]],
            "Scholarship_holder": [binary_options[scholarship_label]],
            "Tuition_fees_up_to_date": [binary_options[tuition_paid_label]],
            "Admission_grade": [admission_grade],
            "Previous_qualification_grade": [previous_grade],
            "Age_at_enrollment": [age]
        }

        input_df = pd.DataFrame(input_dict)
        preprocessed = data_preprocessing(input_df)
        pred_result = prediction(preprocessed)

        # Tampilkan hasil
        st.success(f"Hasil Prediksi: **{pred_result}**")
    #     if pred_result == "Good":
    #         st.markdown("✅ Mahasiswa diprediksi **berhasil dengan baik**.")
    #     elif pred_result == "Standard":
    #         st.markdown("⚠️ Mahasiswa diprediksi **berhasil secara standar**.")
    #     else:
    #         st.markdown("❌ Mahasiswa diprediksi **berpotensi gagal**.")

    except Exception as e:
        st.error(f"Terjadi kesalahan saat memproses: {e}")
