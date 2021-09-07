from flask import Flask, jsonify

import pandas as pd
import numpy as np
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


if __name__ == '__main__':
    app.run(debug=True)
