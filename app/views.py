from flask import render_template, flash, redirect, url_for
from app.forms import DataForm
import numpy as np
from app import app
from app.model import model


@app.route('/index', methods=['GET', 'POST'])
def home():
    """Home route on server load

    Returns:
        _type_: index html page with form class loaded
    """
    form = DataForm()
    return render_template('index.html', form=form)

@app.route('/check', methods=['POST'])
def check():
    """form action route to send parameters
        to loaded model

    Returns:
        _type_: flashed message of predictions
    """
    form = DataForm()
    if form.validate_on_submit():
        sex = form.sex.data
        if sex.lower() == 'male':
            sex = 1
        else:
            sex = 0 
        cp = form.cp.data
        if cp.lower() == "typical angina":
            cp = 1
        elif cp.lower() == "atypical angina":
            cp = 2
        elif cp.lower() == "non-anginal pain":
            cp = 3
        else:
            cp = 4
        restecg = form.restecg.data
        if restecg.lower() == "normal":
            restecg = 0
        elif restecg.lower() == "st-t wave abnormality":
            restecg = 1
        elif restecg.lower() == "left ventricular hypertrophy":
            restecg = 2
        else:
            restecg = 0  # or handle the unexpected case appropriately

        exng = form.exng.data
        if exng.lower() == "yes":
            exng = 1
        else:
            exng = 0
        
        scaled_features = [sex, cp, restecg, exng]
        features = [
            form.age.data, 
            form.thalach.data, 
            form.oldpeak.data, 
            form.slp.data, 
            form.caa.data, 
            form.thall.data
        ]
        final_features = np.array(features + scaled_features).reshape(1, -1)
        
        prediction = model.predict(final_features)
        output = prediction[0]
        
        if output == 1:
            message = "High chance of heart attack"
            alert = "danger"
        else:
            message = "Less chance of a heart attack"
            alert = "info"
        
        flash(f"{form.name.data}, you are predicted to: {message}", alert)
        return redirect(url_for('home'))
    return render_template('index.html', form=form)
