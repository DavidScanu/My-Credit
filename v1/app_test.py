import unittest
from app import app, make_prediction
from fastapi.testclient import TestClient

class TestAPI(unittest.TestCase):

    client = TestClient(app)

    ex_json_dict = {'age': 34, 'job': 'entrepreneur', 'marital': 'married', 'education': 'tertiary', 'default': 'yes', 'balance': 35266, 'housing': 'yes', 'loan': 'no', 'contact': 'telephone', 'day': 15, 'month': 'aug', 'duration': 80, 'campaign': 2, 'pdays': 1, 'previous': 5}

    ex_json_dict_simple = {'age': 34, 'job': 'entrepreneur', 'marital': 'married', 'education': 'tertiary', 'default': 'yes', 'balance': 35266, 'housing': 'yes', 'loan': 'no', 'contact': 'telephone', 'day': 15, 'month': 'aug', 'duration': 80, 'campaign': 2, 'pdays': 1, 'previous': 5}

    ex_json_dict_double = {
    "age": 34,
    "job": "entrepreneur",
    "marital": "married",
    "education": "tertiary",
    "default": "yes",
    "balance": 35266,
    "housing": "yes",
    "loan": "no",
    "contact": "telephone",
    "day": 15,
    "month": "aug",
    "duration": 80,
    "campaign": 2,
    "pdays": 1,
    "previous": 5
    }

    ex_json_str = """{'age': 34, 'job': 'entrepreneur', 'marital': 'married', 'education': 'tertiary', 'default': 'yes', 'balance': 35266, 'housing': 'yes', 'loan': 'no', 'contact': 'telephone', 'day': 15, 'month': 'aug', 'duration': 80, 'campaign': 2, 'pdays': 1, 'previous': 5}"""

    # Test de la fonction
    def test_make_prediction(self):
        self.assertEqual(dict, type(make_prediction(self.ex_json_dict)))

    def test_response_predict_simple(self):
        response = self.client.post("/predict", json=self.ex_json_dict_simple)
        self.assertEqual(response.status_code, 200)

    def test_response_predict_double(self):
        response = self.client.post("/predict", json=self.ex_json_dict_double)
        self.assertEqual(response.status_code, 200)

    # def test_response_predict_str(self):
    #     response = self.client.post("/predict", json=self.ex_json_str)
    #     self.assertEqual(response.status_code, 200)