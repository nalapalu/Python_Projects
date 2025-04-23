## Kaggle Titanic Survival Prediction Project

This project uses machine learning to predict passenger survival from the Titanic disaster based on the famous Kaggle Titanic dataset.

## Project Overview

The Titanic survival prediction model uses passenger information such as age, sex, ticket class, and other features to predict whether a passenger survived the disaster. The project follows a standard machine learning workflow:

1. Data loading and exploration
2. Data cleaning and preprocessing
3. Feature engineering
4. Model training and evaluation
5. Hyperparameter tuning
6. Prediction generation

## Project Structure

```
.
├── data
│   ├── raw             # Original datasets
│   ├── interim         # Intermediary processed data
│   └── processed       # Final processed datasets
├── models              # Trained models
├── src                 # Source code
│   ├── data            # Scripts for data processing
│   ├── features        # Scripts for feature engineering
│   ├── models          # Scripts for model training and prediction
│   └── visualization   # Scripts for visualization
└── README.md
```

## Data Processing

The data processing workflow includes:

- Loading train and test datasets
- Exploring data characteristics and missing values
- Extracting titles from passenger names
- Handling missing values:
  - Age: filled with median values grouped by Sex, Pclass, and Title
  - Cabin: filled with 'U' for unknown and mapped to first letter
  - Embarked: filled with most common value
  - Fare: filled with median value
- Creating family size feature
- Converting categorical values to numerical representations
- Removing unnecessary features

## Feature Engineering

The following features were created or processed:
- Title extraction from Name
- Title normalization (mapping various titles to standard categories)
- Family size calculation
- Categorical encoding for Sex, Cabin, Embarked, and Title

## Model Training

Multiple classification algorithms were tested:
- Random Forest
- Logistic Regression
- Support Vector Machines (SVM)
- K-Nearest Neighbors
- Gaussian Naive Bayes
- Perceptron
- Linear SVM
- Stochastic Gradient Descent
- Decision Tree
- CatBoost

SVM was selected as the best performing model after evaluation.

## Hyperparameter Tuning

Grid search cross-validation was performed on the SVM model with the following parameters:
- C: [0.1, 1, 10, 100]
- gamma: [0.1, 0.01, 0.001, 0.0001]
- kernel: ['linear', 'rbf']

## Results

The model was evaluated using accuracy score and cross-validation. Final predictions were generated for the test dataset and exported for submission.

## Requirements

The project requires the following Python libraries:
- pandas
- numpy
- scikit-learn
- matplotlib
- seaborn
- missingno
- catboost
- joblib

## Usage

To run the prediction pipeline:

1. Place raw data files in `data/raw/`
2. Run data cleaning script
3. Run feature engineering script
4. Run model training script
5. Run prediction script to generate submission file

## Future Improvements

Potential areas for improvement:
- Ensemble modeling
- More advanced feature engineering
- Neural network approaches
- Feature importance analysis
