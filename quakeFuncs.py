from urllib.request import *
import ssl
from json import *
from datetime import *
from operator import *

class Earthquake:
   def __init__(self, place, mag, longitude, latitude, time):
      self.place = place
      self.mag = mag
      self.longitude = longitude
      self.latitude = latitude
      self.time = time

   def __eq__(self, other):
      return self.place == other.place and self.mag == other.mag and self.longitude == other.longitude and self.latitude == other.latitude and self.time == other.time

   def __repr__(self):
      return "%s %f %f %f %d" % (self.place, self.mag, self.longitude, self.latitude, self.time) 

   def __lt__(self, other):
      return self.mag < other.mag



def read_quakes_from_file(filename):
   inFile = open(filename, 'r')
   earthquakes = []

   for line in inFile:

      data = line.split()      
      quake = Earthquake(" ".join(data[4:]), float(data[0]), float(data[1]), float(data[2]), int(data[3]))
      earthquakes.append(quake)

   inFile.close()

   return earthquakes



def display_quakes(earthquakes):
   print("\nEarthquakes:")
   print("------------")
   for quake in earthquakes:
      print("(%.2f) %40s at %s (%.3f, %.3f)" % (quake.mag, quake.place, time_to_str(quake.time), quake.longitude, quake.latitude))

def sort_by_mag(quakes):
   earthquakes = quakes
   earthquakes.sort(reverse = True)
   return earthquakes

def sort_by_time(quakes):
   earthquakes = quakes
   earthquakes.sort(key=attrgetter('time'), reverse = True)
   return earthquakes

def sort_by_longitude(quakes):
   earthquakes = quakes
   earthquakes.sort(key=attrgetter('longitude'))
   return earthquakes

def sort_by_latitude(quakes):
   earthquakes = quakes
   earthquakes.sort(key=attrgetter('latitude'))
   return earthquakes

def filter_by_mag(quakes, low, high):
   earthquakes = [quake for quake in quakes if (quake.mag <= high and quake.mag >= low)]
   return earthquakes     
     
def filter_by_place(quakes, word):
   text = word.lower()
   earthquakes = [quake for quake in quakes if (quake.place.lower().find(text) != -1)]
   return earthquakes 

def quake_from_feature(f):
   return Earthquake(f['properties']['place'], float(f['properties']['mag']), float(f['geometry']['coordinates'][0]), float(f['geometry']['coordinates'][1]), int((f['properties']['time']) / 1000))

def get_json(url):
   gcontext = ssl.SSLContext() 
   with urlopen(url, context=gcontext) as response:
      html = response.read()
   htmlstr = html.decode("utf-8")
   return loads(htmlstr)

def time_to_str(time):
   return datetime.fromtimestamp(time).strftime('%Y-%m-%d %H:%M:%S') 

def save_data(quakes, filename):
   outFile = open(filename, 'w')

   for quake in quakes:
      outFile.write(str(quake.mag) + " " + str(quake.longitude) + " " + str(quake.latitude) + " " + str(quake.time) + " " + str(quake.place) + "\n")

   outFile.close()

   

      


   
