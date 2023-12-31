

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report

# Load the dataset (replace 'your_dataset.csv' with the actual dataset file)
dataset = pd.read_csv('creditcard.csv')

# Check for missing values
print(dataset.isnull().sum())

# Drop rows with missing values
dataset = dataset.dropna()

# Split the dataset into features (X) and target (y)
X = dataset.drop('Class', axis=1)  # Assuming 'Class' column represents the target
y = dataset['Class']

# Split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Standardize the features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Initialize and train a logistic regression model
model = LogisticRegression()
model.fit(X_train_scaled, y_train)

# Make predictions
y_pred = model.predict(X_test_scaled)

# Evaluate the model
report = classification_report(y_test, y_pred)
print(report)
