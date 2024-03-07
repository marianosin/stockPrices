from aplication import app
from flask import render_template



# Define the home page
@app.route('/')
def home():
    return  render_template('index.html', title = 'Index page')

@app.route('/layout')
def layout():
    return  render_template('layout.html')