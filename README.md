# Random Forest Classifier

## Project Overview

This project implements a Random Forest Classification model and compares its performance with a single Decision Tree classifier.

The project demonstrates the concept of ensemble learning and investigates whether combining multiple decision trees can improve classification performance and generalization.

---

## Objective

The main objectives of this project are:

- Build a Decision Tree classification model as a baseline.
- Build a Random Forest classification model.
- Compare the performance of both models.
- Experiment with different values of `n_estimators`.
- Analyse feature importance.
- Evaluate the models using classification metrics and confusion matrices.

---

## Dataset

The project uses the **Breast Cancer Wisconsin Dataset** available through Scikit-learn.

The dataset contains:

- 569 observations
- 30 numerical features
- 2 target classes

The classification task is to distinguish between malignant and benign tumors.

---

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Jupyter Notebook / Google Colab
- Streamlit
- Git and GitHub

---

## Machine Learning Workflow

The project follows these steps:

1. Load the dataset.
2. Explore the dataset.
3. Check for missing values.
4. Split the data into training and testing sets.
5. Train a Decision Tree classifier.
6. Evaluate the Decision Tree.
7. Train a Random Forest classifier.
8. Evaluate the Random Forest.
9. Compare both models.
10. Experiment with different numbers of trees.
11. Analyse feature importance.
12. Create a simple Streamlit application.

---

## Models

### Decision Tree

A single Decision Tree classifier is used as the baseline model.

### Random Forest

A Random Forest classifier is trained using multiple decision trees.

The initial Random Forest configuration uses:

```text
n_estimators = 100
random_state = 42

Performance Evaluation
The models are evaluated using:
Accuracy
Precision
Recall
F1 Score
Confusion Matrix
Training and testing accuracy are also compared to understand model generalization.
Experiment with n_estimators
Different numbers of trees are tested:
10
50
100
200
The resulting training and testing accuracy are compared to understand the effect of the number of trees on model performance.
Feature Importance
Random Forest feature importance is analysed using:
random_forest.feature_importances_
The top features are visualized using a bar chart.
Project Structure
Random-Forest-Classifier/
│
├── app.py
├── requirements.txt
├── Random_Forest_Classifier_Project.ipynb
├── README.md
├── rollback_evidence.md
│
└── images/
    ├── decision_tree_confusion_matrix.png
    ├── random_forest_confusion_matrix.png
    ├── model_performance_comparison.png
    ├── estimator_experiment.png
    └── feature_importance.png
Streamlit Application
A simple Streamlit application is included in app.py.
The application loads the Breast Cancer Wisconsin dataset, trains a Random Forest classifier and displays the testing accuracy and model information.
To run the application locally:
pip install -r requirements.txt
Then:
python -m streamlit run app.py
Results
The project compares the Decision Tree baseline with the Random Forest classifier using multiple evaluation metrics.
The experiment also demonstrates how changing the number of trees can affect training and testing performance.
The feature importance analysis provides insight into which input features contributed most strongly to the Random Forest model's predictions.
Conclusion
This project demonstrates the application of ensemble learning using Random Forest classification.
A single Decision Tree is used as a baseline and its performance is compared with a Random Forest consisting of multiple decision trees.
The experiment provides practical understanding of:
Ensemble learning
Random Forest classification
Model evaluation
Generalization
Hyperparameter experimentation
Feature importance