# can you predict wine quality score based on chemical properties?
# linearregression

'''Linear Regression → predicts continuous numbers (like 5.37, 6.89).

Logistic Regression → predicts categories/classes (like good vs bad wine, or quality = 3, 4, 5…).

 Main Differences Side by Side
Step	Linear Regression	Logistic Regression
Import	from sklearn.linear_model import LinearRegression	from sklearn.linear_model import LogisticRegression
Target y	Can stay numeric (quality scores)	Must be categorical (binary or multiclass)
Model	model = LinearRegression()	model = LogisticRegression(max_iter=5000)
Prediction	y_pred = model.predict(X_test) (floats)	y_pred = model.predict(X_test) (class labels)
Evaluation	mean_squared_error, r2_score	accuracy_score, classification_report, confusion_matrix
Visualization	Scatter plot (actual vs predicted)	Confusion matrix / bar chart

✅ So the data preparation & splitting parts are the same.
✅ The fit & predict steps look similar.
❌ Only model choice and evaluation differ.

'''
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score, accuracy_score, confusion_matrix, classification_report


file_path = r"C:\Users\pc24\Desktop\python_project\project\winequality_red.csv"
df = pd.read_csv(file_path)
X = df.drop("quality", axis=1)
y = df["quality"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print("Mean Squared Error:", mse)
print("R2 Score:", r2)
plt.figure(figsize=(8,6))
plt.scatter(y_test, y_pred, alpha=0.6, color="blue")
plt.xlabel("Actual Quality")
plt.ylabel("Predicted Quality")
plt.title("Wine Quality Prediction (Linear Regression)")
plt.plot([y.min(), y.max()], [y.min(), y.max()], "r--")  
plt.show()
