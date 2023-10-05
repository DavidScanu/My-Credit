from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel
import json
import os
import pickle
import pandas as pd
import numpy as np

tags_metadata = [
  {
    'name' : 'POST',
    'description' : "Lorem Ipsum Main"
  }
]

app = FastAPI(
  title = "💳 API pour l'application My Credit",
  description = "Lorem Ipsum Post",
  openapi_tags=tags_metadata
)

# Import Pickle Dictionnary
def import_pickle_object(pickle_file_path):
  if os.path.exists(pickle_file_path):
    # Open the pickle file in binary read mode.
    with open(pickel_file_path, "rb") as f:
        # Load the pickled object from the file.
        pickled_object = pickle.load(f)
    # Close the file.
    f.close()
    return pickled_object
  else:
    print("The file does not exist.")

pickel_file_path = "model_data.pkl"
pickled_object = import_pickle_object(pickel_file_path)

# Pickle Variables
cols = pickled_object['columns']
scaler = pickled_object['scaler']
model = pickled_object['model']
# feature_importance = pickled_object['feature_importance']


# Import encoding dictionnary
def import_json_file(file_path):
  if os.path.exists(file_path):
    with open(file_path, "r") as f:
        data_json = json.load(f)
  else:
    print("The file does not exist.")
  return data_json

encode_dict = import_json_file("encode_dict.json")



# Probleme si une valeurs est None ou du mauvais type.
def encode_features(params_json_dict):
  """
  Fonction qui encode les variables catégorielles.
  """
  for key, value in params_json_dict.items():
    # print(key, value)
    if key in encode_dict:
      if value != None:
        value_encoded = encode_dict[key][value]
        params_json_dict[key] = value_encoded
  return params_json_dict

# testing model prediction
# pred = model.predict(scaler.fit_transform([range(15)]))
# pred_proba = model.predict_proba([range(15)])
# print(pred_proba)

# Prediction
def make_prediction(params_json):
  """
  Fonction qui réalise une prédiction à partir du JSON.
  """
  # Parse JSON
  # params_dict = eval(params_json) # dict
  # Encoder
  params_enc = encode_features(params_json) # dict
  # Convert into DataFrame
  params_enc_df = pd.DataFrame(params_enc, index=[0]) # df
  # Scaler
  params_scaled = scaler.transform(params_enc_df) # ndarray
  # Prediction
  pred_proba = model.predict_proba(params_scaled)
  y_pred = np.argmax(pred_proba)
  pred_score = pred_proba.max()
  # Results
  results = {
    "prediction" : y_pred,
    "score" : pred_score
    # "feature_importance" : [1, 2 ,3]
  }
  return results


# Variables
# Pydantic is the most widely used data validation library for Python.
class PredictParams(BaseModel):
  age : int
  job : str
  marital : str
  education : str
  default : str
  balance : int
  housing : str
  loan : str
  contact : str
  day : int
  month : str
  duration : int
  campaign : int
  pdays : int
  previous : int

# API
@app.post("/predict", tags=['POST'])
def predict(params:PredictParams):

  # if params == None:
  #   return "Please enter parameters."
  
  return make_prediction(params)


if __name__ == '__main__':
  uvicorn.run(app, host='0.0.0.0', port=8000)