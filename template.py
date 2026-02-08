import os
from pathlib import Path
import logging 
logging.basicConfig(level=logging.INFO,format='[%(asctime)s]:%(message)s:')
project_name="Demanding_Forecasting"
list_files=[
    ".github/workflows/.gitkeep",
    f"src/{project_name}/components/_init__.py",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "schema.yamml",
    "app.py",
    "main.py",
    "Dockerfile",
    "setup.py",
    "requirements.txt"
    

]
for file in list_files:
    filepath=Path(file)
    filedir,filename=os.path.split(filepath)
    if filedir!="":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Creating a directory at {filedir} for the {filename}")
    if  (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath,"w") as f:
            pass
        logging.info(f"Created am empty file with the name {filename}")
    else:
        logging.info(f"the {filename} already exists ")