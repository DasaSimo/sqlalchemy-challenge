# sqlalchemy-challenge

## Climate Analysis and Exploration
We used Python and SQLAlchemy to do basic climate analysis and data exploration of the climate database. All of the following analysis was completed using SQLAlchemy ORM queries, Pandas, and Matplotlib.
In SQLAlchemy was used create_engine to connect to given sqlite database, automap_base() to reflect the tables into classes and save a reference to those classes called Station and Measurement.
By creating an SQLAlchemy session Python was linked to the database.



### Precipitation Analysis

Using the most recent date in the data set,  the last 12 months of precipitation data was retrieved by querying the 12 preceding months of data. The query results were loaded into a Pandas DataFrame with the index set o the date column. 

### Station Analysis

For station analysis following queries were made:

*  a query to calculate the total number of stations in the dataset.

*  a query to find the most active stations (i.e. which stations have the most rows?).

  * List the stations and observation counts in descending order.

  * Which station id has the highest number of observations?

  * for the the most active station id was performed calculation to find the lowest, highest, and average temperature.

  
  *  a query to retrieve the last 12 months of temperature observation data (TOBS).

  * Filter by the station with the highest number of observations.

  * Query the last 12 months of temperature observation data for this station.

  * Plot the results as a histogram with `bins=12`.

  ##  Climate App
  
  In this part a Flask API was designed based on the queries that we developed. We created following routes:

### Routes


  * `/api/v1.0/precipitation`

  * `/api/v1.0/stations`

  * `/api/v1.0/tobs`
  
  * `/api/v1.0/<start>` and `/api/v1.0/<start>/<end>`

  

## Other Analyses


### Temperature Analysis I

* Hawaii is reputed to enjoy mild weather all year. Is there a meaningful difference between the temperature in, for example, June and December?

* We used  pandas to perform this portion to:.

* Identify the average temperature in June and in  December at all stations across all available years in the dataset

* Use the t-test to determine whether the difference in the means, if any, is statistically significant. 

### Temperature Analysis II

* In this portion we are using the historical data in the dataset to find out what the temperature has previously looked like for a trip from August first to August seventh to to predict the weather for this year trip at the same dates.

*  the `calc_temps` function was used to calculate the min, avg, and max temperatures for the trip using the matching dates from a previous year (i.e., use "2017-08-01").

* Plot the min, avg, and max temperature from your previous query as a bar chart.

 
### Daily Rainfall Average

* We also checked  what the rainfall has been  - we analyze data from the dataset to know more about precipitation for the dates of the trip. The calculation were performed per weather stationusing the previous year matching dates



### Daily Temperature Normals

* The daily normals for the duration of the trip were calculating as a next step. Normals are the averages for the min, avg, and max temperatures. 
* Pandas was used to plot an area plot (`stacked=False`) for the daily normals.

![image](https://user-images.githubusercontent.com/84484371/142088989-4665e73d-0d5d-460f-94c8-cda189d42c44.png)

 

