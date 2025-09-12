import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


'''
✅ Steps Covered
Create a dataset with square footage and price.
Preprocess the data if necessary.
Split the dataset into training and test sets.
Train a linear regression model.
Visualize the Data and Regression Line
Make predictions
model parameters
Evaluate the model.
'''


#1.create a dataset with squarefeet X and price Y

X=np.array([500,800,1000,1200,1500]).reshape(-1,1)  #squarefeet
Y=np.array([1500000,800000,1000000,1200000,150500])  #price

#  2.Preprocessing 
# No missing values or categorical data here, so no extra preprocessing needed.

# Create the Linear Regression model
model = LinearRegression()

# Fit the model with the dataset
model.fit(X, Y)


#visualize

plt.scatter(X, Y, color='blue', label='Actual Data')
plt.plot(X, model.predict(X), color='violet', label='Regression Line')
plt.xlabel('Square Feet')
plt.ylabel('Price')
plt.title('House Price Prediction')
plt.legend()
plt.show()


#make predictions
size=11000
predicted_price = model.predict([[size]])
print(f"Predicted Price for {size}sqft= ${predicted_price:.2f}")

#model parameters
print("Slope (price increase per sq ft):", model.coef_[0])
print("Intercept (base price):", model.intercept_)
