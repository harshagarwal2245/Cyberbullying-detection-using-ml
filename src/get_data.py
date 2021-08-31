"""read params.yaml 
preprocess it 
return dataframe"""
import os
import yaml 
import pandas as pd
import argparse

def read_params(config_path):
    """
    Read the params file and intrepret it for configurations
    input:Path to params file 
    output: return dictonary of configuration
    """
    with open(config_path) as yaml_file:
        config=yaml.safe_load(yaml_file)
    return config 

def get_data(config_path):
    """
    Read the configuration path which had data directory
    after parsing it convert json file to dataframe
    with help of pandas return data frame 
    input: config path
    output: dataframe
    """
    config=read_params(config_path)
    data_path=config["data_source"]["s3_source"]
    df=pd.read_json(data_path,lines=True,orient='str')
    return df



if __name__=='__main__':
    args=argparse.ArgumentParser()
    args.add_argument("--config",default="params.yaml")
    parsed_args=args.parse_args()
    get_data(config_path=parsed_args.config)