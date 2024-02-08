# Import the dependencies.

import numpy as np
import datetime as dt
import sqlalchemy
import flask
from flask import jsonify
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func


#################################################
# Database Setup
#################################################

engine = create_engine("sqlite:///Resources/hawaii.sqlite")


# reflect an existing database into a new model

Base = automap_base()

# reflect the tables

Base.prepare(autoload_with=engine)

# Save references to each table

Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB

session = Session(engine)

#################################################
# Flask Setup
#################################################

app = flask(__name__)


#################################################
# Flask Routes
#################################################
@app.route("/")
def welcome():
    return (f"Hello! Here are all available routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs"
        f"/api/v1.0/<start>"
        f"/api/v1.0/<start>/<end>"
    )
@app.route("/api/v1.0/precipitation")
def precipitation():
    session = Session(engine)

session.close()
@app.route("/api/v1.0/stations")
def stations():
    session = Session(engine)

session.close()
@app.route("/api/v1.0/tobs")
def tobs():
    session = Session(engine)

session.close()
@app.route("/api/v1.0/<start>")
def temperatures_start(start):
    session = Session(engine)

session.close()
@app.route("/api/v1.0/<start>/<end>")
def temps_start_end(start, end):
    session = Session(engine)

session = Session(engine)