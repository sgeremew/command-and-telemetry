GPS 
Flight Command and Telemetry


GPS Objective (test run):


For telemetry we need to recieve a csv file containing gps data from Sensor Collection Team such as: 

latitude, longitude, altitude

1,2,3

34.56,0.999,23.23

etc.


We will parse the csv file to get the data that we need and then store the data into a telemtry record 
that will then be stored into our Telemetry Database.
This information will be broadcasted to the ground team.

In the code below we are treating each row as a snapshot of the position captured. Then the data is 
parsed and stored into a dictionary where the keys are the position and the values are the list of data 
points such as latitude, longitude, etc.

The data that is stored in the dictionary will be adjusted to how the Sensor 
team stores it.


To-Do:

We need to figure out how the Sensor Collection team is sending the csv file and how we plan on 
recieving it.
