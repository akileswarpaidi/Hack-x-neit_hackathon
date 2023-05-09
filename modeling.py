import pandas as pd
# import mysql.connector
import random
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder
from weather import weather_s
def build_model(city):
    # Load the data from a CSV file
    data = pd.read_csv('data.csv')

    # Define the features and target
    features = ['Number of vehicles', 'Speed of vehicles', 'Weather']
    target = 'Traffic'

    # Encode the 'Weather' feature
    le = LabelEncoder()
    data['Weather'] = le.fit_transform(data['Weather'])
    
    num_vehicles = random.randint(10, 80)
    speed_vehicles = random.randint(10, 80)
    # Define the conditions for the decision tree
    conditions = [
        data['Number of vehicles'] < 30,
        (data['Number of vehicles'] >= 30) & (data['Number of vehicles'] < 50),
        data['Number of vehicles'] >= 50,
        data['Speed of vehicles'] < 50,
        (data['Speed of vehicles'] >= 50) & (data['Speed of vehicles'] < 70),
        data['Speed of vehicles'] >= 70,
        ((data['Speed of vehicles'] < 50) & (data['Number of vehicles'] < 30)),
        data['Weather'] == 0,  # rainy
        data['Weather'] == 1,  # sunny
        data['Weather'] == 2   # cloudy
    ]

    # Define the predicted traffic levels for each condition
    predictions = ['High Traffic', 'Low Traffic', 'High Traffic', 'High Traffic', 'Moderate Traffic', 'Low Traffic', 'High Traffic',
                   'Low Traffic', 'Moderate Traffic', 'High Traffic']

    # Build the decision tree classifier
    clf = DecisionTreeClassifier()
    clf.fit(data[features], data[target])

    # Test the accuracy of the classifier
    X_train, X_test, y_train, y_test = train_test_split(data[features], data[target], test_size=0.2, random_state=0)
    y_pred = clf.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    # print('Accuracy:', accuracy)
    k=(weather_s(city))
    l=[]
    l.append(k)
        # Make predictions on new data

    # mydb = mysql.connector.connect(
    # host="localhost",
    # user="username",
    # password="password",
    # database="adarsh"
    # )

    # Create a cursor to execute queries
    # mycursor = mydb.cursor()

    # Retrieve the data from the 'photos' table

    # mycursor.execute("SELECT `Number of vehicles`, `Speed of vehicles` FROM data")
    new_data = pd.DataFrame({
            'Number of vehicles': [num_vehicles],
            'Speed of vehicles': [speed_vehicles],
            'Weather': l
    })
    print(num_vehicles, speed_vehicles,l)
    # Encode the 'Weather' feature for new data
    new_data['Weather'] = le.transform(new_data['Weather'])

    predictions = clf.predict(new_data[features])
    print('Predictions:', predictions)
    # return predictions
build_model("delhi")
