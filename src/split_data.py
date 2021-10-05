import os
import argparse
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from get_data import read_params, get_data

def split_train_test(data,test_ratio):
    """
    Functuion to split dataset into train set and test set it 
    takes dataset and s
    """
    shuffled_indices=np.random.permutation(len(data))
    test_set_size=int(len(data)*test_ratio)
    test_indices=shuffled_indices[:test_set_size]
    train_indices=shuffled_indices[test_set_size:]
    return data.iloc[train_indices],data.iloc[test_indices]



def split_and_save_data(config_path):
    config = read_params(config_path)
    train_data_path = config["split_data"]["train_path"]
    test_data_path = config["split_data"]["test_path"]
    raw_data_path = config["load_data"]["raw_dataset_csv"]
    split_ratio = config["split_data"]["test_size"]
    random_states = config["base"]["random_state"]
    df = pd.read_csv(raw_data_path)
    train, test = split_train_test(df,split_ratio)
    train.to_csv(train_data_path, index=False)
    test.to_csv(test_data_path, index=False)



 # run comment
if __name__ == "__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config", default="params.yaml")
    parsed_args = args.parse_args()
    split_and_save_data(config_path=parsed_args.config)