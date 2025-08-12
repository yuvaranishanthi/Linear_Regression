import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
import pickle
import os

# Load dataset
df = pd.read_csv("House_sale_prediction.csv")

# Select features and target (you can modify these as per your dataset)
X = df[['sqft_living', 'bedrooms', 'bathrooms']]  # example features
y = df['price']  # target variable

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Scale data
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)

# Train model
model = LinearRegression()
model.fit(X_train_scaled, y_train)

# Save model and scaler
os.makedirs("model", exist_ok=True)
pickle.dump(model, open("model/lr_model.pkl", "wb"))
pickle.dump(scaler, open("model/scaler.pkl", "wb"))

print("Model and scaler saved successfully.")
