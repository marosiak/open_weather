# open_weather
Web application with REST for IoT

![alt text](https://i.imgur.com/RKqWR7p.png "img")

# Using API
The application does provide simple API which you can use for your own purposes.

The documentary **is not compleate**, you can perform many more actions such as [PUT, PATCH, DELETE, HEAD, OPTIONS]
### Servers
Currently there is only one server [There will be IP Address]

## Stations
### Getting list of stations:
Method type: **[GET]**

Endpoint: **/api/stations/**


### Getting details of station
Method type: **[GET]**

Endpoint: **/api/stations/[int]/**


## Sensors

### Getting list of sensors for station
Method type: **[GET]**

Endpoint: **/api/stations/[int]/sensors/**

### Adding new sensor to station
**Important** You need to be logged in + you have to be owner of the specific station

Method type: **[POST]**

Endpoint: **/api/stations/[int]/sensors/**

Form-data: **'name' = [string]**

### Getting sensor details
Method type: **[GET]**

Endpoint: **/api/stations/[int]/sensors/[int]**

## SensorData

### Getting list of SensorData
Method type: **[GET]**

Endpoint: **/api/stations/[int]/sensors/[int]/data/**

### Writting SensorData
**Important** You need to be logged in + you have to be owner of the specific station

Method type: **[POST]**

Endpoint: **/api/stations/[int]/sensors/[int]/data/**

Form-data: **'value' = [int]**
