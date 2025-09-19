import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np

# Load dataset
file_path = "anxiety-disorders-prevalence-by-age.xltx"
df = pd.read_excel(file_path, sheet_name="Sheet1")

# Get list of available countries
countries = df["Entity"].unique()
print("Available countries in dataset:")
print(", ".join(countries[:20]), "...")  # show first 20 as a preview

# Ask user for country
country = input("\nEnter a country name: ")

# Check if country exists
if country not in countries:
    print(f"❌ '{country}' not found in dataset. Please check spelling.")
else:
    df_country = df[df["Entity"] == country]

    # Feature & target
    X = df_country[["Year"]]
    y = df_country["Anxiety disorders (share of population) - Sex: Both - Age: All ages"]

    if len(X) < 5:
        print(f"⚠️ Not enough data available for {country}")
    else:
        # Train model
        model = LinearRegression()
        model.fit(X, y)

        # Predictions
        y_pred = model.predict(X)

        # Future years (2021–2030)
        future_years = np.array(range(2021, 2031)).reshape(-1, 1)
        future_preds = model.predict(future_years)

        # Plot
        plt.figure(figsize=(8,5))
        plt.scatter(X, y, color="blue", label="Actual Data")
        plt.plot(X, y_pred, color="red", label="Predicted Trend")
        plt.plot(future_years, future_preds, color="orange", linestyle="--", label="Future Prediction")
        plt.title(f"Anxiety Disorder Prevalence Prediction ({country})")
        plt.xlabel("Year")
        plt.ylabel("Prevalence (% of population)")
        plt.legend()
        plt.grid(True)
        plt.show()
