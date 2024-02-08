# Import the dependencies.

import numpy as np
import datetime as dt
import sqlalchemy
from flask import Flask, jsonify
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, desc


#################################################
# Database Setup
#################################################

engine = create_engine("sqlite:///C:/Users/djgoo/DataAnalysis/sqlalchemy-challenge/SurfsUp/Resources/hawaii.sqlite")


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

app = Flask(__name__)


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
    latest_date = dt.datetime(2017, 8, 23)
    Year_prior = latest_date - dt.timedelta(days=365)
    results = session.query(Measurement.date, Measurement.prcp)\
    .filter(Measurement.date >= Year_prior).order_by(desc(Measurement.date)).all()
    data = []
    for date, prcp in results:
        precip_dict = {}
        precip_dict["date"] = date
        precip_dict["precipitation"] = prcp
        data.append(precip_dict)
    
    return jsonify(data)
session.close()

@app.route("/api/v1.0/stations")
def stations():
    session = Session(engine)
    session = Session(engine)
    results = session.query(Station.station).all()
    stations = []
    for station in results:
        stations.append(station)
        
    return jsonify(stations)
session.close()

@app.route("/api/v1.0/tobs")
def tobs():
    session = Session(engine)
    latest_date = dt.datetime(2017, 8, 23)
    Year_prior = latest_date - dt.timedelta(days=365)
    results = session.query(Measurement.tobs).filter(Measurement.station=='USC00519281').filter(Measurement.date >= Year_prior).all()
    tobs = []
    for T in results:
        results.append(tobs)
    return jsonify(results)
session.close()

@app.route("/api/v1.0/<start>")
def start(start):
    session = Session(engine)
    results = session.query(func.min(Measurement.tobs), func.max(Measurement.tobs), func.avg(Measurement.tobs)).filter(Measurement.date >= start).all()
    tobstemps = []
    for TT in tobstemps:
        tobstemps.append(TT[0])
        tobstemps.append(TT[1])
        tobstemps.append(TT[2])
    return jsonify(tobstemps)
session.close()

@app.route("/api/v1.0/<start>/<end>")
def start_end(start, end):
    session = Session(engine)
    results = session.query(func.min(Measurement.tobs), func.max(Measurement.tobs), func.avg(Measurement.tobs)).filter(Measurement.date >= start).filter(Measurement.date <= end).all()
    tobstemps = []
    for TT in tobstemps:
        tobstemps.append(TT[0])
        tobstemps.append(TT[1])
        tobstemps.append(TT[2])
    return jsonify(tobstemps)
session = Session(engine)

if __name__ == '__main__':
    app.run(debug=True)