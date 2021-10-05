""" read data from data source
preproceess it, create corpus
and store it in data raw folder"""

import os
from get_data import read_params, get_data
import argparse
import numpy as np
import pandas as pd

def load_and_save(config_path):
    config = read_params(config_path)
    df = get_data(config_path)
    raw_data_path = config["load_data"]["raw_dataset_csv"]
    df["label"] = df.annotation.apply(lambda x: x.get('label'))
    df["label"] = df.label.apply(lambda x: x[0])
    df['label']=df['label'].astype(int)
    df.drop(['extras'],inplace=True,axis=1) 
    df.to_csv(raw_data_path, index=False)


 # run comment
if __name__ == "__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config", default="params.yaml")
    parsed_args = args.parse_args()
    load_and_save(config_path=parsed_args.config)