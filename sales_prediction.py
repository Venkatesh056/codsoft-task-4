# -*- coding: utf-8 -*-
"""Sales_prediction

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1hKfAsdGCYIbeTAFkEux6mxoILUfpTTUi
"""

import pandas as pd

df=pd.read_csv('/content/sample_data/advertising.csv')

#mean, median, and standard deviation for each column
 summary_stats = df.describe()
print(summary_stats)

# Correlation matrix
correlation_matrix = df.corr()
print(correlation_matrix)

import matplotlib.pyplot as plt

# Scatter plot for TV vs Sales
plt.figure(figsize=(8, 6))
plt.scatter(df['TV'], df['Sales'], color='blue')
plt.title('TV Advertising Budget vs Sales')
plt.xlabel('TV Advertising Budget (in thousands)')
plt.ylabel('Sales (in thousands)')
plt.grid(True)
plt.show()

# Scatter plot for Radio vs Sales
plt.figure(figsize=(8, 6))
plt.scatter(df['Radio'], df['Sales'], color='red')
plt.title('Radio Advertising Budget vs Sales')
plt.xlabel('Radio Advertising Budget (in thousands)')
plt.ylabel('Sales (in thousands)')
plt.grid(True)
plt.show()

# Scatter plot for Newspaper vs Sales
plt.figure(figsize=(8, 6))
plt.scatter(df['Newspaper'], df['Sales'], color='green')
plt.title('Newspaper Advertising Budget vs Sales')
plt.xlabel('Newspaper Advertising Budget (in thousands)')
plt.ylabel('Sales (in thousands)')
plt.grid(True)
plt.show()

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

X = df[['TV']]
y = df['Sales']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create the model
model = LinearRegression()

model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Mean Squared Error: {mse}")
print(f"R^2 Score: {r2}")

# Plot the regression line
plt.figure(figsize=(8, 6))
plt.scatter(X_test, y_test, color='blue')
plt.plot(X_test, y_pred, color='red', linewidth=2)
plt.title('TV Advertising Budget vs Sales (Test Data)')
plt.xlabel('TV Advertising Budget (in thousands)')
plt.ylabel('Sales (in thousands)')
plt.grid(True)
plt.show()

# Highest sales
highest_sales = df[df['Sales'] == df['Sales'].max()]
print("Highest Sales:\n", highest_sales)

# Lowest sales
lowest_sales = df[df['Sales'] == df['Sales'].min()]
print("Lowest Sales:\n", lowest_sales)

import seaborn as sns

# Distribution plot for Sales
plt.figure(figsize=(8, 6))
sns.histplot(df['Sales'], kde=True, color='purple')
plt.title('Distribution of Sales')
plt.xlabel('Sales (in thousands)')
plt.ylabel('Frequency')
plt.show()

# Pair plot
sns.pairplot(df)
plt.show()

X = df[['TV', 'Radio', 'Newspaper']]  # Using all three advertising budgets as independent variables
y = df['Sales']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create the model
model = LinearRegression()

# Train the model
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Mean Squared Error: {mse}")
print(f"R^2 Score: {r2}")

# Feature importance (coefficients)
coefficients = pd.DataFrame(model.coef_, X.columns, columns=['Coefficient'])
print(coefficients)

residuals = y_test - y_pred

# Plot the residuals
plt.figure(figsize=(8, 6))
plt.scatter(y_pred, residuals, color='blue')
plt.axhline(y=0, color='red', linestyle='--')
plt.title('Residuals vs Predicted Values')
plt.xlabel('Predicted Values')
plt.ylabel('Residuals')
plt.grid(True)
plt.show()

from sklearn.preprocessing import PolynomialFeatures

# Transform features to polynomial features
poly = PolynomialFeatures(degree=2)
X_poly = poly.fit_transform(X)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_poly, y, test_size=0.2, random_state=42)

# Create and train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

#Evaluate the model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Mean Squared Error: {mse}")
print(f"R^2 Score: {r2}")

from sklearn.preprocessing import StandardScaler

# Normalize the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

from sklearn.model_selection import cross_val_score

# Cross-validation
scores = cross_val_score(model, X, y, cv=5, scoring='r2')
print(f"Cross-Validation R^2 Scores: {scores}")
print(f"Mean R^2 Score: {scores.mean()}")

