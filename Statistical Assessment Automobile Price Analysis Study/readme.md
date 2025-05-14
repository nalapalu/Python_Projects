# **Statistical Assessment: Automobile Price Analysis Study**

## Objectives:
This project showcases my expertise in statistical analysis and machine learning using Python to examine sales trends for an automobile retailer. The primary goals include:  
- Identifying the key factors influencing car prices.  
- Forecasting future sales trends through time series analysis.  
- Assessing the statistical significance of differences between feature categories.  

## Data Overview:
The dataset consists of fictional automobile sales data, including:  
- Time series data on vehicle sales.  
- Specifications and features of various car types.  
- Monthly records of advertising expenditures, pricing, and units sold.  

## Methodology:  
- Developed relevant business questions to extract meaningful insights from the data.  
- Performed data loading, cleaning, and imputation of missing values, followed by exploratory data analysis (EDA).  
- Applied statistical tests (Chi-Square, ANOVA, Ordinary Least Squares) to identify features most relevant to determining car prices.  
- Constructed a Multiple Linear Regression model to predict car prices based on different attributes.  
- Conducted time series analysis using Exponential Smoothing and Seasonal ARIMA to forecast sales for the upcoming quarter.  

## Key Findings & Insights: 
1. **Price Determinants:** Strong correlations exist between vehicle horsepower, engine size, and price (correlation coefficients > 0.8). OLS regression analysis confirms that engine size significantly impacts pricing (**p-value < 0.05**).  
2. **Category Comparisons:** Significant price differences were observed across vehicle body types (**p-value < 0.05**), whereas fuel type variations showed no statistically significant price effects (**p-value > 0.05**).  
3. **Predictive Performance:** The Multiple Linear Regression model demonstrated robust predictive accuracy, achieving an R² value of approximately **0.83** on the test dataset.  
4. **Influential Features:** Among all numerical attributes, engine size, horsepower, curb weight, and car width emerged as the strongest predictors of price due to their high correlations.  
5. **Sales Forecast:** Using time series models, Q1 2025 sales were forecasted, projecting **577 units**.  

## Stakeholder Report: 
For a detailed breakdown of findings, methodology, and business implications, refer to the full project report:  

[Project Report for Stakeholders](https://github.com/nalapalu/Python_Projects/blob/main/Statistical%20Assessment%20Automobile%20Price%20Analysis%20Study/Report_of_Results_Chiran.pdf)  
