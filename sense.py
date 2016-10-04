import logging
from twoDigit.twoDigit import numToMatrix
from sense_hat import SenseHat
from datetime import datetime
from time import sleep

# Set up the logfile name based on date/time
logfile = "sensor-data-"+str(datetime.now().strftime("%Y%m%d-%H%M"))+".csv"
# Logging settings and format for CSV
logging.basicConfig(filename=logfile, level=logging.DEBUG,
    format='%(asctime)s %(message)s',
    datefmt='%Y-%m-%d, %H:%M:%S,')

sh = SenseHat() # Connect to Sense HAT
sh.low_light = 1 # set LED light intensity to low
h_old = 0
col = [0,0,255]

#header
logging.info( 'Date_Time,Temperature,Humidity,Pressure' )

while True: # Main loop

   #Read the sensor data
   h = sh.get_humidity() # Take humidity reading
   t = sh.get_temperature() # Take temperature reading
   p = sh.get_pressure() # Take barometric pressure reading

   #Log the sensor values
   logging.info( str(h) + str(',') + str(t) + str(',') + str(p) ) # Log value to file

   #set LED for status; avoid disturbing during dark hours :-)
   if (datetime.today().hour > 8 and datetime.today().hour < 18):
   	if h > h_old: # If humidity has increased...
       		col = [210,0,0] # Set to red
   	else: # If humidity has decreased...
       		col = [0,210,0] # Set to green
   	h = int(round(h,0)) # Round to a whole percent
   	i = numToMatrix(h,col) # Create 2-digit image for matrix
   	sh.set_pixels(i) # Display reading
   	sleep(1) #Every second

   	h_old = h # Set previous value
