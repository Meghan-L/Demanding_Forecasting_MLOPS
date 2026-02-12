import os 
from Demanding_Forecasting import logger 
from sklearn.model_selection import train_test_split
import pandas as pd
from Demanding_Forecasting.entity.entity_config import DataTransformationConfig


class DataTransformation:
    def __init__(self,config:DataTransformationConfig):
        self.config=config
    def train_test_splitting(self):
        try:
            with open(self.config.STATUS_FILE, "r") as f:
                # read().strip() removes newlines or hidden spaces
                status = f.read().strip()

            # We check if 'True' is anywhere in that string
            if "True" in status:
                data = pd.read_csv(self.config.data_path)
                train, test = train_test_split(data, test_size=self.config.test_size)

                train.to_csv(os.path.join(self.config.root_dir, "train.csv"), index=False)
                test.to_csv(os.path.join(self.config.root_dir, "test.csv"), index=False)

                logger.info("Splitted data into training and test sets")
            else:
                raise Exception("Data schema validation failed! Check artifacts/data_validation/status.txt")

        except Exception as e:
            raise e