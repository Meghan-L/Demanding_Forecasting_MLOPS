import os 
from box.exception import BoxValueError
import yaml
from Demand_Forecasting import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any 

@ensure_annotations
def read_yaml(path_to_yaml:Path)->ConfigBox:
    try :
        with open(path_to_yaml) as yaml_file:
            content=yaml.safe_load(yaml_file)
            logger.info("the yaml file {path_to_yaml} has been read successfully ")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file not found")
    except Exception as e:
        raise e 
def create_directories(path_to_directories: list ,verbose=True):
    for path in path_to_directories:
        os.makedirs(path,exist_ok=True)
        if verbose:
            logger.info("created a directory at {path}")

@ensure_annotations
def get_size(path:Path)->str:
    size_in_kb=round(os.path.getsize(path).1024)
    return f"the size of the file is {size_in_kb} KB"

