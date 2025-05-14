# **Data-Driven Decisions with A/B Testing**

## Objectives:
- Act as a data scientist at an online travel agency (OTA) testing a new search ranking system aimed at improving conversion. Using Python, you will analyze the A/B test results and decide whether the new system should be rolled out.
- Analyze and interpret the results to determine whether the new ranking system delivers a statistically significant improvement and provide a clear, data-driven recommendation.

#### Data Overview:
- A/B test datasets with session-level booking data ("sessions_data.csv") and user-level control/variant split ("users_data.csv").

## Methodology:
- Load and Join data
- Estimate effect size
- Compute primary metric
- Determine Sample Ratio Mismatch
- Conduct effect analysis on the Primay metric and then on the Guardrail metric
- make decision

## Key Findings & Insights: 
- Primary metric was be statistically significant and showed positive effect, indicating successful experiment with a sigificant postive conversion rate
- Guardrail was either be statistically insignificant and showed positive effect indicating guardrail metric was not harmed.  

