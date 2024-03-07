from flask import Flask

# Create a Flask app
app = Flask(__name__)


# Define the home page
@app.route('/')
def home():
    return  "<h1>Stock Dashboard</h1>"


if __name__ == '__main__':
    app.run(debug=True)