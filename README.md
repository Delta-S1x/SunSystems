This is a data sending system setup using ZMQ and Mysql connector. The server connects incoming data from multiple "sensors" at the same time and then takes that data and updates the appropriate Mysql Tables.

The use case for this would be having multiple Pi's set up sending weather station data(or any data at all really) to one handler to update a Database. Would work great to feed live data to a web page.
