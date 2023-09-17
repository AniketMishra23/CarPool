import requests
import os
import dotenv

# Load environment variables
dotenv.load_dotenv()

# SerpApi API endpoint
serpapi_endpoint = "https://serpapi.com/search?engine=google_maps"

# Your SerpApi API Key
api_key = os.getenv("SERP_API_KEY")

# User input for location and destination
location = input("Enter your current location: ")
destination = input("Enter your destination: ")

# Create the query string
query = f"{location} to {destination}"

# Define the parameters for the API request
params = {
    "q": query,
    "api_key": api_key,
    "output": "json"  # You can change the output format if needed
}

try:
    # Send a GET request to the SerpApi endpoint
    response = requests.get(serpapi_endpoint, params=params)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse and print the JSON response
        data = response.json()
        print("Location data retrieved:")
        print(data)
        # google_maps_url = data['search_metadata']['google_maps_url']

# Print the extracted google_maps_url
        # print(google_maps_url)
    else:
        print(f"Error: {response.status_code} - {response.text}")
except Exception as e:
    print(f"An error occurred: {str(e)}")




import math

# Function to calculate the distance between two coordinates using Haversine formula
def haversine(lat1, lon1, lat2, lon2):
    # Radius of the Earth in kilometers
    R = 6371.0
    
    # Convert latitude and longitude from degrees to radians
    lat1 = math.radians(lat1)
    lon1 = math.radians(lon1)
    lat2 = math.radians(lat2)
    lon2 = math.radians(lon2)
    
    # Haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance = R * c
    
    return distance

# Carpooler's route coordinates
carpooler_route = [(40.7128, -74.0060), (41.8781, -87.6298)]  # New York City to Los Angeles

# Sample registered users with their destinations
registered_users = [
    {"name": "User1", "start_location": (40.730610, -73.935242), "destination": (41.8781, -87.6298)},  # NYC to Chicago
    {"name": "User2", "start_location": (34.0522, -118.2437), "destination": (41.8781, -87.6298)},  # LA to Chicago
    {"name": "User3", "start_location": (40.7128, -74.0060), "destination": (34.0522, -118.2437)},  # NYC to LA
    {"name": "User4", "start_location": (41.8781, -87.6298), "destination": (51.5074, -0.1278)},  # Chicago to London
]
    
# Define the maximum distance radius for matching (in kilometers)
max_radius_km = 500.0

# Find users who want to go to the same destination from a location in the carpooler's route
matching_users = []

for user in registered_users:
    start_lat, start_lon = user["start_location"]
    destination_lat, destination_lon = user["destination"]
    
    # Check if the start location of the user is in the carpooler's route
    if any(
        haversine(start_lat, start_lon, car_lat, car_lon) <= max_radius_km
        for car_lat, car_lon in carpooler_route
    ):
        # Check if the destination of the user matches the carpooler's destination
        if haversine(destination_lat, destination_lon, carpooler_route[-1][0], carpooler_route[-1][1]) <= max_radius_km:
            matching_users.append(user)

# Print the matching users
print("Matching Users: ")
for user in matching_users:
    print(f"Name: {user['name']}, Start Location: {user['start_location']}, Destination: {user['destination']}")
