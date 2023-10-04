from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel

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

# Import model 

# Import Label Encoder (pour encoder les variables)

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

@app.post("/bank_loan", tags=['POST'])
def bank_loan(params:PredictParams):

  if params == None:
    return "Please enter parameters."
  
  # Parameters encoding
  
  # Prediction

  # Results

  return params

  # Sortie : 
  # la réponse du modèle
  # le score de précision
  # (Bonus : Les variables ayant le plus contribué à la réponse du modèle dans un dictionnaire).



if __name__ == '__main__':
  uvicorn.run(app, host='0.0.0.0', port=8000)