# import des packages
import pandas as pd
import json
import xgboost as xgb

from sklearn.preprocessing import StandardScaler, LabelEncoder


def import_data_function(train_csv_path='train.csv', test_csv_path='test.csv'):
    """
    Importe les données à partir de fichiers CSV distincts pour l'entraînement et le test.
    Args:
    -----
        train_csv_path (str): Chemin vers le fichier CSV d'entraînement.
        test_csv_path (str): Chemin vers le fichier CSV de test.
    Returns:
    -----
        pd.DataFrame: Un DataFrame pandas contenant les données d'entraînement.
        pd.DataFrame: Un DataFrame pandas contenant les données de test.
    """
    # Importer les données d'entraînement depuis le fichier CSV
    train_data = pd.read_csv(train_csv_path, delimiter=';')

    # Importer les données de test depuis le fichier CSV
    test_data = pd.read_csv(test_csv_path, delimiter=';')

    return train_data, test_data


def preprocess_data(data):
    """
    Supprime la colonne 'poutcome' du DataFrame et modifie la colonne 'pdays' en remplaçant -1 par 0 et le reste par 1.
    Args:
    -----
        data (pd.DataFrame): Le DataFrame pandas à prétraiter.
    Returns:
    -----
        pd.DataFrame: Le DataFrame prétraité.
    """
    # Supprimer la colonne 'poutcome'
    if 'poutcome' in data.columns:
        data.drop('poutcome', axis=1, inplace=True)

    # Modifier la colonne 'pdays' en remplaçant -1 par 0 et le reste par 1
    data['pdays'] = data['pdays'].apply(lambda x: 0 if x == -1 else 1)

    return data


def labelize_standardize_data_function(train_data, test_data):
    """
    Standardise les données après l'encodage avec LabelEncoder en utilisant les valeurs du fichier JSON.
    Args:
    -----
        train_data (pd.DataFrame): Un DataFrame pandas contenant les données d'entraînement.
        test_data (pd.DataFrame): Un DataFrame pandas contenant les données de test.
        label_encoder_mapping_file (str): Chemin vers le fichier JSON contenant les valeurs d'encodage.
    Returns:
    -----
        pd.DataFrame: Un DataFrame pandas contenant les données d'entraînement labelisées & standardisées.
        pd.DataFrame: Un DataFrame pandas contenant les données de test labelisées & standardisées.
    """
    # Charger le fichier JSON avec les valeurs d'encodage
    with open('encode_dict.json', 'r') as json_file:
        label_encoder_mapping = json.load(json_file)

    # Créer un objet StandardScaler pour la standardisation
    scaler = StandardScaler()

    # Liste des noms de colonnes à labeliser('columns_to_labelize', récupérées directement via le fichier json) & à standardiser ('columns_to_standardize')
    columns_to_labelize = list(label_encoder_mapping.keys())
    columns_to_standardize = train_data.columns.tolist()[:-1]

    # Créer des copies des DataFrames pour les données d'entraînement et de test
    train_lb_st_data = train_data.copy()
    test_lb_st_data = test_data.copy()

    # Appliquer le LabelEncoder via le fichier JSON pour le 'train_data'
    for col in columns_to_labelize:
        train_lb_st_data[col] = train_lb_st_data[col].map(label_encoder_mapping[col])


    # Appliquer le LabelEncoder via le fichier JSON pour le 'test_data'
    for col in columns_to_labelize:
        test_lb_st_data[col] = test_lb_st_data[col].map(label_encoder_mapping[col])

    # Appliquer la standardisation au 'train_data'
    train_lb_st_data[columns_to_standardize] = scaler.fit_transform(train_lb_st_data[columns_to_standardize])

    # Appliquer la standardisation au 'test_data'
    test_lb_st_data[columns_to_standardize] = scaler.transform(test_lb_st_data[columns_to_standardize])

    return train_lb_st_data, test_lb_st_data


def train_model_function(train_data):
    """
    Entraîne un modèle XGBoost Classifier avec les paramètres par défaut.
    Args:
    -----
        train_data (pd.DataFrame): Un DataFrame pandas contenant les données d'entraînement.
    Returns:
    -----
        xgb.XGBClassifier: Un modèle XGBoost Classifier entraîné.
    """
    # Séparez les caractéristiques (X) de la cible (y)
    X_train_XGBC = train_data.drop(columns=['y'])
    y_train_XGBC = train_data['y']

    # Créez et entraînez le modèle XGBoost Classifier avec les paramètres par défaut
    model_XGBC = xgb.XGBClassifier()
    model_XGBC.fit(X_train_XGBC, y_train_XGBC)

    return model_XGBC
