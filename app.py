from flask import Flask, render_template, request
import webbrowser
from flask import Flask, jsonify, render_template, request, redirect, url_for, session
from modeling import build_model
import sqlite3

app = Flask(__name__)

app.secret_key = 'secret_key'
db_name = 'users.db'

API_KEY="AIzaSyC0E2-VFWnUjcoN63GjKLE-QZI94kcjEaU"
@app.route("/")
def index():
    return render_template("home.html")


def init_db():
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                 username TEXT NOT NULL,
                 email TEXT NOT NULL UNIQUE,
                 password TEXT NOT NULL,
                 points INTEGER)''')
    conn.commit()
    conn.close()


init_db()

@app.route("/home")
def home():
    return render_template("index.html")

# Signup route
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        # Check if the email already exists in the database
        conn = sqlite3.connect(db_name)
        c = conn.cursor()
        c.execute("SELECT * FROM users WHERE email=?", (email,))
        user = c.fetchone()
        conn.close()

        if user:
            error = 'This email address is already registered. Please choose another one.'
            return render_template('signup.html', error=error)
        elif password != confirm_password:
            error = 'The passwords you entered do not match. Please try again.'
            return render_template('signup.html', error=error)
        else:
            # Add the user to the database
            conn = sqlite3.connect(db_name)
            c = conn.cursor()
            c.execute("INSERT INTO users (username, email, password, points) VALUES (?, ?, ?, ?)", (username, email, password, 0))
            conn.commit()
            conn.close()
            return redirect(url_for('login'))
    else:
        return render_template('signup.html')


# Login route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        # Check if the email and password match a user in the database
        conn = sqlite3.connect(db_name)
        c = conn.cursor()
        c.execute("SELECT * FROM users WHERE email=? AND password=?", (email, password))
        user = c.fetchone()
        conn.close()

        if user:
            session['user_id'] = user[0]
            session['progress'] = user[4]
            return render_template('index.html')
        else:
            error = 'Incorrect email or password. Please try again.'
            return render_template('login.html', error=error)

    else:
        return render_template('login.html')


@app.route("/submit", methods=["GET"])
def submit():
    origin = request.args.get("origin")
    destination = request.args.get("destination")
    mode = request.args.get("mode")
    d = {
        'noida_visakhaptanam': [        ['Dankaur', 'Jewar', 'Morena', 'Gwalior', 'Jhansi', 'sagar', 'Lakhnadon', 'Balaghat', 'Jeypore'],
            ['Dankaur', 'Jewar', 'Morena', 'Gwalior', 'Jhansi', 'sagar', 'Mandla', 'Nowrangpur', 'Araku Valley']
        ],
        'delhi_vizag': [        ['Agra', 'Gwalior', 'Jagdal Pur'],
            ['Jhansi', 'Chhatarpur', 'Panna'],
            ['Lalitpur', 'Lakhnadon', 'Bastar']
        ],
        'vizag_hyderabad': [        ['Rajamundry', 'Eluru', 'Suryapet'],
            ['Annavaram', 'Koyyalgudam', 'Katangur']
        ],
        'hyderabad_bangalore': [        ['Shadnagar', 'Mahbubnagar', 'Anantapur', 'Bagepalli'],
            ['Kurnool', 'Noonepalli', 'Mydukur', 'Kadapa']
        ],
        'chennai_mumbai': [        ['Gudur', 'Rapur', 'Cholapur'],
            ['Nellore', 'Hyderabad', 'Pune']
        ],
        'vizag_kolkata': [        ['Srikakulam', 'cuttak', 'Alampur'],
            ['Palasa', 'Deogarh', 'Kharaghpur']
        ],
        'delhi_jammu': [        ['Panipat', 'Dasuir', 'Vijaypur'],
            ['Hansi', 'Batala', 'Sujanpur']
        ],
        'jaipur_haryana': [        ['Daunatpura', 'Beelapur', 'Shivpuri'],
            ['Jaipur', 'Haryana', 'Shahpura', 'Mundhal', 'Sorkhi']
        ],
        'hyderabad_bangalore': [        ['Mahbubnagar', 'Kurnool', 'Anantapur', 'Bagepalli'],
            ['Mahbubnagar', 'Kurnool', 'Nandyala', 'Kadapa']
        ],
        'hyderabad_mumbai': [        ['Miyapur', 'Solapur', 'Indapur', 'Pune'],
            ['Chittapur', 'Kalaburagi', 'juer', 'Daund', 'Thane']
        ]
    }

    key = f"{origin}_{destination}"

    # Predict routes for each intermediate location list in the value data
    predicted_outputs = []
    for intermediate_locations in d.get(key, []):
        high_count = 0
        for i in intermediate_locations:
            if build_model(i) == "high":
                high_count += 1
        predicted_output = build_model(i)
        predicted_outputs.append(high_count)

    if(len(predicted_outputs) > 0):  
        # Find the maximum observed value across all predicted outputs
        # Assuming predicted_outputs is a list of numbers
        min_value = min(predicted_outputs)
        route = predicted_outputs.index(min_value)+1
        print("Min value:", min_value)
        print("optimal route :", route)
    else:
        route=1

    url = f"https://www.google.com/maps/dir/?api=1&origin={origin}&destination={destination}&travelmode={mode}&key={API_KEY}"
    return f"""
            <!DOCTYPE html>
            <html>
            <head>
                <meta charset="utf-8" />
                <title>Optimized Route</title>
                <link rel="stylesheet" type="text/css" href="{{ url_for('static', filename='style.css') }}">    
            </head>
            <body>
                <h1>Real-time Alert</h1>
                <h2>The optimized route selected by AI:</h2>
                <div id="route-container">
                <h3>Route { route }</h3>
                </div>

                <script src="https://cdn.jsdelivr.net/npm/sweetalert2@10"></script>
                <script>
                    window.open('{url}', '_blank');
                    window.alert('Optimal Route: {route}');
                    window.close();
                </script>
            </body>
        </html>
    """

if __name__ == "__main__":
    app.run(port=8000,debug=True)
