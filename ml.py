import requests
import json

# Set up the API request
api_key = 'YOUR_API_KEY'
origin = 'New York, NY'
destination = 'Los Angeles, CA'
url = f'https://maps.googleapis.com/maps/api/directions/json?origin={origin}&destination={destination}&key={api_key}'

# Get the directions response and extract the routes
response = requests.get(url)
routes = json.loads(response.text)['routes']

# Loop through each route and print the intermediate places
for i, route in enumerate(routes):
    print(f'Route {i+1}:')
    legs = route['legs']
    for leg in legs:
        steps = leg['steps']
        for j, step in enumerate(steps):
            if j == 0:
                print(f"Start at {step['start_location']['lat']},{step['start_location']['lng']}")
            elif j == len(steps) - 1:
                print(f"End at {step['end_location']['lat']},{step['end_location']['lng']}")
            else:
                print(f"Intermediate place at {step['end_location']['lat']},{step['end_location']['lng']}")
    print('\n')
