import joblib
import numpy as np
import pandas as pd

encoder_Course = joblib.load("model/encoder_Course.joblib")
encoder_Daytime_evening_attendance = joblib.load("model/encoder_Daytime_evening_attendance.joblib")
encoder_Debtor = joblib.load("model/encoder_Debtor.joblib")
encoder_Displaced = joblib.load("model/encoder_Displaced.joblib")
encoder_Educational_special_needs = joblib.load("model/encoder_Educational_special_needs.joblib")
encoder_Gender = joblib.load("model/encoder_Gender.joblib")
encoder_International = joblib.load("model/encoder_International.joblib")
encoder_Marital_status = joblib.load("model/encoder_Marital_status.joblib")
encoder_Scholarship_holder = joblib.load("model/encoder_Scholarship_holder.joblib")
encoder_target = joblib.load("model/encoder_target.joblib")
encoder_Tuition_fees_up_to_date = joblib.load("model/encoder_Tuition_fees_up_to_date.joblib")

scaler_Admission_grade = joblib.load("model/scaler_Admission_grade.joblib")
scaler_Age_at_enrollment = joblib.load("model/scaler_Age_at_enrollment.joblib")
scaler_Previous_qualification_grade = joblib.load("model/scaler_Previous_qualification_grade.joblib")


def data_preprocessing(data):
    """Preprocessing data
 
    Args:
        data (Pandas DataFrame): Dataframe that contain all the data to make prediction 
        
    return:
        Pandas DataFrame: Dataframe that contain all the preprocessed data
    """
    data = data.copy()
    df = pd.DataFrame() 
    
    df["Course"] = encoder_Course.transform(data["Course"])[0]
    df["Daytime_evening_attendance"] = encoder_Daytime_evening_attendance.transform(data["Daytime_evening_attendance"])[0]
    df["Debtor"] = encoder_Debtor.transform(data["Debtor"])[0]
    df["Displaced"] = encoder_Displaced.transform(data["Displaced"])[0]
    df["Educational_special_needs"] = encoder_Educational_special_needs.transform(data["Educational_special_needs"])[0]
    df["Gender"] = encoder_Gender.transform(data["Gender"])[0]
    df["International"] = encoder_International.transform(data["International"])[0]
    df["Marital_status"] = encoder_Marital_status.transform(data["Marital_status"])[0]
    df["Scholarship_holder"] = encoder_Scholarship_holder.transform(data["Scholarship_holder"])[0]
    df["Tuition_fees_up_to_date"] = encoder_Tuition_fees_up_to_date.transform(data["Tuition_fees_up_to_date"])[0]

    df["Admission_grade"] = scaler_Admission_grade.transform(np.asarray(data["Admission_grade"]).reshape(-1,1))[0]
    df["Age_at_enrollment"] = scaler_Age_at_enrollment.transform(np.asarray(data["Age_at_enrollment"]).reshape(-1,1))[0]
    df["Previous_qualification_grade"] = scaler_Previous_qualification_grade.transform(
    np.asarray(data["Previous_qualification_grade"]).reshape(-1,1))[0]
    
    ordered_columns = [
    "Marital_status",
    "Course",
    "Daytime_evening_attendance",
    "Previous_qualification_grade",
    "Admission_grade",
    "Displaced",
    "Educational_special_needs",
    "Debtor",
    "Tuition_fees_up_to_date",
    "Gender",
    "Scholarship_holder",
    "Age_at_enrollment",
    "International",
    ]

    df = df[ordered_columns]
    return df