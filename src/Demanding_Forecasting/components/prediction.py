import joblib
import pandas as pd
from pathlib import Path

class PredictionProvider:
    def __init__(self):
        self.model = joblib.load(Path('artifacts/model_trainer/model.joblib'))

    def predict(self, year, month_val):
        expected_features = self.model.feature_names_in_

        full_input = {feature: 0 for feature in expected_features}
        full_input['year'] = year
        full_input['month_val'] = month_val

        df = pd.DataFrame([full_input])[expected_features]
        prediction = self.model.predict(df)

        # Return the first element so it's a float, not an array
        return prediction[0]