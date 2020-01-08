import googlemaps
import json
import pandas as pd
import csv

# Define the API Key.
# keep API key code hidden!
API_KEY = 'ENTER_YOUR_KEY'
gmaps = googlemaps.Client(key = API_KEY)

#get route coordinate pointsı
def get_route():
    geocode_resultstart= gmaps.geocode('Disneyland')[0]
    geocode_resultend=gmaps.geocode('Lynwood')[0]
    latlong_result1= geocode_resultstart['geometry']['location']
    latlong_result2= geocode_resultend['geometry']['location']
    return(latlong_result1, latlong_result2)




#open csv file
#read in first row of data(lat, long)
#parse these coordinates
#use for loop to iterate through streetlight coords
#store streetlight lat and long coord in a set

def findCoordsInFile(path, latlong_result1, latlong_result2):
    with open('STLIGHT.csv', 'r') as file:
    reader= csv.DictReader(file)
    count= 0
    #draw bounds for Lat and long coordinates taken from LatLngBound class
    bounds= gmaps.getBounds(latlong_result1, latlong_result2)
    light_locations=set()
    for row in reader:
        value= row['the_geom']
        encoded= value.split()
        long_value= encoded[1]
        lat_value = encoded[2]
        latlong_resultLight= (lat_value, long_value)
        for point in latlong_resultLight:
            if (bounds.contains(light)):
                #increment counter
                count++
                light_locations.add(point)
    return light_locations






