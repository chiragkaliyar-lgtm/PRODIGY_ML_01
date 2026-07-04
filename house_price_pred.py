import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Load dataset
df = pd.read_csv("train.csv")

# Select only required columns
data = df[["GrLivArea", "BedroomAbvGr", "FullBath", "SalePrice"]]

# Display first five rows
print(data.head())

# Features (input)
X = data[["GrLivArea", "BedroomAbvGr", "FullBath"]]

# Target (output)
y = data["SalePrice"]

print("\nFeatures:")
print(X.head())

print("\nTarget:")
print(y.head())


# Split dataset into training and testing sets

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("Training Features:", X_train.shape)
print("Testing Features:", X_test.shape)

print("Training Target:", y_train.shape)
print("Testing Target:", y_test.shape)

# Create the Linear Regression model
model = LinearRegression()

# Train the model
model.fit(X_train, y_train)

print("Model trained successfully!")

# Predict house prices on the test data
predictions = model.predict(X_test)

print("First 10 Predictions:")
print(predictions[:10])

comparison = pd.DataFrame({
    "Actual Price": y_test.values,
    "Predicted Price": predictions
})

print(comparison.head(10))

# Evaluate the model

mse = mean_squared_error(y_test, predictions)
r2 = r2_score(y_test, predictions)

print("\nMean Squared Error (MSE):", mse)
print("R² Score:", r2)

plt.figure(figsize=(8,6))
plt.scatter(y_test, predictions)

plt.xlabel("Actual House Price")
plt.ylabel("Predicted House Price")
plt.title("Actual vs Predicted House Prices")

plt.show()

print("\nIntercept:", model.intercept_)

coefficients = pd.DataFrame({
    "Feature": X.columns,
    "Coefficient": model.coef_
})

print(coefficients)

import joblib

joblib.dump(model, "model.pkl")

print("Model saved successfully!")