# **Hypothesis Testing with Men and Women Soccer Matches**

## Objectives:
- Perform an appropriate hypothesis test to determine the p-value, and hence result, of whether to reject or fail to reject the null hypothesis that the mean number of goals scored in women's international soccer matches is the same as men's using a 10% significance level.

## Data Overview:
- The two datasets contain the results of every official men's and women's international football match since the 19th century
- This data is stored in two CSV files: `women_results.csv` and `men_results.csv`.

## Methodology:
- Perform Exploratory analysis
- Filtering data
- Choosing Correct Hypothesis test
- Running test
- Interpret results

## Key Findings & Insights: 
- Goals scored is not normally distributed, so use perform right-tailed Wilcoxon-Mann-Whitney test with scipy
- Mean Womens teams Goal: 2.98. Mean Mean's Team goal 2.513
- p-value less than 0.01. Can reject Null hypothesis.  

