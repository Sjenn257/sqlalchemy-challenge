from flask import Flask, jsonify


import datetime as dt
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func


app = Flask(__name__)

@app.route("/")
def welcome():
    """Welcome page with available routes"""
    
    return (
        f"Welcome to this free API page for Honolulu, Hawaii's historical weather information including temperature and precipitation.<br/><br/>"

        f"One-year information is available 2016-08-23 through 2017-08-23. Summary temperature data available 2010-01-01 through 2017-08-23.<br/><br/>"

        f"Available Routes:<br/><br/>"

        f"/api/v1.0/precipitation -- one year of precipitation data 2016-8-23 through 2017-08-23 at all Honolulu stations<br/>"
        f"/api/v1.0/stations -- Honolulu stations and their locations<br/>"
        f"/api/v1.0/tobs -- one year of temperatures observed at Honolulu's most active station 2016-8-23 through 2017-08-23<br/>"
        f'/api/v1.0/starttemp/2016-01-01 -- provides high, low, average temperature from start date entered through 2017-08-23<br/>'        
        f'/api/v1.0/starttemp/2016-01-01/endtemp/2016-01-31 -- provides high, low, average temperature from start date entered through the end date entered<br/><br/>'
        f'*Enter date in this format: yyyy-mm-dd<br/>'
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
    results = session.query(Measure.date, Measure.prcp, Measure.station).filter(Measure.date>=year_start).all()


    session.close()


    # Create a dictionary from the row data and append to a list of all_passengers
    all_precipitation = []
    for date, prcp, station in results:
        prcp_dict = {}
        prcp_dict["date"] = date
        prcp_dict["prcp"] = prcp
        prcp_dict["station"] = station
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

    results=session.query(Station.station, Station.name, Station.latitude, Station.longitude, Station.elevation).all()


    session.close()


    # Create a dictionary from the row data and append to a list of all_passengers
    all_stations = []
    for station, name, latitude, longitude, elevation in results:
        station_dict = {}
        station_dict["station"] = station
        station_dict["name"] = name
        station_dict["latitude"] = latitude
        station_dict["longitude"] = longitude
        station_dict["elevation"] = elevation
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

@app.route("/api/v1.0/starttemp/<starttemp>")
def get_start(starttemp):
    engine = create_engine("sqlite:///Resources/hawaii.sqlite",echo=False)
    Base = automap_base()
    Base.prepare(engine, reflect=True)
    Base.classes.keys()
    Measure = Base.classes.measurement


    session=Session(engine)

    results=session.query(func.min(Measure.tobs), func.max(Measure.tobs), func.avg(Measure.tobs)).\
        filter(Measure.date>=starttemp).all()


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


@app.route("/api/v1.0/starttemp/<starttemp>/endtemp/<endtemp>")
def get_end(starttemp,endtemp):
    engine = create_engine("sqlite:///Resources/hawaii.sqlite",echo=False)
    Base = automap_base()
    Base.prepare(engine, reflect=True)
    Base.classes.keys()
    Measure = Base.classes.measurement


    session=Session(engine)

    results=session.query(func.min(Measure.tobs), func.max(Measure.tobs), func.avg(Measure.tobs)).\
        filter(Measure.date>=starttemp).filter(Measure.date<=endtemp).all()


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
