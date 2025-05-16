# Customer Churn Prediction using ANN

This project uses an Artificial Neural Network (ANN) to predict customer churn based on bank data.

## 📁 Dataset
- **Source:** Provided CSV file (`Churn_Modelling.csv`)
- **Target column:** `Exited` (1 = churned, 0 = stayed)

## ⚙️ Model Architecture
- Input Layer: 11 features
- Hidden Layers: 2 layers with 16 neurons each (ReLU)
- Output Layer: 1 neuron (Sigmoid for binary classification)

# Evaluation
Model is evaluated using:
- Accuracy
- Confusion Matrix
- Classification Report

# Usage

```bash
# Install dependencies
pip install -r requirements.txt

# Run notebook
jupyter notebook main.ipynb
```

## Files Included
- `main.ipynb`: Training and evaluating the ANN
- `requirements.txt`: Required libraries
- `test.py`: Predict sample input
- `config.py`: Configuration (paths, hyperparameters)
- `README.md`: Project summary
