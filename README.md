# Python Projects

Welcome to my Python Projects repository! This collection showcases various Python projects I've worked on to demonstrate my expertise in data analysis, database design, and query optimization. Each project addresses real-world problems and provides insightful solutions using Python.

## Table of Contents

- [Overview](#overview)
- [Projects](#projects)
  - [Predicting SpaceX Falcon 9 Launch Success](#predicting-spacex-falcon-9-launch-success)
  - [Statistical Assessment: Automobile Price Analysis Study](#statistical-assessment-automobile-price-analysis-study)
  - [Kaggle Titanic Survival Prediction Project](#kaggle-titanic-survival-prediction-project)
- [Technologies Used](#technologies-used)
- [Getting Started](#getting-started)
- [Contact](#contact)

---

## Overview

This repository features Python scripts, Jupyter Notebooks, and related files for portfolio projects I've completed. These projects span various industries and use cases, highlighting:
- The application of data science libraries, including Pandas, NumPy, SciPy, and Scikit-Learn.
- Advanced data visualization techniques.
- Processes such as data collection, wrangling, and exploratory data analysis (EDA).
- Machine learning and deep learning methodologies.

---

## Projects

### [**Predicting SpaceX Falcon 9 Launch Success**](https://github.com/nalapalu/Python_Projects/tree/main/Predicting-SpaceX-Falcon-9-Launch-Success)

#### Objectives:
- This capstone project applies the skills developed during the [IBM Data Science Professional Certificate program](https://www.coursera.org/account/accomplishments/professional-cert/URXA2M62VAPC) to a real-world problem: predicting the success of SpaceX Falcon 9 rocket launches.
- Utilize historical launch data from diverse sources to create a machine learning model that estimates the probability of success for future launches.

#### Data Overview:
- The dataset contains mission information for SpaceX rocket launches and was compiled using:
  - The SpaceX API
  - Web scraping from Wikipedia with BeautifulSoup.

#### Methodology:
- Demonstrated data extraction via an API and web scraping techniques.
- Focused on cleaning, handling missing values, and transforming data for analysis.
- Conducted EDA to understand the dataset and explore relationships between features and the target variable. Visualizations were created using Matplotlib and Seaborn.
- Developed machine learning models for prediction using Scikit-Learn, Pandas, and NumPy.

#### Key Findings & Insights: 
- Achieved 87.7% accuracy with a logistic regression model.
- KSC (Kennedy Space Center) launch site had the highest success rates, likely due to stable environmental conditions.
- Success rates improved over time as providers refined their procedures.
- Payloads exceeding 6,000 kg were less successful, possibly due to increased difficulty and susceptibility to weather conditions.

[Project Presentaion for Stakeholders](https://github.com/nalapalu/Python_Projects/blob/main/Predicting-SpaceX-Falcon-9-Launch-Success/Final_assignment.pdf)

---

## [**Statistical Assessment: Automobile Price Analysis Study**](https://github.com/nalapalu/Python_Projects/tree/main/Statistical%20Assessment%20Automobile%20Price%20Analysis%20Study)  

### Objectives:
This project showcases my expertise in statistical analysis and machine learning using Python to examine sales trends for an automobile retailer. The primary goals include:  
- Identifying the key factors influencing car prices.  
- Forecasting future sales trends through time series analysis.  
- Assessing the statistical significance of differences between feature categories.  

### Data Overview:
The dataset consists of fictional automobile sales data, including:  
- Time series data on vehicle sales.  
- Specifications and features of various car types.  
- Monthly records of advertising expenditures, pricing, and units sold.  

### Methodology:  
- Developed relevant business questions to extract meaningful insights from the data.  
- Performed data loading, cleaning, and imputation of missing values, followed by exploratory data analysis (EDA).  
- Applied statistical tests (Chi-Square, ANOVA, Ordinary Least Squares) to identify features most relevant to determining car prices.  
- Constructed a Multiple Linear Regression model to predict car prices based on different attributes.  
- Conducted time series analysis using Exponential Smoothing and Seasonal ARIMA to forecast sales for the upcoming quarter.  

### Key Findings & Insights: 
1. **Price Determinants:** Strong correlations exist between vehicle horsepower, engine size, and price (correlation coefficients > 0.8). OLS regression analysis confirms that engine size significantly impacts pricing (**p-value < 0.05**).  
2. **Category Comparisons:** Significant price differences were observed across vehicle body types (**p-value < 0.05**), whereas fuel type variations showed no statistically significant price effects (**p-value > 0.05**).  
3. **Predictive Performance:** The Multiple Linear Regression model demonstrated robust predictive accuracy, achieving an R² value of approximately **0.83** on the test dataset.  
4. **Influential Features:** Among all numerical attributes, engine size, horsepower, curb weight, and car width emerged as the strongest predictors of price due to their high correlations.  
5. **Sales Forecast:** Using time series models, Q1 2025 sales were forecasted, projecting **577 units**.  

### Stakeholder Report: 
For a detailed breakdown of findings, methodology, and business implications, refer to the full project report:  

[Project Report for Stakeholders](https://github.com/nalapalu/Python_Projects/blob/main/Statistical%20Assessment%20Automobile%20Price%20Analysis%20Study/Report_of_Results_Chiran.pdf)  

--- 

### [**Kaggle Titanic Survival Prediction Project**](https://github.com/nalapalu/Python_Projects/tree/main/Kaggle_Titanic_Survival_Prediction_Project)

#### Objectives:
- This project predicts Titanic passenger survival using features like age, gender, ticket class, and more. The workflow includes:
  - Data loading and exploration.
  - Data cleaning and preprocessing.
  - Feature engineering.
  - Model training and evaluation.
  - Hyperparameter tuning and generating predictions.

#### Data Overview:
- The dataset was sourced from the Kaggle competition, [Titanic - Machine Learning from Disaster](https://www.kaggle.com/competitions/titanic/data).
- It contains training and test datasets with passenger details such as name, age, gender, socio-economic class, etc.
- The test dataset omits the survival column, which serves as the prediction target.

#### Methodology:
- Conducted data exploration, cleaning, and preprocessing.
- Implemented feature engineering techniques.
- Trained and evaluated machine learning models.
- Performed hyperparameter tuning to improve model performance.
- Generated predictions based on the trained model.

#### Key Findings & Insights: 
- The SVM model achieved the highest accuracy, at 77.9%.
- Grid search cross-validation enhanced the performance of the SVM model.

---

## Technologies Used

- **Programming Languages:** Python, SQL
- **Data Science Libraries:** Pandas, NumPy, Scikit-Learn, Matplotlib, Seaborn, Missingno, CatBoost, Joblib
- **Machine Learning Algorithms:** Linear Regression, Logistic Regression, Decision Trees, Random Forest, Support Vector Machines, K-Nearest Neighbors, Gradient Boosting Machines.
- **Environment:** Jupyter Notebooks

---

## Getting Started

1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/nalapalu/Python_Projects
   ```

2. Navigate through the project folders to explore the associated files, scripts, and documentation.

---

## Contact

If you have questions, feedback, or opportunities you'd like to discuss, feel free to reach out:

- **Email:** [chiran.nalapalu@gmail.com](mailto:chiran.nalapalu@gmail.com)
- **LinkedIn:** [nalapalu](https://www.linkedin.com/in/nalapalu/)  

Let's connect!

---

Thank you for reviewing my Python portfolio! I hope these projects showcase my skills and enthusiasm for working with data.

---
