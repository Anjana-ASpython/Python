import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# -------------------------------- DATA --------------------------------

# 1. Load dataset from CSV file
file_path = r"C:\Users\pc24\Downloads\50_startups_sample.csv"  # Update this to your actual file path
df = pd.read_csv(file_path)

# Display first few rows
print("Dataset preview:")
print(df.head())


# Convert categorical 'State' column into dummy variables
df = pd.get_dummies(df, columns=['State'], drop_first=True)

# Handle missing values (fill with median)
df = df.fillna(df.median())


# 2. Prepare features and target
X = df.drop(columns=['Profit'])
y = df['Profit']

# 3. Split the dataset into training and test sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# ------------------------- MODEL CREATION -----------------------------

# 4. Train a Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)

# -------------------------- EVALUATION -------------------------------

# 5. Predict on the test set
y_pred = model.predict(X_test)

print("\nModel Evaluation Metrics:")
print("Mean Squared Error:", mean_squared_error(y_test, y_pred))
print("R² Score:", r2_score(y_test, y_pred))

# Plot actual vs predicted
plt.scatter(y_test, y_pred)
plt.xlabel("Actual Profit")
plt.ylabel("Predicted Profit")
plt.title("Actual vs Predicted Profit")
plt.show()

# Plot heatmap of correlations
plt.figure(figsize=(10,8))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
plt.title("Correlation Matrix")
plt.show()

# --------------------- CONFUSION MATRIX FOR REGRESSION ---------------------

# Define a threshold to classify profits into categories
threshold = y.mean()  # Or choose a specific threshold
print(f"\nUsing threshold {threshold:.2f} to classify profits into High/Low categories.")

# Convert actual and predicted profits into categories
y_test_class = (y_test >= threshold).astype(int)
y_pred_class = (y_pred >= threshold).astype(int)

# Confusion Matrix
cm = confusion_matrix(y_test_class, y_pred_class)
plt.figure(figsize=(5,4))
sns.heatmap(cm, annot=True, fmt="d", cmap="Blues",
            xticklabels=["Low Profit", "High Profit"],
            yticklabels=["Low Profit", "High Profit"])
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.title("Confusion Matrix for Profit Classification")
plt.show()

# ----------------------- USER INPUT PREDICTION -----------------------

print("\n--- Predict Profit Based on User Input ---")

try:
    rd_spend = float(input("Enter R&D Spend: "))
    admin = float(input("Enter Administration Spend: "))
    marketing = float(input("Enter Marketing Spend: "))
except ValueError:
    print("Invalid input! Please enter numeric values.")
    exit()

state_input = input("Enter State (New York, California, Florida): ").strip()

# Create user input as a DataFrame
user_dict = {
    'R&D Spend': rd_spend,
    'Administration': admin,
    'Marketing Spend': marketing,
    'State_California': 0,
    'State_Florida': 0,
    'State_New York': 0
}

# List of valid states
valid_states = ["New York", "California", "Florida"]
state_column = f"State_{state_input}"

if state_input in valid_states:
    user_dict[state_column] = 1
else:
    print("Warning: State not recognized. Using all zeros.")

user_df = pd.DataFrame([user_dict])

# Predict the profit
user_prediction = model.predict(user_df)[0]
print(f"\nPredicted Profit: {user_prediction:.2f}")
