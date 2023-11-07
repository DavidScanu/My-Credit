from functions import import_data_function, preprocess_data, labelize_standardize_data_function, train_model_function
import mlflow
import os
import sys
from mlflow.models import infer_signature


## Import des données
data, data_test = import_data_function()


## Preprocess des données
data = preprocess_data(data)
data_test = preprocess_data(data_test)


## Labellisation et standardisation des données
data, data_test = labelize_standardize_data_function(data, data_test)


## Entraînement du modèle
model = train_model_function(data)


## Configuration du projet MLflow
# Crédentials d'accès à AWS
os.environ['AWS_ACCESS_KEY_ID'] = "AKIA3R62MVALHESATEYJ"
os.environ['AWS_SECRET_ACCESS_KEY'] = "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"
os.environ['ARTIFACT_STORE_URI'] = "s3://isen-mlflow/models/"
os.environ['BACKEND_STORE_URI'] = "postgresql://eagbhergisskna:6e299604b7204f81d625807348dd55dd6d33d426eb2d33762b54c1dcf7367112@ec2-3-214-103-146.compute-1.amazonaws.com:5432/d9ov3338s1olla"
# Connexion à MLflow
mlflow.set_tracking_uri("https://isen-mlflow-fae8e0578f2f.herokuapp.com/")
# Configuration de l'autolog
mlflow.sklearn.autolog()
# Connexion à une expérience
experiment = mlflow.get_experiment_by_name(
                                           "ISEN - Groupe 4"  # Nom de l'expérience de votre groupe
                                            )


## Sauvegarde via MLFlow
# Utilisez sys.argv pour récupérer le run_name en tant qu'argument en ligne de commande
run_name = sys.argv[1]

# Infer signature : obtention des informations sur les colonnes en entrée
signature = infer_signature(data.drop("y", axis=1), data["y"])

with mlflow.start_run(experiment_id=experiment.experiment_id, run_name=run_name):
    # Log des métriques
    mlflow.log_metric("train_score", model.score(data.drop("y", axis=1), data["y"]))


    mlflow.sklearn.log_model(model,                     # Sauvegarde du modèle
                            "model_my-credit",          # Nom du modèle
                            signature=signature,        # Informations sur les colonnes en entrée
                            input_example=data.drop("y", axis=1).head(1),  # Exemple d'entrée
                            registered_model_name="my-credit_model"   # Nom du modèle enregistré
                            )

print("Entraînement et suivi via MLFlow terminés.")