# import necessary libraries
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

from flask_sqlalchemy import SQLAlchemy
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



if __name__ == "__main__":
    app.run()
