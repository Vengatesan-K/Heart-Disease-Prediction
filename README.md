# Heart Disease Prediction 

> ${\textsf{\color{Darkblue}Predicting probability of heart disease in patients.}}$
***

![Heart](https://www.econsight.com/wp-content/uploads/2022/12/Medical-Imaging.jpg)

***

<table align="center">
    <tr>
        <td width="10%">
            <img src="https://www.pngall.com/wp-content/uploads/2016/06/Health-Free-Download-PNG.png">
        </td>
        <td>
            <div align="center" style="font-size:200%">
                <font color="#21618C">
                    <b>Diagnosing Heart Disease</b> 
                </font>
            </div>
        </td>
    </tr>
</table>

<hr>

> <span style="font-family:Comic Sans MS"> 🎯 Aims to develop a predictive model for heart disease detection using a dataset containing various physiological and clinical attributes of individuals.</span> 

> <span style="font-family:Comic Sans MS"> 🎯 The primary objective is to create a machine learning model that can accurately predict the likelihood of an individual having heart disease based on their characteristics and medical data.</span>

___


<table align="center">
    <tr>
        <td width="7%">
            <img src="https://qvcc.edu/wp-content/uploads/2017/08/information-clipart-information-icon-1024x1024@2x.png">
        </td>
        <td>
            <div align="center" style="font-size:200%">
                <font color="#21618C">
                    <b>About Features</b> 
                </font>
            </div>
        </td>
    </tr>
</table>

<hr>

|S.No|Features|Detail|
|------|------|------|
|1    | Age|   Refers to the numerical representation of a person's age in years.    |
|2    |Sex|   Typically represents the gender of an individual, often encoded as binary values (0 for female, 1 for male).   |
|3    |ChestPainType|   Categorization of chest pain experienced by individuals, often classified into categories like typical angina, atypical angina, non-anginal pain, and asymptomatic.|
|4    |RestingBP|Stands for Resting Blood Pressure and represents the blood pressure of an individual measured at rest in millimeters of mercury (mmHg).|
|5    | Cholesterol	|Denotes the level of cholesterol in the blood, usually measured in milligrams per deciliter (mg/dL). |
|6    |FastingBS|Stands for Fasting Blood Sugar and represents the blood sugar level of an individual after fasting, typically measured in milligrams per deciliter (mg/dL)  |
|7    |RestingECG|Resting Electrocardiographic Results, detailing the electrical activity of the heart at rest, often classified into different categories such as normal, abnormal ST-T wave, and hypertrophy.|
|8    |MaxHR| Maximum Heart Rate and represents the highest heart rate achieved by an individual during an exercise test, measured in beats per minute (bpm). |
|9    | ExerciseAngina |Exercise-Induced Angina, indicating whether an individual experiences chest pain during exercise, often represented as a binary value (0 for no, 1 for yes). |
|10     |	Oldpeak	|ST depression induced by exercise relative to rest, providing insights into the heart's activity during exercise.   |
|11   | ST_Slope |Refers to the slope of the peak exercise ST segment, which describes the heart rate change during exercise and recovery.  |
|12     |	HeartDisease    |Typically denotes the presence or absence of heart disease, often encoded as a binary value (0 for absence, 1 for presence) in the heart disease prediction dataset.    |


```mermaid
flowchart LR

A[Data Collection] -->|Kaggle| B(Cleaning)
B --> C{Preprocessing}
C -->|Visualization| D[EDA]
C -->|ML Algorithms| E[Predictions]
```
