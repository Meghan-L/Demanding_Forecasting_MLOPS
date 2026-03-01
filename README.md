# Demanding_Forecasting_MLOPS
A solid README.md is what transforms a "folder of code" into a Professional Portfolio Project. Since you’re presenting this at JNTUK, we should highlight the MLOps structure and the Random Forest implementation.

Here is a clean, formatted template you can copy and paste into a file named README.md in your project's root directory.

 E-Commerce Product Demand Forecasting
Developer: L Surya Meghan
ECE Junior | University College of Engineering Kakinada (JNTUK)

 Project Overview
This project is an end-to-end Machine Learning Pipeline designed to solve the "Overstocking vs. Stockout" dilemma in e-commerce. By utilizing a Random Forest Regressor, the system predicts monthly product demand based on historical trends, allowing businesses to optimize their inventory and safety stock levels.

Technical Stack
Language: Python 3.12

Modeling: Scikit-Learn (Random Forest Regressor)

Data Handling: Pandas, NumPy

Web Framework: Streamlit (Interactive UI)

Architecture: Modular MLOps (Components, Pipelines, Artifacts)

 Key Features
Interactive Forecasts: Predict demand for any month in the future (e.g., 2026-2030).

Inventory Action Plan: Automatically calculates 20% Safety Stock and Recommended Reorder Levels.

Modular Pipeline: Clean separation between Data Transformation, Model Training, and Prediction.

Feature Alignment: Dynamic dictionary mapping ensures the UI always matches the model's training schema.

Demand_Forecasting_Project/
├── artifacts/                # Trained model (.joblib) and processed data
├── src/
│   └── Demanding_Forecasting/
│       ├── components/       # Data Transformation, Trainer, Predictor
│       └── pipeline/         # Training and Prediction Pipelines
├── app.py                    # Streamlit Web Application
├── main.py                   # Script to trigger the full pipeline
├── requirements.txt          # Project dependencies
└── README.md                 # Project documentation

📊 Model Performance
The system uses a Random Forest Regressor to capture non-linear seasonality in retail data.

Input Features: Year, Month (Numerical), and One-Hot Encoded Product Categories.

Output: Estimated units required for the following month

How to run 
1) Clone the repository
2) Install dependencies
        pip install -r requirements.txt
3) Train the Model  
        python main.py
4) Launch the UI
        streamlit run app.py
