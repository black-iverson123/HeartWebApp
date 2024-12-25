from flask_wtf import FlaskForm
from wtforms import IntegerField, FloatField, StringField, SubmitField
from wtforms.validators import DataRequired

class DataForm(FlaskForm):
    name = StringField("Patient's Name", validators=[DataRequired(message="Patient's Name is Required!!!")])
    age = IntegerField("Patient's Age", validators=[DataRequired(message="Patient's age is Required!!!")])
    sex = StringField("Patient's Sex ", validators=[DataRequired(message="Patient's sex is Required!!")])
    cp = StringField("Chest Pain Type", validators=[DataRequired(message="This Field is Required!!")])
    restecg = StringField("Resting Electrocardiographic Results", validators=[DataRequired(message="This Field is Required!!")])
    thalach = IntegerField("Maximum Heart Rate Achieved", validators=[DataRequired(message="This Field is Required!!")])
    exng = StringField("Exercise Induced Angina", validators=[DataRequired(message="This Field is Required!!")])
    oldpeak = FloatField("Oldpeak", validators=[DataRequired(message="This Field is Required!!")])
    slp = IntegerField("SLP", validators=[DataRequired(message="This Field is Required!!")])
    caa = IntegerField("Number of Major Vessels (Caa)", validators=[DataRequired(message="This Field is Required!!")])
    thall = IntegerField("Thall", validators=[DataRequired(message="This Field is Required!!")])
    submit = SubmitField("Check!!")
