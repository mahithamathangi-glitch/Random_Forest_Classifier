import streamlit as st
import pandas as pd

from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

st.set_page_config(
    page_title="Random Forest Classifier",
    page_icon="🌳"
)

st.title("🌳 Random Forest Classifier")

st.write(
    "Breast Cancer Wisconsin Dataset Classification "
    "using Random Forest."
)

# Load dataset
data = load_breast_cancer()

X = pd.DataFrame(
    data.data,
    columns=data.feature_names
)

y = pd.Series(data.target)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

# Train model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

# Predictions
predictions = model.predict(X_test)

accuracy = accuracy_score(
    y_test,
    predictions
)

st.subheader("Model Performance")

st.metric(
    "Testing Accuracy",
    f"{accuracy:.2%}"
)

st.subheader("Model Information")

st.write("Algorithm: Random Forest Classifier")
st.write("Number of Trees: 100")
st.write("Dataset: Breast Cancer Wisconsin Dataset")
st.write("Number of Features:", X.shape[1])

st.success("Random Forest model trained successfully!")