'''
✅ What is Machine Learning?

You use the training set to teach the model how to make predictions.

Machine learning (ML) is a branch of artificial intelligence (AI) where computers learn patterns from data and make decisions or predictions without being explicitly programmed for every case.

📌 Types of Machine Learning

Supervised Learning

Model learns from labeled data (input → correct output).

Example: Predicting house prices based on features like area, location.

Unsupervised Learning

Model finds patterns without labels.

Example: Grouping customers based on purchasing behavior.

Reinforcement Learning

Model learns by interacting with an environment and receiving rewards or penalties.

Example: Self-learning robots, game-playing AI.



📌 Basic Steps in Machine Learning

Data Collection → Data Cleaning → Feature Selection → Encoding → Scaling → Splitting
       ↓
 Model Selection → Training → Validation → Testing → Performance Analysis → Improvement
       ↓
 Final Training → Saving → Deployment → Monitoring

 

📌 Where Exactly Does Preprocessing Happen?

Data Collection → **Preprocessing** → Splitting → Model Training → Validation → Testing → Deployment

Preprocessing happens:
✔ Immediately after collecting the raw data
✔ Before splitting it into train/test sets
✔ Sometimes also applied after splitting (e.g., scaling fitted only on training data and applied to test data)



✅ Why pandas is Imported
📦 Pandas is for Data Handling

It helps in organizing, manipulating, and analyzing structured data (like tables, spreadsheets, CSV files).

It makes it easy to:

Load datasets.

Select columns and rows.

Filter, aggregate, and transform data.

Handle missing values and work with time series.


✅ Why numpy is Imported
📦 NumPy is for Numerical Operations

It provides support for efficient array operations and mathematical computations.

Used for linear algebra, random number generation, and scientific computing.

📊 Where It’s Used

Even if it's not explicitly used in your house price code, libraries like scikit-learn internally rely on numpy arrays for computations. For example:

The feature matrix X and target vector y are automatically converted to numpy arrays.

Operations like fitting the model and calculating errors use efficient matrix math handled by numpy.

✅ Why matplotlib is Imported
📦 Matplotlib is for Visualization

It helps you create graphs, charts, and plots to understand the data, inspect model performance, and communicate results.

Visualizing data gives you insights like:

How data is distributed

Whether there’s a relationship between variables

How well your model fits the data


✅ Why sklearn is Imported
📦 scikit-learn (sklearn) is for Machine Learning

It’s a powerful library that provides tools for:

Splitting datasets

Applying machine learning algorithms

Preprocessing data

Evaluating models using metrics

Tuning parameters, cross-validation, etc.

📌 Summary Table
Library	Purpose	Example Use
matplotlib	Create plots and graphs	Scatter plot of data, regression line, axis labels
sklearn	Apply machine learning algorithms and evaluation	Splitting data, training the model, calculating error metrics
'''
