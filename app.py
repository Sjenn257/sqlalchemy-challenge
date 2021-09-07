from flask import Flask, jsonify


import datetime as dt
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func


app = Flask(__name__)

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f'/api/v1.0/"start date"<br/>'        
        f'/api/v1.0/"start date"/"end date"<br/><br/>'
        f'**Must use date format in quotations: "yyyy-m-d"<br/>'
    )


@app.route("/api/v1.0/precipitation")
def get_precipitation():
    engine = create_engine("sqlite:///Resources/hawaii.sqlite",echo=False)
    Base = automap_base()
    Base.prepare(engine, reflect=True)
    Base.classes.keys()
    Measure = Base.classes.measurement


    session=Session(engine)

    year_start=dt.date(2017, 8 ,23)-dt.timedelta(days=365)
    results = session.query(Measure.date, Measure.prcp).filter(Measure.date>=year_start).all()


    session.close()


    # Create a dictionary from the row data and append to a list of all_passengers
    all_precipitation = []
    for date, prcp in results:
        prcp_dict = {}
        prcp_dict["date"] = date
        prcp_dict["prcp"] = prcp
        all_precipitation.append(prcp_dict)

    return jsonify(all_precipitation)


@app.route("/api/v1.0/stations")
def get_stations():
    engine = create_engine("sqlite:///Resources/hawaii.sqlite",echo=False)
    Base = automap_base()
    Base.prepare(engine, reflect=True)
    Base.classes.keys()
    Station = Base.classes.station


    session=Session(engine)

    results=session.query(Station.station, Station.name).all()


    session.close()


    # Create a dictionary from the row data and append to a list of all_passengers
    all_stations = []
    for station, name in results:
        station_dict = {}
        station_dict["station"] = station
        station_dict["name"] = name
        all_stations.append(station_dict)

    return jsonify(all_stations)

@app.route("/api/v1.0/tobs")
def get_tobs():
    engine = create_engine("sqlite:///Resources/hawaii.sqlite",echo=False)
    Base = automap_base()
    Base.prepare(engine, reflect=True)
    Base.classes.keys()
    Measure = Base.classes.measurement


    session=Session(engine)

    year_start=dt.date(2017, 8 ,23)-dt.timedelta(days=365)
    results=session.query(Measure.date, Measure.tobs).filter(Measure.station=='USC00519281').filter(Measure.date>=year_start).all()


    session.close()


    # Create a dictionary from the row data and append to a list of all_passengers
    all_tobs = []
    for date, tobs in results:
        tobs_dict = {}
        tobs_dict["date"] = date
        tobs_dict["tobs"] = tobs
        all_tobs.append(tobs_dict)

    return jsonify(all_tobs)

@app.route("/api/v1.0/<start>")
def get_start(start):
    engine = create_engine("sqlite:///Resources/hawaii.sqlite",echo=False)
    Base = automap_base()
    Base.prepare(engine, reflect=True)
    Base.classes.keys()
    Measure = Base.classes.measurement


    session=Session(engine)

    results=session.query(func.min(Measure.tobs), func.max(Measure.tobs), func.avg(Measure.tobs)).\
        filter(Measure.date>=start).all()


    session.close()


    # Create a dictionary from the row data and append to a list of all_passengers
    all_summary = []
    for min, max, avg in results:
        summary_dict = {}
        summary_dict["min"] = min
        summary_dict["max"] = max
        summary_dict["avg"] = avg
        all_summary.append(summary_dict)

    return jsonify(all_summary)


@app.route("/api/v1.0/<start>/<end>")
def get_end(start,end):
    engine = create_engine("sqlite:///Resources/hawaii.sqlite",echo=False)
    Base = automap_base()
    Base.prepare(engine, reflect=True)
    Base.classes.keys()
    Measure = Base.classes.measurement


    session=Session(engine)

    results=session.query(func.min(Measure.tobs), func.max(Measure.tobs), func.avg(Measure.tobs)).\
        filter(Measure.date>=start).filter(Measure.date<=end).all()


    session.close()


    # Create a dictionary from the row data and append to a list of all_passengers
    all_summary_end = []
    for min, max, avg in results:
        summaryend_dict = {}
        summaryend_dict["min"] = min
        summaryend_dict["max"] = max
        summaryend_dict["avg"] = avg
        all_summary_end.append(summaryend_dict)

    return jsonify(all_summary_end)



if __name__ == '__main__':
    app.run(debug=True)
