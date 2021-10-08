from src.get_data import read_params
import argparse
import mlflow 
from mlflow.tracking import MlflowClient 
from pprint import pprint
import joblib 
import os 

def log_production_model(config_path):
    config = read_params(config_path)

    mlflow_config=config["mlflow_config"]
    model_name = mlflow_config["registered_model_name"]
    remote_server_uri = mlflow_config["remote_server_uri"]
    mlflow.set_tracking_uri(remote_server_uri)
    runs = mlflow.search_runs(experiment_ids=1)
    highest= runs["metrics.acc"].sort_values(ascending=False)[0]
    highest_run_id= runs[runs["metrics.acc"]==highest]["run_id"][0]
    #print(highest_run_id)   
    client=MlflowClient()
    for mv in client.search_model_versions(f"name='{model_name}'"):
        mv = dict(mv)
        if mv["run_id"] == highest_run_id:
            current_version = mv["version"]
            logged_model = mv["source"]
            pprint(mv, indent=4)
            client.transition_model_version_stage(
                name=model_name,
                version=current_version,
                stage="Production"
            )
        else:
            current_version = mv["version"]
            client.transition_model_version_stage(
            name=model_name,
            version=current_version,
            stage="Staging"
            )
    loaded_model = mlflow.pyfunc.load_model(logged_model)
    model_path = config["webapp_model_dir"]
    joblib.dump(loaded_model, model_path)



if __name__ == '__main__':
    args = argparse.ArgumentParser()
    args.add_argument("--config", default="params.yaml")
    parsed_args = args.parse_args()
    log_production_model(config_path=parsed_args.config)
