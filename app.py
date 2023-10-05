from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel
import json
import os
import pickle

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


def import_pickle_object(pickle_file_path):
  if os.path.exists(pickle_file_path):
    # Open the pickle file in binary read mode.
    with open(pickel_file_path, "rb") as f:
        # Load the pickled object from the file.
        pickled_object = pickle.load(f)
    # Close the file.
    f.close()
  else:
    print("The file does not exist.")
  return pickled_object

pickel_file_path = "model_data.pkl"
pickled_object = import_pickle_object(pickel_file_path)

# Dans le bon ordre
cols = pickled_object['columns']
scaler = pickled_object['scaler']
model = pickled_object['model']
feature_importance = pickled_object['feature_importance']

# Import encoding dictionnary
def import_json_file(file_path):
  if os.path.exists(file_path):
    with open(file_path, "r") as f:
        data_json = json.load(f)
  else:
    print("The file does not exist.")
  return data_json

encode_dict = import_json_file("encode_dict.json")

# Variables
# Pydantic is the most widely used data validation library for Python.
class PredictParams(BaseModel):
  age : int
  matrimonial : str
  education : str
  work : str
  salary : int
  credit_failure : bool
  housing_credit : bool
  personal_credit : bool
  contact : bool
  contact_type : str
  nbr_contact_actual : int
  nbr_contact_past : int
  day : int
  month : str
  second : int


# testing model prediction
pred = model.predict(scaler.fit_transform([range(15)]))


def make_prediction(params_json_str):

  # Parse JSON
  params_json_dict = eval(params_json_str)
  # Encoder
  # encode_dict
  # params_encoded = 
  # Scaler
  # data_scaled = scaler.fit_transform([range(15)])
  # Prediction

  # Dictionnary
  results = {
    "prediction" : 0,
    "score" : 0.86,
    "feature_importance" : [1, 2 ,3]
  }
  return results

ex_json_str = "{'age': 25, 'job': None, 'marital': 'Célibataire', 'education': 'Inconnu', 'default': False, 'balance': 30000, 'housing': False, 'loan': False, 'contact': 'inconnu', 'day': None, 'month': None, 'duration': 0, 'campaign': 0, 'pdays': False, 'previous': 0}"

pred = make_prediction(ex_json_str)
print(pred)

# API
@app.post("/bank_loan", tags=['POST'])
def bank_loan(params:PredictParams):

  if params == None:
    return "Please enter parameters."
  
  # Parameters encoding
  
  # Prediction

  # Sortie : 
  # la réponse du modèle
  # le score de précision
  # (Bonus : Les variables ayant le plus contribué à la réponse du modèle dans un dictionnaire).

if __name__ == '__main__':
  uvicorn.run(app, host='0.0.0.0', port=8000)