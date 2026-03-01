import pandas as pd
import os 
from sklearn.metrics import root_mean_squared_error, mean_absolute_error,r2_score 
import joblib
import json
from pathlib import Path 
from src.Demanding_Forecasting import logger 
from src.Demanding_Forecasting.entity.entity_config import ModelEvaluationConfig

class ModelEvaluation:
    def __init__(self,config:ModelEvaluationConfig):
        self.config=config
    def save_results(self,metrics):
        with open(self.config.metric_file_name,"w") as f:
            json.dump(metrics, f , indent=4)
        logger.info(f"Metrics are saved to a file with the name {self.config.metric_file_name}")

    def initiate_model_evaluation(self):
        try:
            test_data=pd.read_csv(self.config.test_data_path)
            model=joblib.load(self.config.model_path)
            logger.info("Successfully loaded the test data for model evaluation")

            test_x=test_data.drop([self.config.target_column],axis=1)
            test_y=test_data[[self.config.target_column]]

            predicted_values=model.predict(test_x)

            rmse=root_mean_squared_error(test_y,predicted_values)
            mae=mean_absolute_error(test_y,predicted_values)
            r2=r2_score(test_y,predicted_values)

            metrics={
                "rmse":rmse,
                "mae":mae,
                "r2_score":r2
            }
            logger.info(f"Evaluation Metrics - RMSE: {rmse:.4f}, MAE: {mae:.4f}, R2: {r2:.4f}")
            self.save_results(metrics)


        except Exception as e:
            logger.error(f"Error Occured in Model Evaluation {e}")
            raise e

