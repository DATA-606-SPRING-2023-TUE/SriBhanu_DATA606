# Loading Libraries
import streamlit as st
import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud, STOPWORDS
import streamlit.components.v1 as components
from pandas_profiling import ProfileReport
from PIL import Image
from sklearn.model_selection import train_test_split#, cross_validate
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
import numpy as np
import pandas as pd
import streamlit as st
import requests


#Choice of menu
menu = ["Home", "About", "Prediction"]
# Selection Box
choice = st.sidebar.selectbox("Menu",menu)
if choice =="About":
    def add_bg_from_url():
      st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("https://media.istockphoto.com/id/1163285589/vector/abstract-medical-background-with-flat-icons-and-symbols-template-design-with-concept-and.jpg?s=612x612&w=0&k=20&c=q9PFxIxWe-lasksFZ56obgC2gdZqzME6MkrdkfoW07A=");
            background-attachment: fixed;
            background-size: cover
        }}
        </style>
        """,
        unsafe_allow_html=True
      )
    add_bg_from_url() 
    st.subheader("Data Description")
    st.write('The dataset is taken from the UCI website "https://archive.ics.uci.edu/ml/datasets/Heart+Disease" of three databases with datasets of Cleaveland, Hungarian and Switzerland are taken. There are 14 features in all the datasets. There are 303 entries in cleaveland dataset, 294 entries in Hungarian dataset and 123 entries in Switzerland dataset. These three datasets are with different datatypes and data types are changed as per the analysis from all the three datasets and unified. These unified datasets after merging will be processed for model fitting in the further analysis, visualization and model fitting.')
    df = pd.read_csv('https://raw.githubusercontent.com/GunduSriBhanu/SriBhanu_DATA606/main/data/uci_heart_data.csv',sep = ',')
    st.dataframe(df)
    st.write("age - In years")
    st.write("sex - (1 = male; 0 = female)")
    st.write("chest_pain_type - Value 1: typical angina -- Value 2: atypical angina -- Value 3: non-anginal pain -- Value 4: asymptomatic bp")
    st.write("resting blood pressure (in mm Hg on admission to the hospital)")
    st.write("cholesterol - serum cholestoral in mg/dl")
    st.write("fbs_over_120 - (fasting blood sugar > 120 mg/dl) (1 = true; 0 = false)")
    st.write("ekg_results - resting electrocardiographic results -- Value 0: normal -- Value 1: having ST-T wave abnormality (T wave inversions and/or ST elevation or depression of > 0.05 mV) -- Value 2: showing probable or definite left ventricular hypertrophy")
    st.write("max_hr - maximum heart rate achieved")
    st.write("exercise_angina - exercise induced angina (1 = yes; 0 = no)")
    st.write("st_depression - ST depression induced by exercise relative to rest")
    st.write("slope_of_st - the slope of the peak exercise ST segment -- Value 1: upsloping -- Value 2: flat -- Value 3: downsloping")
    st.write("thallium - 3 = normal; 6 = fixed defect; 7 = reversable defect")
    st.write("vessels - number of vessels fluoroscopy")
    st.write("heart_disease - Value 0: < 50% diameter narrowing -- Value 1: > 50%')")



elif choice == "Prediction":
   def add_bg_from_url():
     st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("https://media.istockphoto.com/id/1163285589/vector/abstract-medical-background-with-flat-icons-and-symbols-template-design-with-concept-and.jpg?s=612x612&w=0&k=20&c=q9PFxIxWe-lasksFZ56obgC2gdZqzME6MkrdkfoW07A=");
            background-attachment: fixed;
            background-size: cover
        }}
        </style>
        """,
        unsafe_allow_html=True
     )
   add_bg_from_url() 
   
   # Load the heart data CSV file
   df = pd.read_csv('https://raw.githubusercontent.com/GunduSriBhanu/SriBhanu_DATA606/main/data/uci_heart_data.csv')
   df['heart_disease'] = df['heart_disease'].replace({'0':'Absence', '1' : 'Presence', '2' : 'Presence', '3' : 'Presence', '4' : 'Presence'})
   df=df.rename(columns={'resting blood pressure': 'resting_blood_pressure'})
   df=df.drop(columns=['Unnamed: 0'])
   
   # Define the feature and target columns
   features = ['age','sex','chest_pain_type','resting_blood_pressure','cholestoral','fasting_blood_sugar','ekg_results','max_hr','exercise_angina','ST_depression','slope_of_st','vessels','thallium']
   target = 'heart_disease'
   df[features] = df[features].apply(pd.to_numeric)
   
   # Create the feature matrix and target vector
   X = df[features]
   y = df[target]
   
   # Split the data into training and testing sets
   X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
   
   # Train a random forest classifier on the training set
   rf_clf = RandomForestClassifier(n_estimators=100, random_state=42)
   rf_clf.fit(X_train, y_train)
   
   # Define the Streamlit app
   def app():
       st.title("Heart Failure Prediction App")
       st.write("This app predicts the likelihood of heart failure based on several risk factors.")
       
       # Get user input for the risk factors
       age = st.slider("Age", 18, 100)
       sex = st.selectbox("Sex", ["Male", "Female"])
       chest_pain_type = st.selectbox("Chest Pain Type", ["Typical Angina", "Atypical Angina", "Non-Angina", "Asymptomatic"])
       resting_blood_pressure = st.slider("Resting Blood Pressure (mm Hg)", 80, 200)
       cholestoral = st.slider("Cholesterol (mg/dl)", 50, 600)
       fasting_blood_sugar = st.selectbox("Fasting Blood Sugar > 120 mg/dl", ["False", "True"])
       ekg_results = st.selectbox("EKG Results", ["Normal", "Abnormal", "Probable"])
       max_hr = st.slider("Maximum Heart Rate Achieved", 50, 220)
       exercise_angina = st.selectbox("Exercise Induced Angina", ["No", "Yes"])
       ST_depression = st.number_input("ST Depression Induced by Exercise", min_value=0.0, max_value=10.0, value=0.0, step=0.1)
       slope_of_st = st.selectbox("Slope of the Peak Exercise ST Segment", ["Upsloping", "Flat", "Downsloping"])
       vessels = st.selectbox("Number of Major Vessels Colored by Flourosopy", ["0", "1", "2", "3"])
       thallium = st.selectbox("Thallium", ["Normal", "Fixed Defect", "Reversible Defect"])
   
       # Convert categorical variables to numerical variables
       sex = 1 if sex == "Female" else 0
       chest_pain_type = ["Typical Angina", "Atypical Angina", "Non-Angina", "Asymptomatic"].index(chest_pain_type)
       fasting_blood_sugar = 1 if fasting_blood_sugar == "True" else 0
       ekg_results = ["Normal", "Abnormal", "Probable"].index(ekg_results)
       exercise_angina = 1 if exercise_angina == "Yes" else 0
       slope_of_st = ["Upsloping", "Flat", "Downsloping"].index(slope_of_st)
       thallium = ["Normal", "Fixed Defect", "Reversible Defect"].index(thallium)
   
       # Make a prediction using the trained random forest classifier
       features = [age, sex, chest_pain_type, resting_blood_pressure, cholestoral,
                   fasting_blood_sugar, ekg_results, max_hr, exercise_angina,
                   ST_depression, slope_of_st, vessels, thallium]
       prediction = rf_clf.predict([features])[0]

       # Prediction of Heart Failure Present or Absent
       if prediction == 0:
           st.write("HEART DISEASE ABSENT") #"Based on the provided information, it is unlikely that you have heart failure.")
       else:
           if prediction == 1 or prediction == 2 or prediction == 3 or prediction == 4:
              st.write("HEART DISEASE PRESESNT")
           #st.write("Based on the provided information, you may have heart failure. Please consult with a medical professional.")
           
   app()
   
   
   
else:
   st.subheader("HEART FAILURE PREDICTION")   
   def add_bg_from_url():
     st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("https://media.istockphoto.com/id/1163285589/vector/abstract-medical-background-with-flat-icons-and-symbols-template-design-with-concept-and.jpg?s=612x612&w=0&k=20&c=q9PFxIxWe-lasksFZ56obgC2gdZqzME6MkrdkfoW07A=");
            background-attachment: fixed;
            background-size: cover
        }}
        </style>
        """,
        unsafe_allow_html=True
     )
   add_bg_from_url()     


   st.write("The project primarily focused on the health care domain of prediction and detection of health issues especially issues of heart failure. One of the main issues of world in health domain are cardiovascular diseases. These diseases killing more than 17 million people globally every year. This projects helps to predict the patients with heart failures. This helps in avoiding and predicting the health issues in the primary stage.")
   st.write(" CAPSTONE PROJECT 606")
   st.write(" BY SRI BHANU GUNDU (CW65895)")
 

def load_data():
    df=pd.read_csv('https://raw.githubusercontent.com/GunduSriBhanu/SriBhanu_DATA606/main/data/uci_heart_data.csv',sep = ',')
    return df

data = load_data()

    

        
        


    