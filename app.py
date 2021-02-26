# import necessary libraries
from flask_sqlalchemy import SQLAlchemy
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
import os
import pandas as pd
from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)

# from config import URI

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Database Setup
#################################################

# app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///nflDB.db"

#  os.environ.get('DATABASE_URL', '') or

# Remove tracking modifications
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# db = SQLAlchemy(app)


# create route that renders index.html template
@app.route("/")
def home():
    return render_template("index.html")


@app.route("/team")
def team():
    return render_template("team.html")


@app.route("/link1")
def link1():
    return render_template("link1.html")


@app.route("/link2")
def link2():
    return render_template("link2.html")


@app.route("/viz")
def viz():
    return render_template("viz.html")

@app.route("/api/data")
def dataoverall():

    heart_df = pd.read_csv('./Data/heart_failure_clinical_records_dataset.csv')
    new_list = []

    for index, row in heart_df.head(5).iterrows():
        new_dict = {}
        new_dict['Age'] = row['age']
        new_dict['Anaemia'] = row['anaemia']
        new_dict['Creatinine_phosphokinase'] = row['creatinine_phosphokinase']
        new_dict['Diabetes'] = row['diabetes']
        new_dict['Ejection_fraction'] = row['ejection_fraction']
        new_dict['High_blood_pressure'] = row['high_blood_pressure']
        new_dict['Platelets'] = row['platelets']
        new_dict['Serum_creatinine'] = row['serum_creatinine']
        new_dict['Serum_sodium'] = row['serum_sodium']
        new_dict['Sex'] = row['sex']
        new_dict['Smoking'] = row['smoking']
        new_dict['Time'] = row['time']
        new_dict['Death_event'] = row['DEATH_EVENT']
        new_list.append(new_dict)

    return jsonify(new_list)

@app.route("/api/f1score")
def f1score():

    report_df = pd.read_csv('./Data/Report.csv')
    f1_list = []

    for index, row in report_df.head(5).iterrows():
        f1_dict = {}
        f1_dict['Index'] = row['Index']
        f1_dict['Precision'] = row['precision']
        f1_dict['Recall'] = row['recall']
        f1_dict['F1_score'] = row['f1-score']
        f1_dict['Support'] = row['support']
        f1_list.append(f1_dict)

    return jsonify(f1_list)



if __name__ == "__main__":
    app.run()

