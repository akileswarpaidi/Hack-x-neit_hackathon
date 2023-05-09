import pandas as pd
import random

# Define the number of rows to generate
n_rows = 100000

# Define the possible values for each attribute
places = ["Dankaur", "Jewar", "Morena", "Gwalior", "Jhansi", "Sagar","Lakhnadon", "Balaghat", "Jeypore", "Mandla","Nowrangpur", "Araku Valley","Agra", "Gwalior", "Jagdal Pur", "Jhansi",
"Chhatarpur", "Panna", "Lalitpur", "Lakhnadon","Bastar", "Rajamundry", "Eluru", "Suryapet",
"Annavaram", "Koyyalgudam", "Katangur", "Shadnagar","Mahbubnagar", "Anantapur", "Kurnool", "Noonepalli","Mydukur", "Gudur", "Rapur", "Cholapur","Nellore", "Hyderabad", "Pune", "Srikakulam","Cuttack", "Alampur", "Palasa", "Deogarh","Kharagpur", "Panipat", "Dasuapara", "Vijaypur","Hansi", "Batala", "Sujanpur", "Daunatpura","Beelapur", "Shivpuri", "Jaipur", "Haryana","Shahpura", "Mundhal", "Sorkhi", "Mahbubnagar","Kurnool", "Anantapur", "Bagepalli", "Nandyala","Kadapa", "Miyapur", "Solapur", "Indapur","Pune", "Chittapur", "Kalaburagi",
"Jeur", "Daund", "Thane"]

weathers = ['sunny', 'cloudy', 'rainy', 'snowy']
events = ['none', 'accident', 'construction']
road_qualities = ['poor', 'fair', 'good']
traffic_levels = ['low', 'high']

# Define the conditions for the traffic level
def get_traffic_level(num_vehicles, speed):
    if num_vehicles < 30 and speed < 50:
        return 'high'
    elif num_vehicles < 50:
        return 'low'
    elif num_vehicles >= 50 and speed > 70:
        return 'low'
    elif num_vehicles >= 50 and speed <= 70:
        return 'high'
    else:
        return 'low'

# Generate the data
data = []
for i in range(n_rows):
    place = random.choice(places)
    weather = random.choice(weathers)
    num_vehicles = random.randint(10, 100)
    speed = random.randint(30, 100)
    event = random.choice(events)
    road_quality = random.choice(road_qualities)
    traffic_level = get_traffic_level(num_vehicles, speed)
    row = [i+1, place, weather, num_vehicles, speed, event, road_quality, traffic_level]
    data.append(row)

# Convert the data to a pandas DataFrame
df = pd.DataFrame(data, columns=['id', 'Place', 'Weather', 'Number of vehicles', 'Speed of vehicles', 'Events', 'Road Quality', 'Traffic'])

# Save the data to a CSV file
df.to_csv('data.csv', index=False)
