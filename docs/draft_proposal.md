# Draft Proposal for the project

## Project on Health Care Domain "Heart Disease Prediction"

### Problem Statement
The project primarily focused on the health care domain of prediction and detection of health issues especially issues of heart failure. One of the main issues of world in health domain are cardiovascular diseases. These diseases killing more than 17 million people globally every year. This projects helps to predict the patients with heart failures. This helps in avoiding and predicting the health issues in the primary stage. 

### Dataset Description:
The dataset is taken from the UCI website "https://archive.ics.uci.edu/ml/datasets/Heart+Disease" of three databases with datasets of Cleaveland, Hungarian and Switzerland are taken. There are 14 features in all the datasets. There are 303 entries in cleaveland dataset, 294 entries in Hungarian dataset and 123 entries in Switzerland dataset. These three datasets are with different datatypes and data types are changed as per the analysis from all the three datasets and unified. These unified datasets after merging will be processed for model fitting in the further analysis, visualization and model fitting.

### Features of Data:
* age  - In years
* sex - (1 = male; 0 = female)
* chest_pain_type - Value 1: typical angina -- Value 2: atypical angina -- Value 3: non-anginal pain -- Value 4: asymptomatic bp
* resting blood pressure (in mm Hg on admission to the hospital)
* cholesterol - serum cholestoral in mg/dl
* fbs_over_120 - (fasting blood sugar > 120 mg/dl) (1 = true; 0 = false)
* ekg_results - resting electrocardiographic results -- Value 0: normal -- Value 1: having ST-T wave abnormality (T wave inversions and/or ST elevation or depression of > 0.05 mV) -- Value 2: showing probable or definite left ventricular hypertrophy
* max_hr - maximum heart rate achieved
* exercise_angina - exercise induced angina (1 = yes; 0 = no)
* st_depression - ST depression induced by exercise relative to rest
* slope_of_st - the slope of the peak exercise ST segment -- Value 1: upsloping -- Value 2: flat -- Value 3: downsloping
* thallium - 3 = normal; 6 = fixed defect; 7 = reversable defect
* vessels - number of vessels fluoroscopy 
* heart_disease - Value 0: < 50% diameter narrowing -- Value 1: > 50%

Among these features, heart_disease attribute comprised of 5 different values, in which '0' indicates 'no heart disease' and '>1' indicates 'heart disease'. So, all the values are categorized to binary class of 0 (Absence) and 1 (Presence). This target variable of binary class will be processed for model fitting to predict the failure of heart.

### Models:
I am planning to use machine learning models of Regression and classification models. The machine learning models include the Logistic regression model and would like to deploy the models of Decision trees, KNeighbours classifiers and to some extent ANN network, and would like to improve the scores with tuning and other optimization techniques. The target variable choosen for the model is "heart_disease".

### Outcome:
These predictive in avoiding and resolution of health issues especially related to heart, which are more prevelant problems. Even, these problems are analyzed and predicted in the patients based on the age, blood sugar level, depression and cholesterol. These analysis will help in the early prediction and resolution of the disease. 


