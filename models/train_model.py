import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report

# Load dataset
df = pd.read_csv("datasets/industrial_safety_dataset.csv")

# Encode categorical features
encoders = {}

categorical_columns = [
    "Maintenance",
    "Permit",
    "MachineStatus",
    "Zone"
]

for column in categorical_columns:
    encoder = LabelEncoder()
    df[column] = encoder.fit_transform(df[column])
    encoders[column] = encoder

# Encode target
risk_encoder = LabelEncoder()
df["Risk"] = risk_encoder.fit_transform(df["Risk"])

# Features
X = df.drop(columns=["Timestamp", "Risk"])

# Target
y = df["Risk"]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Train model
model = RandomForestClassifier(
    n_estimators=200,
    random_state=42
)

model.fit(X_train, y_train)

# Prediction
predictions = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, predictions)

print("\nModel Accuracy")

print(accuracy)

print("\nClassification Report")

print(classification_report(y_test, predictions))

# Save model
joblib.dump(model, "models/risk_model.pkl")

joblib.dump(encoders, "models/encoders.pkl")

joblib.dump(risk_encoder, "models/risk_encoder.pkl")

print("\nModel Saved Successfully")