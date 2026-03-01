import pandas as pd 
import os 
from sklearn.ensemble import RandomForestRegressor
import joblib
from src.Demanding_Forecasting import logger
from src.Demanding_Forecasting.entity.entity_config import ModelTrainerConfig

class ModelTrainer:
    def __init__(self,config:ModelTrainerConfig):
        self.config=config
    
    def train(self):
        try:
            train_data=pd.read_csv(self.config.train_data_path)
            test_data=pd.read_csv(self.config.test_data_path)
            train_x=train_data.drop([self.config.target_column],axis=1)
            train_y=train_data[[self.config.target_column]]
            logger.info("Successfully loaded the training and testing data for Model Training")
            test_x=test_data.drop([self.config.target_column],axis=1)
            test_y=test_data[[self.config.target_column]]
            rf=RandomForestRegressor(
                n_estimators=self.config.n_estimators,
                max_depth=self.config.max_depth,
                random_state=42

            )
            logger.info(f"The random forest model is being trained with {self.config.n_estimators}")
            rf.fit(train_x,train_y.values.ravel())
            save_path=os.path.join(self.config.root_dir,self.config.model_name)
            joblib.dump(rf,save_path)
            logger.info(f"The Model has been successfully saved at {save_path} ")

        except Exception as e:
            logger.error(f"Error Occurred in Model Training :{e}")
            raise e 




