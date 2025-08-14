#House Price Prediction – Linear Regression

This project is a **Flask-based web application** that predicts house prices based on features such as square footage, number of bedrooms, and bathrooms.  
It uses a **Linear Regression model** trained on the `House_sale_prediction.csv` dataset.

---

## 📂 Project Structure

```
House_Price_Prediction/
│
├── app.py                      # Flask app for prediction
├── train_model.py              # Script to train and save the model
├── House_sale_prediction.csv   # Dataset
├── Linear_Regression_Model.yaml# Model description/configuration (optional)
├── requirements.txt            # Python dependencies
├── README.md                   # Project documentation
│
├── model/
│   ├── lr_model.pkl            # Saved Linear Regression model
│   └── scaler.pkl              # Saved StandardScaler object
│
├── templates/
│   ├── home.html               # Homepage with input form
│   └── result.html             # Result display page
```

---

##Installation & Setup

1. **Clone the repository**  
   ```bash
   git clone <your-repo-url>
   cd House_Price_Prediction
   ```

2. **Create & activate virtual environment** (optional but recommended)  
   ```bash
   python -m venv venv
   source venv/bin/activate    # macOS/Linux
   venv\Scripts\activate       # Windows
   ```

3. **Install dependencies**  
   ```bash
   pip install -r requirements.txt
   ```

4. **Train the model** (if model files are not present)  
   ```bash
   python train_model.py
   ```

5. **Run the Flask app**  
   ```bash
   python app.py
   ```

6. **Access the app in your browser**  
   ```
   http://127.0.0.1:5000/
   ```

---

## Usage

1. Open the web app in your browser.
2. Enter:
   - **sqft_living** – Total living area in square feet
   - **bedrooms** – Number of bedrooms
   - **bathrooms** – Number of bathrooms
3. Click **Predict**.
4. The app will display the **predicted house price** in Indian Rupees (₹).

---

##Dependencies

From `requirements.txt`:
```
Flask==2.3.2
pandas==2.2.2
numpy==1.26.4
scikit-learn==1.4.2
joblib==1.4.2
```

---

##Model Details

- **Algorithm:** Linear Regression
- **Features used:**  
  - `sqft_living`  
  - `bedrooms`  
  - `bathrooms`
- **Data Scaling:** StandardScaler
- **Dataset:** `House_sale_prediction.csv`

---

##Notes
- The trained model and scaler are stored in the `model/` directory.
- You can modify `train_model.py` to use different features or algorithms.
- Make sure `templates/` contains `home.html` and `result.html` for the app to run.
