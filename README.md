# Bank-Account-Opening-Prediction
## Problem Statement
To predict which individuals are most likely to have or use a bank account based on demographic information and financial service usage data from approximately 33,600 individuals across East Africa.

### Objective
- Develop a Machine Learning model to predict which individuals are most likely to have or use a bank account.
- Evaluate the model's performance using relevant evaluation metrics

#### Data Features: country, year, uniqueid, location_type, cellphone_access, household_size, age_of_respondent,gender_of_respondent, relationship_with_head, marital_status, education_level, and job_type.

##### Correlation:
The correlation matrix of the African Financial Inclusion data shows that are mostly weak relationships between he variables indicating that there are no strong linear relationships between these variables except for country and year variables which are perfectly correlated with (1.000), suggesting that the data might be from a specific year for each country.

Weak Correlations
- education_level and bank_account (0.388): Individuals with higher education levels are more likely to have a bank account.
- job_type and country (0.451): Certain job types are more prevalent in specific countries.
- age_of_respondent and bank_account (0.110): Older individuals are slightly more likely to have a bank account.
- cellphone_access and bank_account (0.209): Individuals with access to a cellphone are more likely to have a bank account.
- education_level and age_of_respondent (0.190): Older individuals tend to have higher education levels.

Negative Correlations
- household_size and age_of_respondent (-0.107): Larger households tend to have younger individuals.

