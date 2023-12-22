from flask import Flask, request, render_template
import numpy as np
from sklearn.preprocessing import StandardScaler
import joblib as joblib
import os
import pandas as pd

model = joblib.load('randomforest_model.pkl')
scaler = joblib.load('standardScaler.pkl')

app = Flask(__name__)

IMG_FOLDER = os.path.join('static', 'IMG')
app.config['UPLOAD_FOLDER'] = IMG_FOLDER


from sklearn.preprocessing import LabelEncoder

# Sample label encoding function
def encode_categorical_features(data):
    le = LabelEncoder()
    categorical_columns = ['Sex', 'ChestPainType', 'RestingECG', 'ExerciseAngina', 'ST_Slope']
    
    # Encode categorical columns with label encoding
    for col in categorical_columns:
        data[col] = le.fit_transform(data[col])
    
    return data

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        Age = float(request.form['Age'])
        Sex = request.form['Sex']
        ChestPainType = request.form['ChestPainType']
        RestingBp = float(request.form['RestingBp'])
        Cholesterol = float(request.form['Cholesterol'])
        FastingBS = float(request.form['FastingBS'])
        RestingECG = request.form['RestingECG']
        MaxHR = float(request.form['MaxHR'])
        ExerciseAngina = request.form['ExerciseAngina']
        Oldpeak = float(request.form['Oldpeak'])
        ST_Slope = request.form['ST_Slope']

        # Prepare input data for prediction
        input_data = {
            'Age': [Age],
            'Sex': [Sex],
            'ChestPainType': [ChestPainType],
            'RestingBp': [RestingBp],
            'Cholesterol': [Cholesterol],
            'FastingBS': [FastingBS],
            'RestingECG': [RestingECG],
            'MaxHR': [MaxHR],
            'ExerciseAngina': [ExerciseAngina],
            'Oldpeak': [Oldpeak],
            'ST_Slope': [ST_Slope]
        }

        # Create a DataFrame with the input data
        input_df = pd.DataFrame(input_data)

        # Encode categorical features
        encoded_input = encode_categorical_features(input_df)

        # Scale numerical features
        numerical_features = ['Age', 'RestingBp', 'Cholesterol', 'FastingBS', 'MaxHR', 'Oldpeak']
        scaled_input = encoded_input.copy()  
        scaled_input[numerical_features] = scaler.transform(encoded_input[numerical_features])

        # Make a prediction using the loaded model
        prediction_array = model.predict(scaled_input)
        
    
        if prediction_array == 1:
            prediction = "Yes"
            image = prediction + ".png"
            image = os.path.join(app.config['UPLOAD_FOLDER'], image)
        else:
            prediction = "No"
            image = prediction + ".png"
            image = os.path.join(app.config['UPLOAD_FOLDER'], image)
        
        return render_template('index.html', prediction=prediction, image=image)

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
    

