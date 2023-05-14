![image](https://github.com/GunduSriBhanu/SriBhanu_DATA606/assets/112648901/5023e3a0-b7d7-4a66-8a19-38bfe41c57fe)

### Presentation PPT Link:

https://github.com/DATA-606-SPRING-2023-TUE/SriBhanu_DATA606/blob/main/docs/capstone.pptx

### YouTube Link:

https://www.youtube.com/watch?v=JhPwiieBoZ4

# Heart Disease Prediction
![image](https://github.com/GunduSriBhanu/SriBhanu_DATA606/blob/main/docs/images/Data_Life_Cycle.png)

### Understanding the Business Problem:
Cardiovascular diseases, which include conditions like coronary artery disease, heart failure, and stroke, are a major cause of death globally, with over 17 million deaths annually. Treatment for Cardio Vascular Diseases depends on the specific condition and other factors. Prevention is crucial, and can be achieved through managing risk factors like high blood pressure, high cholesterol, and fasting blood sugar, and early detection for prompt treatment. Working with healthcare providers to develop personalized prevention and management plans is important for reducing the risk of developing these disease especially heart failure or heart diseases. These diseases killing more than 17 million people globally every year. This projects helps to predict the patients with heart failures.

### Preparing the Data:
The dataset is taken from the UCI website "https://archive.ics.uci.edu/ml/datasets/Heart+Disease" of three databases with datasets of Cleaveland, Hungarian and Switzerland are taken. There are 14 features in all the datasets. There are 303 entries in cleaveland dataset, 294 entries in Hungarian dataset and 123 entries in Switzerland dataset. These three datasets are with different datatypes and data types are changed as per the analysis from all the three datasets and unified. These unified datasets after merging will be processed for model fitting in the further analysis, visualization and model fitting.

Raw encoded data is retrieved from a website in the form of ".data". The data is then converted to semi-structured format and analyzed. Column labels are assigned based on information provided on the UCI website. Data from three different countries, each with varying data types, are combined. Special characters are replaced with null values and handled based on the target variable. Finally, all datasets are merged and prepared for further analysis.

**File:** "Data_Preparation.ipynb"

### Exploratory Data Analysis and Data Visualization:
The data has both categorical and numerical data types. Categorical data types include sex, chest_pain_type, ekg_results, exercise_angina, slope_of_st, thallium, and heart_disease. Numerical data types include age, resting blood pressure, cholestoral, fasting_blood_sugar, max_hr, ST_depression, and vessels. The categorical data types consist of information that can be grouped into different categories, while the numerical data types consist of quantitative data that can be measured and analyzed. It is important to identify the type of data in order to choose the appropriate statistical methods for analysis and interpretation.

**Features of Data:**
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
The effect of cholesterol and blood sugar levels has the major impact on the heart_disease especially on different ages of people. The chest pain type and max heart rate can analyze the impact of heart disease.

The data shows that most of the patients are in the age range of 50 to 60 years, and there are more male patients (625) than female patients (274). Asymptomatic BP is the most common chest pain type among the patients, with a count of 411. Resting blood pressure is uniformly distributed among the patients, with the majority falling between 120 to 140. Cholesterol levels are also uniformly distributed, with the highest count between 200 to 300. Most of the patients (789) in the data are suffering from fasting blood sugar. Ekg_results show that the majority of the patients have normal results. Maximum heart rate is between 125 to 175 for most of the patients in the data, and exercise-induced angina has a count of 612 among the patients. ST_depression is highest in number between the range of 0 to 2. Upsloping in slope_of_st is the most common with a count of 485 in the data, while downsloping has the lowest count of 43. The majority of the patients had vessels of 0 with a count of 653. The patients in the data had mostly normal thallium results, with a count of 608. Lastly, the data provides more instances of absence of heart disease, with a count of 515

**Correlation between numerical variables:**

![image](https://github.com/GunduSriBhanu/SriBhanu_DATA606/blob/main/docs/images/606_Correlation.png)

**Outliers and skewness detection**

![image](https://github.com/GunduSriBhanu/SriBhanu_DATA606/blob/main/docs/images/606_outlier.png)

Dataset is small and hence outliers and highle correlated data cannot be removed, because these features are important for the prediction of heart disease.

The majority of patients in the dataset fall between the ages of 50 and 60. Male patients outnumber female patients with a count of 625 and 274, respectively. The most common type of chest pain reported is Asymptomatic BP, with 411 occurrences, followed by other pain types. Resting blood pressure appears to be uniformly distributed, with a concentration of patients falling within the range of 120 to 140. Cholesterol levels are also uniformly distributed, with the highest count between 200 and 300. A large majority of patients, with a count of 789, are suffering from fasting blood sugar. Most patients have normal EKG results and a maximum heart rate between 125 and 175. Exercise-induced angina is reported by 612 patients. ST depression is more frequently observed within the range of 0 to 2. Upsloping is the most commonly observed slope of ST with a count of 485, while downsloping is the least common with a count of 43. The majority of patients had zero vessels, with a count of 653. Normal thallium appears most frequently with a count of 608. The dataset contains more instances of the absence of heart disease, with a count of 515.

From the data of heart failures presence, Females had more in number of cases with cholosterol, maximum heart rate and resting blood pressure in comparison to males with fasting blood sugar presence.

![image](https://github.com/GunduSriBhanu/SriBhanu_DATA606/blob/main/docs/images/606_gender_fbp_chol_maxhr_rbp_hf.png)

Patient with cholesterol of 83.78% had the presence of blood sugar, which is the highest percentage. So, the patients with blood sugar had high chances of cholosterol problems.

![image](https://github.com/GunduSriBhanu/SriBhanu_DATA606/blob/main/docs/images/606_blood_sugar_cholosterol.png)

From the data, both in the males and females between age 50 and 60 is more provided and among them in the age of 50 to 60, there are many patients.

![image](https://github.com/GunduSriBhanu/SriBhanu_DATA606/blob/main/docs/images/606_age_gender_distribution.png)

From overall analysis of EDA and visualization, based on the data of patients with both heart disease present and absence, it was found that most of the patients were between the ages of 50 to 60. The dataset showed that there were more males than females, and most of the patients had Asymptomatic chest pain type with resting blood pressure between 120 to 140. Fasting blood sugar presence was found to be highest in the data and most of the ekg_results were normal. ST_depression was mostly in the range of 0 to 2, and Upsloping was the most common slope_of_st. The thallium count was found to be 608 with Normal results. Additionally, it was observed that for patients with heart disease present and cholesterol presence, most of the patients were also between the ages of 50 to 60 with Asymptomatic chest pain type and resting blood pressure between 120 to 140. The dataset showed that there were more males than females, and fasting blood sugar presence was highest. Most of the ekg_results were normal and ST_depression was mostly in the range of 0 to 2, with Downsloping being the most common slope_of_st. The thallium count was found to be 159 with Reversible defects.

**File:** "Eda_Heart_Failure.ipynb"

### Modeling the data:

After performing exploratory data analysis (EDA), the dataset was loaded to predict the heart disease variable. The class distribution is imbalanced, indicating that there are more samples for one class than the other. Furthermore, there appear to be issues with bias and variance in this dataset, suggesting that using metrics like recall may be more appropriate for modeling than accuracy.

**Feature Processing:**

The missing data in the dataset was filled using mean imputation and then the data was standardized. For categorical data, missing values were filled with the most frequent values and then binary one hot encoding was applied for encoding. The transformed data was passed through a pipeline to ensure that the shape of the data was retained. After applying fit transform to the numerical columns, there were 8 columns and for categorical columns, there were 22 columns. Finally, the transformed data had 28 columns without any data loss.

**Classification models:**

Heart disease diagnosis in patients can be done using regression and classification models. However, when fitting models such as logistic regression, random forest and decision trees, issues like overfitting, multicollinearity, skewness and outliers in the data were encountered. Decision trees showed severe overfitting, with a large difference in training and testing performance metrics.  

**Comparison of models with accuracy**

![image](https://github.com/GunduSriBhanu/SriBhanu_DATA606/blob/main/docs/images/606_Accarcy_compare_models.png)

**After hyperparameter tuning:**

To solve these problems, hyperparameter tuning with grid search CV was performed, resulting in improved performance metrics like accuracy, recall and precision. The best model parameters were then used for cross-validation with 6 folds to determine the best performance.

**Comparing models after hyper tuning parameters with best scores**

![image](https://github.com/GunduSriBhanu/SriBhanu_DATA606/blob/main/docs/images/606_ROC_AUC_CV.png)

**Voting Classifiers:**

From the ROC curves of validation metrics for ensembles of voting classifiers, the Random Forest model outperformed voting classifier, decision trees and logistic regression, making it the better model for predicting heart disease diagnosis. 

**Comparing models of ensembles, voting classifiers with best scores**

![image](https://github.com/GunduSriBhanu/SriBhanu_DATA606/blob/main/docs/images/606_VOT_CLF.png)

### Evaluating the model:

After evaluating the validation metrics using ROC curves, Accuracy, Recall and precision, it can be observed that the Random Forest model has a slightly higher performance compared to the decision tree and logistic regression models. Therefore, the Random Forest model is considered to be the preferred model for heart failure prediction.

**File:** "UCI_Heart_Disease_Prediction_Modeling.ipynb"

### Deploying the model:

Streamlit web deployment involves creating a web-based application for predicting heart failure using the Streamlit library. The process starts with developing a heart failure prediction model using machine learning algorithms and training it on a dataset. The next step involves integrating the model with a Streamlit application to create an interactive interface that allows users to input their health data for predicting the likelihood of heart failure. The application can also provide visualizations and insights into the data to help users understand the results more easily.

**File:**  streamlit_heart_disease_predict.py

**Local URL:** http://localhost:8501

**Network URL:** http://192.168.1.154:8501

**Heart Disease Absent:**

![image](https://github.com/DATA-606-SPRING-2023-TUE/SriBhanu_DATA606/assets/112648901/54f68846-5534-457c-a3af-b765d988105c)

**Heart Disease Presence:**

![image](https://github.com/DATA-606-SPRING-2023-TUE/SriBhanu_DATA606/assets/112648901/1e6c705f-a6ac-44d3-8cfd-0223e2b3b227)

### Conclusion:
Based on the overall data analysis, it can be observed that heart diseases are more common in males over the age of 50 with high cholesterol levels (>200 mg), fasting blood sugar presence, asymptomatic blood pressure, and ST_depression between 0 to 2. Therefore, patients with these parameters should take extra care to prevent heart diseases. Random Forest algorithm was used to predict the presence of heart diseases. The developed heart failure prediction model has demonstrated its potential to predict the likelihood of heart failure in patients based on their medical history and other factors. It can be a useful tool for healthcare professionals to identify high-risk patients and provide them with appropriate treatments and preventive measures. However, the accuracy and reliability of the model depend on the quality and completeness of the data used to train it. Further research is required to validate its performance on larger and more diverse datasets. The model has been implemented as a web application using Streamlit.

### References:

http://www.lnit.org/uploadfile/2015/0115/20150115023938381.pdf

https://www.tctmd.com/news/artificial-intelligence-ecgs-may-id-asymptomatic-lv-dysfunction

https://www.alibabacloud.com/blog/predicting-heart-diseases-with-machine-learning_218458
