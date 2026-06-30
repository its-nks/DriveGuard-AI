Dataset 1 – OBD-II Vehicle Sensor Dataset

Important Observations
Original dataset contained 60,439 records × 33 columns.
Removed metadata columns (timestamp, vehicle ID, model, etc.) because they do not contribute to prediction.
Dropped columns having more than 60% missing values to improve data quality.
Final cleaned dataset contains 34,397 records × 18 features.
Missing values in remaining numerical columns were imputed using the median.
Percentage-based columns were converted into numeric values.
Categorical variables were label encoded.
No duplicate records remain after preprocessing.
Dataset contains real vehicle sensor readings, making it suitable for learning driving behaviour and engine health patterns.
Feature engineering was performed to generate domain-specific indicators:
Engine Stress Index
Thermal Stress
Driving Score
Air Flow Index
Engine Efficiency
IRSI (Integrated Risk Score Index)
Some engineered features (especially Engine Stress Index and Driving Score) show strong correlation with other variables. During model training, feature importance or dimensionality reduction may be considered if required.
Dataset has no target label, therefore it will mainly be used for feature enrichment and knowledge transfer while creating the final unified dataset.

Dataset 2 – AI4I Predictive Maintenance Dataset
Important Observations
Original dataset contains 10,000 records × 14 columns.
Removed identifier columns (UDI and Product ID) since they do not help prediction.
Encoded categorical feature (Type) into numerical format.
No missing values were present.
No duplicate records were found.
Additional engineered features were created:
Temperature Difference
Mechanical Stress
Wear Rate
Final dataset is fully numeric and ready for machine learning.
Machine Failure is the target variable.
Class Distribution
Normal Machines → 9,661 (96.61%)
Failed Machines → 339 (3.39%)
Important Note

The dataset is highly imbalanced.

This may bias machine learning models toward predicting normal operation. During model development, imbalance handling techniques such as:

SMOTE
Class Weights
Balanced Random Forest

may be applied to improve failure prediction.

Integration Notes:
Both datasets have been independently cleaned and standardized.
Feature names follow a consistent naming convention.
All features are numeric after preprocessing.
These datasets are intended to be merged with an additional driving/vehicle dataset to create a richer feature space for predictive maintenance.
Final dataset preparation and model training will be handled after dataset integration.