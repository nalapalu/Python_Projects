import sys

import pandas as pd
from sklearn.calibration import LinearSVC
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import AdaBoostClassifier, RandomForestClassifier
from sklearn.model_selection import GridSearchCV, train_test_split, StratifiedKFold
from catboost import CatBoostClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression, Perceptron, SGDClassifier
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import cross_val_score

import joblib
from sklearn.metrics import (
    f1_score,
    accuracy_score,
    confusion_matrix,
    classification_report,
    log_loss,
    roc_auc_score,
    roc_curve,
    precision_score,
    recall_score,
    RocCurveDisplay,
    ConfusionMatrixDisplay
)
from sklearn.tree import DecisionTreeClassifier



sys.path.append("..")

# --------------------------------------------------------------
# Load data
# --------------------------------------------------------------

train = pd.read_csv("../../data/processed/train.csv")
train = train.drop(train.columns[0], axis=1)

target = "Survived"

# --------------------------------------------------------------
# Train test split
# --------------------------------------------------------------

X = train.drop([target], axis=1)
y = train[target]

X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.8)

# --------------------------------------------------------------
# Train model
# --------------------------------------------------------------

# Define preprocessing for numeric columns (scale them)
numeric_features = X.select_dtypes(include=["float64", "int64"]).columns
numeric_transformer = Pipeline(steps=[("scaler", StandardScaler())])

# Define preprocessing for categorical features (encode them)
categorical_features = X.select_dtypes(include=["category"]).columns
categorical_transformer = Pipeline(
    steps=[("onehot", OneHotEncoder(handle_unknown="ignore"))]
)

# Combine preprocessing steps
preprocessor = ColumnTransformer(
    transformers=[
        ("num", numeric_transformer, numeric_features),
        ("cat", categorical_transformer, categorical_features),
    ]
)


# --------------------------------------------------------------
# Testing different models
# --------------------------------------------------------------

classifiers = [
    RandomForestClassifier(),
    LogisticRegression(),
    SVC(),
    KNeighborsClassifier(),
    GaussianNB(),
    Perceptron(),
    LinearSVC(),
    SGDClassifier(),
    DecisionTreeClassifier(),
    CatBoostClassifier()
]

accuracy_scores = []
cv_scores = [] 
for classifier in classifiers:
    # Build the pipeline for the current classifier
    pipeline = Pipeline(
        steps=[("preprocessor", preprocessor), ("classifier", classifier)]
    )

    # Fit the pipeline to train the model on the training set
    model = pipeline.fit(X_train, y_train)

    # Evaluate the model
    # Get predictions
    predictions = model.predict(X_test)

    # Display metrics
    accuracy = accuracy_score(y_test, predictions)
    accuracy_scores.append((classifier.__class__.__name__, accuracy))
    
    # Compute cross-validation scores
    scores = cross_val_score(pipeline, X_train, y_train, cv=5)
    cv_scores.append((classifier.__class__.__name__, scores.mean()))

train_accuracy = pd.DataFrame(accuracy_scores, columns=['Classifier', 'Accuracy'])
train_CVscore = pd.DataFrame(cv_scores, columns=['Classifier', 'CV_score'])

train_accuracy.sort_values(by = 'Accuracy', ascending = False, ignore_index = True)
train_CVscore.sort_values(by = 'CV_score', ascending = False, ignore_index = True)

# --------------------------------------------------------------
# Testing best models
# --------------------------------------------------------------

# Build the pipeline
pipeline = Pipeline(
    steps=[("preprocessor", preprocessor), ("classifier", SVC())]
)

# fit the pipeline to train the model on the training set
model = pipeline.fit(X_train, y_train)

# --------------------------------------------------------------
# Evaluate the model 
# --------------------------------------------------------------

# Get predictions
predictions = model.predict(X_test)

# Display metrics
accuracy = accuracy_score(y_test, predictions)
print("Accuracy:", accuracy)

# --------------------------------------------------------------
# Hyper parameter tuning
# --------------------------------------------------------------

param_grid = {
    'classifier__C': [0.1, 1, 10, 100],  # Penalty parameter C of the error term
    'classifier__gamma': [0.1, 0.01, 0.001, 0.0001],  # Kernel coefficient for 'rbf'
    'classifier__kernel': ['linear', 'rbf']  # Kernel type
}

# Create GridSearchCV instance
grid_search = GridSearchCV(pipeline, param_grid, cv=5, scoring='accuracy')

# Fit the GridSearchCV instance to perform hyperparameter tuning
grid_search.fit(X_train, y_train)

# Get the best parameters and best estimator from the GridSearchCV
best_params = grid_search.best_params_
best_estimator = grid_search.best_estimator_

# Fit the best estimator on the training data
best_estimator.fit(X_train, y_train)

# Predictions using the best estimator
predictions = best_estimator.predict(X_test)

# Display metrics
accuracy = accuracy_score(y_test, predictions)
print("Accuracy:", accuracy)
print("Best Parameters:", best_params)


# --------------------------------------------------------------
# Export model
# --------------------------------------------------------------

ref_cols = list(X.columns)

joblib.dump(value=[best_estimator, ref_cols, target], filename="../../models/model.pkl")
