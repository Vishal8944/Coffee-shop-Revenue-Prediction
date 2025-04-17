

# ☕️ Coffee Shop Revenue Predictor 📊

Welcome to the **Coffee Shop Revenue Predictor** — a complete data science project that uses machine learning to estimate the **daily revenue** of a coffee shop based on various operational factors. It's designed to help café owners and business analysts make smarter, data-driven decisions.

---

## 🚀 What's Inside?

### 📦 Project Highlights:
- Trained and compared **multiple regression models**:
  - Linear Regression 📈
  - Decision Tree Regressor 🌳
  - Support Vector Regressor (SVR) 💡
  - Random Forest Regressor 🌲 *(Best-performing model)*
- Built an interactive **Streamlit web app** for real-time predictions
- Implemented **feature scaling**, **data visualization**, and **model evaluation**
- Saved trained models and scalers using `pickle` for deployment

---

## 📊 Input Features

These are the business metrics used to predict revenue:

| Feature                        | Description                                      |
|-------------------------------|--------------------------------------------------|
| 🧍 Customers Per Day           | Total number of daily visitors                   |
| 💵 Average Order Value         | Average sale value per customer ($)             |
| ⏰ Operating Hours             | Daily hours the shop is open                     |
| 👥 Employees                  | Total number of working staff                    |
| 📢 Marketing Spend             | Daily advertising/marketing budget ($)          |
| 🚶 Location Foot Traffic       | Estimated footfall around the coffee shop       |

---

## 🧠 Machine Learning Workflow

1. **Data Cleaning & Preprocessing**:
   - Handled missing values and standardized numeric features using `StandardScaler`.

2. **Model Training & Evaluation**:
   - Tried out 4 regression models:  
     ✅ *Random Forest Regressor* had the highest R² score and lowest error.
   - Used metrics like:
     - R² Score
     - Mean Absolute Error (MAE)
     - Mean Squared Error (MSE)

3. **Model Tuning**:
   - Performed **GridSearchCV** to optimize Random Forest hyperparameters.

4. **Model Saving**:
   - Stored the final model (`model.pkl`) and scaler (`scalar.pkl`) for use in the web app.

---

## 🌐 Streamlit Web App

Launch an interactive UI to test your business scenarios!

### Features:
- 🎛 Slider-based input controls for easy data entry
- 🔍 Instant predictions with Random Forest model
- 🎉 Fun animations like balloons on result display
- 📘 Project description & context right in the app

### Run it locally:

```bash
pip install -r requirements.txt
streamlit run app.py
```

---

## 📁 Repository Structure

```
├── app.py                     # Streamlit web app
├── model.pkl                  # Trained Random Forest model
├── scalar.pkl                 # Scaler for input transformation
├── coffee_shop_revenue.csv    # Dataset
├── model_training.ipynb       # Jupyter notebook for training & evaluation
├── README.md
└── requirements.txt
```

---

## 📈 Example Output

> Input: 150 customers, $25 order value, 10 hrs, 8 employees, $500 marketing, 5000 foot traffic  
> Output: 💰 **Predicted Daily Revenue: $4,932.47**

---

## 💡 Future Improvements

- Add model interpretability (SHAP / Feature Importance)
- Extend dataset with external factors (weather, events)
- Deploy the app on the web (e.g., Streamlit Cloud / Heroku)
- Include user-upload CSV for batch predictions

---

## 🤝 Contributing

Want to improve the model, add new features, or enhance the UI?  
You're welcome to fork, clone, and contribute. PRs are always appreciated! 🚀
