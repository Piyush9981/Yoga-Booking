from flask import Flask, request, render_template

app = Flask(__name__)

event_data = [
    {"id": 1, "title": "Benifits Of Yoga", "price": 299 },
    {"id": 2, "title": "Best Practices", "price": 299 },
    {"id": 3, "title": "Yoga Precautions", "price": 299 },
    {"id": 4, "title": "Benifits Of Yoga", "price": 399 },
    {"id": 5, "title": "Best Practices", "price": 399 },
    {"id": 6, "title": "Yoga Precautions", "price": 399 }
 ]

user_profile = []

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/signup")
def signup():
    return render_template("signup.html")

@app.route("/events")
def events():
    return render_template("events.html")

@app.route("/loginsubmit", methods=["POST"])
def loginsubmit():
    email = request.form.get('email')
    password = request.form.get('pass')
    print(email,password)
    return render_template('index.html')

@app.route("/signupsubmit", methods=["POST"])
def signupsubmit():
    name = request.form.get('name')
    email = request.form.get('email')
    password = request.form.get('pass')
    confirmpassword = request.form.get('confirmpass')
    if password == confirmpassword and len(password) >= 8:
        user_profile.append({
            "name": name, 
            "email": email, 
            "pass":password
        })
        return render_template('index.html')
    else:
        return render_template('signup.html')
    

@app.route("/book/<int:event_id>")
def bookingform(event_id):
    event = next((eve for eve in event_data if eve["id"] == event_id), None)
    return render_template("booking-form.html", event=event)

app.run(debug=True)