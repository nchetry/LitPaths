# pip install googlemaps
import googlemaps
import json
import requests
from key import key
url= "https://maps.googleapis.com/maps/api/place/textsearch/json"
details_url= "https://maps.googleapis.com/maps/api/place/details/json"

#Set Maps API Key
gmap_key= googlemaps.Client(key)
df["LAT"] = None
df["LON"] = None

for i in range(0, len(df), 1):
	geocode_result=gmap_key.geocode(df.iat[i,0])
	try:
		lat= geocode_result[0]["geometry"]["location"]["lat"]
		lon= geocode_Result[0]["geometry"]["location"]["lon"]

with open('STLIGHT.csv', 'r') as file:
	reader= csv.DictReader(file)

	count =0

	for row in reader:
		value= row['the_geom']
		encoded= value.split()
		longitude= encoded[1]
		latatitude = encoded[2]
		print(longitude, latatitude)












	


