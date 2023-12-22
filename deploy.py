from flask import Flask, request, render_template
import numpy as np
from sklearn.preprocessing import StandardScaler
import joblib as joblib
import os

model = joblib.load('randomforest_model.pkl')
scaler = joblib.load('standardScaler.pkl')

app = Flask(__name__)

IMG_FOLDER = os.path.join('static', 'IMG')
app.config['UPLOAD_FOLDER'] = IMG_FOLDER


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        age = request.form['Age']
        sex = request.form['Sex']
        cpt = request.form['ChestPainType']
        rbp = request.form['RestingBP']
        chl = request.form['Cholestrol']
        fas = request.form['FastingBS']
        recg = request.form['RestingECG']
        mhr = request.form['MaxHR']
        ex = request.form['ExerciseAngina']
        old = request.form['Oldpeak']
        st = request.form['ST_Slope']
        
        new_data_to_scale = np.array([[age, rbp, chl, old, mhr]])
        scaled_new_data_partial = scaler.transform(new_data_to_scale)
        additional_data = np.array([[sex, cpt, fas, recg, ex, st]])
        new_data_combined = np.concatenate((scaled_new_data_partial, additional_data), axis=1)
        prediction = model.predict(new_data_combined)
        image = prediction[0]+'.png'
        image = os.path.join(app.config['UPLOAD_FOLDER'], image)
        return render_template('index.html', prediction=prediction[0], image=image)
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)