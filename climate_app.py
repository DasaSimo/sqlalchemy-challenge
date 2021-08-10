import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
import datetime as dt

from flask import Flask, jsonify

# create engine
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save references to each table
Msrmnts = Base.classes.measurement
Station = Base.classes.station

# Flask Setup
app = Flask(__name__)

# Flask Routes

@app.route("/")
def api_routes():
    """All available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0/<start>/<end>"
    )


# 
@app.route("/api/v1.0/precipitation")
def precipitation():
   
    session = Session(engine) 
    # getting max_value for date
    d1 =  session.query(func.max(Msrmnts.date)).first()
    max_d = dt.datetime.strptime(d1[0], "%Y-%m-%d")
    # going back one year
    query_date = max_d  - dt.timedelta(days=365)
    # getting data from database
    results= session.query(Msrmnts.date,func.max(Msrmnts.prcp)).\
            filter(Msrmnts.date >= query_date).\
            group_by(Msrmnts.date).all()
    session.close()

    # preparing results set   
    precipitation_dict = {}
    for date, prcp in results:
        precipitation_dict[date] = prcp
    return jsonify(precipitation_dict)



@app.route("/api/v1.0/stations")
def stations():
    
    session = Session(engine)
    # Query all stations in dataset
    results = session.query(Station.station,Station.name,Station.latitude, Station.longitude, Station.elevation).all()
    session.close()
    
    # preparing outout data
    all_stations = []
    for station,name, latitude, longitude, elevation in results:
        station_dict = {}
        station_dict["station"] = station
        station_dict["name"] = name
        station_dict["latitude"] = latitude
        station_dict["longitude"] = longitude
        station_dict["elevation"] = elevation
      
        all_stations.append(station_dict)
        
    return jsonify(all_stations)    


if __name__ == '__main__':
    app.run(debug=True)

