import numpy as np
from tensorflow.keras.models import load_model
from sklearn.preprocessing import StandardScaler

# Load the model
model = load_model("model.h5")

# Example input (11 features)
# Replace this with actual user data as needed
sample = np.array([[600, 1, 0, 40, 3, 60000.0, 2, 1, 1, 50000.0, 1]])

# Scaling (note: use same scaler as during training for actual production)
scaler = StandardScaler()
sample_scaled = scaler.fit_transform(sample)

# Predict
prediction = model.predict(sample_scaled)
print("Churn Prediction:", "Yes" if prediction[0][0] > 0.5 else "No")
