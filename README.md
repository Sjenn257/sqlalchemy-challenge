# SQLAlchemy Homework (Climate in Honolulu, Hawaii)
![image](https://user-images.githubusercontent.com/82002107/131227624-bf0e6ca4-056d-4839-ba0f-fe0e3749e594.png)

Lucky for me, my homework is taking me to Honolulu, Hawaii to analyze the climate in the area (temp and precipitation-wise).

## Part 1: Climate Analysis & Exploration

For climate analysis and exploration, I connected to a sqlite database to find two tables: Measurement and Station. 

The Measurement table provided precipitation and temperature data from 9 stations located in Honolulu, Hawaii between 1-1-2010 through 8-23-2017. The Station table provided geographical data and the names of the 9 stations.

The following figure shows the last 12 months of precipitation captured in the dataset:

![one_year_precipitation](https://user-images.githubusercontent.com/82002107/132607465-62c23ef5-98b0-4f60-b63d-481b38c06edf.png)

On average, preciptation was just below 0.2 but did peak as high as 6.7.

The Waihee station was the most active. The following figure plots a histogram of temperature readings observed at that station:

![tobs_histogram](https://user-images.githubusercontent.com/82002107/132607764-411dd1c8-4009-44c5-a89c-653e633ef620.png)

## Part 2: Climate App

For the climate app, I created an API page to extract this information. The home page explains the routes.

<Home Page>

Welcome to this free API page for Honolulu, Hawaii's historical weather information including temperature and precipitation.

One-year information is available 2016-08-23 through 2017-08-23. Summary temperature data available 2010-01-01 through 2017-08-23.

Available Routes:

/api/v1.0/precipitation -- one year of precipitation data 2016-8-23 through 2017-08-23 at all Honolulu stations
/api/v1.0/stations -- Honolulu stations and their locations
/api/v1.0/tobs -- one year of temperatures observed 2016-8-23 through 2017-08-23 at all Honolulu stations
/api/v1.0/starttemp/2016-01-01 -- provides high, low, average temperature from start date entered through 2017-08-23
/api/v1.0/starttemp/2016-01-01/endtemp/2016-01-31 -- provides high, low, average temperature from start date entered through the end date entered

*Enter date in this format: yyyy-mm-dd


