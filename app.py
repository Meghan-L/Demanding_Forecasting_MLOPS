import streamlit as st
import pandas as pd
from src.Demanding_Forecasting.components.prediction import PredictionProvider

st.set_page_config(page_title="Product Forecasting Optimizer", page_icon="📈")

st.title("Product Demand Forecasting")
st.markdown("""
Welcome to the **Demand Forecasting System**. 
This engine helps e-commerce businesses minimize stockouts and reduce overstocking 
by predicting monthly product demand with high precision.
""")

st.divider()

st.subheader("Enter Forecast Parameters")
col1, col2 = st.columns(2)

months = ["January", "February", "March", "April", "May", "June", 
          "July", "August", "September", "October", "November", "December"]

with col1:
    year = st.number_input("Select Planning Year", min_value=2024, max_value=2050, value=2026)

with col2:
    month_name = st.selectbox("Select Target Month", options=months)
    
    # Mapping name to number (1-12) to match our backend month_val
    month_val = months.index(month_name) + 1

if st.button("🚀 Calculate Forecast", use_container_width=True):
    try:
        # Pass a simple list [year, month_val]
        obj = PredictionProvider()
        prediction = obj.predict(year, month_val)
        
        st.success(f"Prediction generated for {month_name} {year}")
        st.metric(label="Estimated Demand Units", value=f"{prediction:.2f}")
        st.divider()
        
        st.subheader("💡 Inventory Action Plan")

        safety_stock = prediction * 0.20
        total_required = prediction + safety_stock

        c1, c2 = st.columns(2)
        c1.warning(f"**Safety Stock Needed:** {safety_stock:.0f} units")
        c2.info(f"**Recommended Reorder Level:** {total_required:.0f} units")

        st.caption("Calculation based on 20% safety margin to prevent stockouts.")
        st.info("Note: This prediction is based on the Random Forest Regressor trained in your pipeline.")
                
    except Exception as e:
        st.error("Prediction failed. Ensure the model is trained in the artifacts folder.")
        st.write(f"Error details: {e}")

st.sidebar.header("Project Info")
st.sidebar.text("Developer: L Surya Meghan")
st.sidebar.info("ECE B.TECH| JNTUK")