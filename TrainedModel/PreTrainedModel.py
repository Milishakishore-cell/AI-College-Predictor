# import pandas as pd
# from sklearn.model_selection import train_test_split
# from sklearn.ensemble import RandomForestClassifier
# from sklearn.metrics import accuracy_score
# import joblib

# # Load the synthetic dataset
# df = pd.read_csv("college_admission_dataset.csv")

# # Define features and target
# X = df.drop("college_admitted", axis=1)  # Features
# y = df["college_admitted"]  # Target

# # Convert categorical variables to numerical using one-hot encoding
# X = pd.get_dummies(X, columns=["category", "state_of_domicile", "preferred_branch"])

# # Split the data into training and testing sets
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# # Train a Random Forest Classifier
# model = RandomForestClassifier(n_estimators=100, random_state=42)
# model.fit(X_train, y_train)

# # Evaluate the model
# y_pred = model.predict(X_test)
# accuracy = accuracy_score(y_test, y_pred)
# print(f"Model Accuracy: {accuracy * 100:.2f}%")

# # Save the trained model
# joblib.dump(model, "college_predictor_model.pkl")

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib

# Load the synthetic dataset
df = pd.read_csv("college_admission_dataset.csv")

# Define features and target
X = df.drop("college_admitted", axis=1)  # Features
y = df["college_admitted"]  # Target

# Convert categorical variables to numerical using one-hot encoding
X = pd.get_dummies(X, columns=["category", "state_of_domicile", "preferred_branch"])

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a Random Forest Classifier
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Save the feature names to the model object
model.feature_names_in_ = X.columns.tolist()  

# Evaluate the model
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy * 100:.2f}%")

# Save the trained model
joblib.dump(model, "college_predictor_model.pkl")


