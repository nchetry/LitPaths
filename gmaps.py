import googlemaps
import json
import pandas as pd
import csv
import geocoder

# Define the API Key.
# keep API key code hidden!
API_KEY = 'ENTER_YOUR_KEY'
gmaps = googlemaps.Client(key = API_KEY)

#get route coordinate points 
#open csv file
#read in first row of data(lat, long)
#parse these coordinates
#use for loop to iterate through streetlight coords
#if streetlight lat and long coords are within the bounds, store coords in a set

def findCoordsInFile():
    #create bounds
    g = geocoder.osm('Lynwood, CA')
    s = geocoder.osm('Disneyland, CA')
    bounds = [g.lat, g.lng, s.lat, s.lng]
    # print(bounds)
    with open('STLIGHT.csv', 'r') as file:
        reader= csv.DictReader(file)
        count= 0
        #draw bounds for Lat and long coordinates taken from LatLngBound class
        light_locations=set()
        for row in reader:
            value= row['the_geom']
            encoded= value.split()
            long_value= encoded[1]
            lat_value = encoded[2]
            latlong_resultLight= (lat_value, long_value)
            # print(latlong_resultLight)
            for point in latlong_resultLight:
                if(point in bounds):
                    #increment counter
                    count+=1
                    light_locations.add(point)
                    print(light_locations)
    return light_locations

findCoordsInFile()


