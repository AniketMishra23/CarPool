import requests
from pprint import pprint
import folium


BASE_URL = 'https://nominatim.openstreetmap.org/search?format=json'

postcode = 'G42 9AY'

response = requests.get(f"{BASE_URL}&postalcode={postcode}")
data = response.json()
pprint(data)


     
latitude = data[0].get('lat')
longitude = data[0].get('lon')
print(latitude, longitude)

bbox = data[0].get('boundingbox')
print(bbox)



zipcode = '2601'

response = requests.get(f"{BASE_URL}&postalcode={zipcode}")
data = response.json()
print(data)

latitude2 = data[0].get('lat')
longitude2 = data[0].get('lon')

print(latitude2, longitude2)






# create tuples representing our location
location = float(latitude), float(longitude)
location2 = float(latitude2), float(longitude2)

# center the map at Amsterdam
amsterdam = (52.3676, 4.9041)

# create a Folium map centred at the above location
m = folium.Map(location=amsterdam, zoom_start=4, width=800, height=400)

# add markers at the locations
folium.Marker(location, popup="The postcode brought me here").add_to(m)
folium.Marker(location2, popup="The postcode brought me here").add_to(m)

# refer to the map to display it in Jupyter/Colab notebooks
print(m)



# generator expression to compute midpoint of the two locations
# this works because both locations are of form: (lat, long)
# zipping them together allows us to iterate over both lats at once, 
# and then both lons at once
midpoint_gen = ((x+y)/2 for x,y in zip(location, location2))

# convert generator to a tuple representing lat/longitude of the midpoint
midpoint = tuple(midpoint_gen)

print(location)
print(location2)
print(midpoint)




# create Folium map
m = folium.Map(location=midpoint, zoom_start=4, width=800, height=400)

# add marker at the locations
folium.Marker(location, popup="The postcode brought me here").add_to(m)
folium.Marker(location2, popup="The postcode brought me here").add_to(m)
folium.Marker(midpoint, popup="Middle!").add_to(m)

print(m)



from geopy.distance import distance

km = distance(location, location2 )
miles = distance(location, location2).miles

print("Distance between postcodes:")
print(f"{km}")
print(f"{miles} miles")




# create a Folium map centred at the above location
m = folium.Map(location=midpoint, zoom_start=4, width=800, height=400)

# add marker at the locations
folium.Marker(location, popup="The postcode brought me here").add_to(m)
folium.Marker(location2, popup="The postcode brought me here").add_to(m)

# add line between points
folium.PolyLine((location,location2)).add_to(m)

print(m)