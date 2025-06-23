import pandas as pd

# Load the uploaded dataset
file_path = "data.csv"
df = pd.read_csv(file_path)

# Display basic information and first few rows
df.info()

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

# Drop the 'id' column
df = df.drop(columns=["id"])

# Encode the 'diagnosis' column: M -> 1, B -> 0
label_encoder = LabelEncoder()
df["diagnosis"] = label_encoder.fit_transform(df["diagnosis"])

# Separate features and target
X = df.drop(columns=["diagnosis"])
y = df["diagnosis"]

# Split data into train (80%) and test (20%)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

X_train.shape, X_test.shape, y_train.shape, y_test.shape

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, f1_score

# Train a Random Forest Classifier
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# Predict on test set
y_pred = model.predict(X_test)

# Evaluate performance
accuracy = accuracy_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)

print(f"Accuracy: {accuracy:.4f}")
print(f"F1 Score: {f1:.4f}")    

