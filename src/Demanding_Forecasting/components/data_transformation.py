import os
import pandas as pd
from sklearn.model_selection import train_test_split
from Demanding_Forecasting import logger

class DataTransformation:
    def __init__(self, config):
        self.config = config

    def train_test_splitting(self):
        try:
            data = pd.read_csv(self.config.data_path)
            date_col = next((col for col in data.columns if 'date' in col.lower() or 'month' in col.lower()), None)

            if date_col:
                month_map = {
                    'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'June': 6,
                    'July': 7, 'Aug': 8, 'Sept': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12
                }
                
                data['month_val'] = data[date_col].str.strip().str.title().str[:3].map(month_map)
                data = data.select_dtypes(exclude=['object']) 
                
                if 'year' not in data.columns:
                    data['year'] = 2026

            train, test = train_test_split(data, test_size=0.2)
            os.makedirs(self.config.root_dir, exist_ok=True)
            
            train.to_csv(os.path.join(self.config.root_dir, "train.csv"), index=False)
            test.to_csv(os.path.join(self.config.root_dir, "test.csv"), index=False)
            
            logger.info("Transformation complete: Exported cleaned numerical data.")

        except Exception as e:
            raise e