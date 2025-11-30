from flask import Flask, render_template, request
from flask_cors import CORS, cross_origin
import pickle
import pandas as pd
import numpy as np

app = Flask(__name__)
CORS(app)

# Load trained ML model
model = pickle.load(open('LinearRegressionModel.pkl', 'rb'))

# Load cleaned dataset (used for dropdown values)
car = pd.read_csv('Cleaned_Car_data.csv')


@app.route('/', methods=['GET'])
def index():
    # Dropdown data
    companies = sorted(car['company'].unique())
    car_models = sorted(car['name'].unique())
    years = sorted(car['year'].unique(), reverse=True)
    fuel_types = sorted(car['fuel_type'].unique())

    # Pass data to HTML template
    return render_template(
        'index.html',
        companies=companies,
        car_models=car_models,
        years=years,
        fuel_types=fuel_types
    )


@app.route('/predict', methods=['POST'])
@cross_origin()
def predict():

    # Receive form data
    company = request.form.get('company')
    car_model = request.form.get('car_models')
    year = int(request.form.get('year'))
    fuel_type = request.form.get('fuel_type')
    driven = int(request.form.get('kilo_driven'))

    # Prepare input for model
    input_df = pd.DataFrame(
        [[car_model, company, year, driven, fuel_type]],
        columns=['name', 'company', 'year', 'kms_driven', 'fuel_type']
    )

    # Prediction
    prediction = model.predict(input_df)[0]

    return str(round(prediction, 2))


if __name__ == '__main__':
    app.run(debug=True)
