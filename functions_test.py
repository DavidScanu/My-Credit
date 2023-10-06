import unittest
import json
import pandas as pd

from functions import import_data_function, preprocess_data, labelize_standardize_data_function, train_model_function

class TestFunctions(unittest.TestCase):

    def setUp(self):
        # Chargement des données de test depuis les fichiers CSV ('train' & 'test)
        self.train_data = pd.read_csv('train.csv', delimiter=';')
        self.test_data = pd.read_csv('test.csv',  delimiter=';')
        # Chargement du fichier JSON contenant les valeurs d'encodage
        with open('encode_dict.json', 'r') as json_file:
            self.label_encoder_mapping = json.load(json_file)

    def test_import_data(self):
        # Appel de la fonction d'importation des données
        train_data, test_data = import_data_function('train.csv', 'test.csv')
        # Vérifiez que les données d'entraînement et de test ont été importées avec succès
        self.assertIsNotNone(train_data)
        self.assertIsNotNone(test_data)

    def test_preprocess_train_data(self):
        # Appel de la fonction de prétraitement des données d'entraînement
        preprocessed_train_data = preprocess_data(self.train_data)
        # Vérifiez que la colonne 'poutcome' a été supprimée
        self.assertNotIn('poutcome', preprocessed_train_data.columns)
        # Vérifiez que la colonne 'pdays' a été modifiée correctement
        self.assertTrue(all(preprocessed_train_data['pdays'].isin([0, 1])))

    def test_preprocess_test_data(self):
        # Appel de la fonction de prétraitement des données de test
        preprocessed_test_data = preprocess_data(self.test_data)
        # Vérifiez que la colonne 'poutcome' a été supprimée
        self.assertNotIn('poutcome', preprocessed_test_data.columns)
        # Vérifiez que la colonne 'pdays' a été modifiée correctement
        self.assertTrue(all(preprocessed_test_data['pdays'].isin([0, 1])))

    def test_labelize_standardize_data(self):
        # Appel de la fonction de standardisation des données avec les données d'entraînement et de test
        labelize_standardized_train_data, labelize_standardized_test_data = labelize_standardize_data_function(self.train_data, self.test_data)
    
        # Vérifiez que les données d'entraînement et de test ont été standardisées avec succès
        self.assertIsNotNone(labelize_standardized_train_data)
        self.assertIsNotNone(labelize_standardized_test_data)
    
    
    def test_train_model(self):
        # Appel de la fonction de standardisation des données avec les données d'entraînement et de test
        train_data, test_data = import_data_function('train.csv', 'test.csv')
        labelize_standardized_train_data, labelize_standardized_test_data = labelize_standardize_data_function(train_data, test_data)
        # Appel de la fonction d'entraînement du modèle
        model_XGBC = train_model_function(labelize_standardized_train_data)
        # Vérifiez que le modèle a été correctement entraîné
        self.assertIsNotNone(model_XGBC)

if __name__ == '__main__':
    unittest.main()
