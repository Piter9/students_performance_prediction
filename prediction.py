import joblib
 
model = joblib.load("model/rdf_model.joblib")
result_target = joblib.load("model/encoder_target.joblib")

def prediction(data):
    """Making prediction
 
    Args:
        data (Pandas DataFrame): Dataframe that contain all the preprocessed data
 
    Returns:
        str: Prediction result (Good, Standard, or Poor)
    """
    result = model.predict(data)
    # try:
    #     final_result = result_target.inverse_transform(result)[0]
    # except ValueError as e:
    #     final_result = f"Unknown ({result[0]})"
    return result[0]
    # final_result = result_target.inverse_transform(result)[0]
    # return final_result