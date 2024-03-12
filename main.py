from flask import Flask
print("Starting the app")

app = Flask(__name__)

@app.route('/')
def index():
    return "Welcome to Clean Social Network!!!"

app.run(host='0.0.0.0', port=81)