import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report
import joblib

# Load dataset
data = pd.read_csv(r"C:\Movies\Water Quality\water_potability.csv")

# Handle missing values
data['ph'].fillna(data['ph'].mean(), inplace=True)
data['Sulfate'].fillna(data['Sulfate'].mean(), inplace=True)
data['Trihalomethanes'].fillna(data['Trihalomethanes'].mean(), inplace=True)

# Separate features and target
X = data.drop('Potability', axis=1)
y = data['Potability']

# Scale features
scaler = StandardScaler()
X = scaler.fit_transform(X)

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# Evaluate model
y_pred = model.predict(X_test)
print(classification_report(y_test, y_pred))

# Save model
joblib.dump(model, 'water_quality_model.pkl')
joblib.dump(scaler, 'scaler.pkl')
