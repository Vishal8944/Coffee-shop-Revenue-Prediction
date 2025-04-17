import streamlit as st
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error
import pickle

# Load model and scaler
model = pickle.load(open('model.pkl', 'rb'))
scaler = pickle.load(open('scalar.pkl', 'rb'))

# Page config
st.set_page_config(page_title="Coffee Shop Revenue Predictor ☕", layout="wide")

# Layout with columns
left_col, right_col = st.columns([2, 1])

# Main title
left_col.title("📊 Coffee Shop Daily Revenue Predictor")
left_col.markdown("Use the sidebar to enter your coffee shop metrics and predict **daily revenue**.")

# Right column: About section
with right_col.expander("📘 About this Project", expanded=True):
    st.markdown("""
    This app predicts the **daily revenue** of a coffee shop using machine learning.
    
    🔹 Built with a **Random Forest Regressor** trained on actual sales data.  
    🔹 Input metrics like customers, employees, marketing spend, etc.  
    🔹 Output is a predicted dollar value of expected revenue.  
    🔹 Helps shop owners make data-driven decisions.  
    🔹 Powered by **Streamlit** + **Scikit-learn**.  
    🔹 Simple, intuitive, and insightful.  
    🔹 Sliders ensure smooth data entry and validation.  
    🔹 Predictions are scaled internally using `StandardScaler`.  
    🔹 Ideal for coffee business planning and analysis.
    """)

# Sidebar inputs
st.sidebar.header("🧾 Input Shop Metrics")
cust = st.sidebar.slider("Number of Customers Per Day", 0, 1000, 150)
order_val = st.sidebar.slider("Average Order Value ($)", 0.0, 50.0, 25.0, step=0.5)
hours = st.sidebar.slider("Operating Hours Per Day", 0.0, 24.0, 10.0, step=1.0)
employees = st.sidebar.slider("Number of Employees", 0, 20, 8)
marketing = st.sidebar.slider("Marketing Spend Per Day ($)", 0.0, 2000.0, 500.0, step=10.0)
foot_traffic = st.sidebar.slider("Location Foot Traffic", 0, 10000, 5000, step=100)

# Predict button
if left_col.button("🔍 Predict Revenue"):
    user_input = np.array([[cust, order_val, hours, employees, marketing, foot_traffic]])
    user_input_scaled = scaler.transform(user_input)
    predicted_revenue = model.predict(user_input_scaled)

    left_col.success(f"💰 Predicted Daily Revenue: **${predicted_revenue[0]:,.2f}**")
    left_col.balloons()
