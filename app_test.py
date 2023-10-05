import unittest
from app import app
from fastapi.testclient import TestClient

class TestAPI(unittest.TestCase):

    client = TestClient(app)

    data = {'n' : 5}

    def test_repsonse(self):
        response = self.client.post("/bank_loan", json=data)
        self.assertEqual(response.status_code, 200)
    
