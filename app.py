from flask import Flask, redirect, render_template, url_for, Blueprint
from datetime import timedelta
from flask import request, session, jsonify
import mysql.connector

from pages.HomePage.HomePage import HomePage
from pages.contactUs.contactUs import contactUs
from pages.assignment3_1.assignment3_1 import assignment3_1
from pages.assignment3_2.assignment3_2 import assignment3_2
from pages.assignment4.assignment4 import assignment4


app = Flask(__name__)

app.register_blueprint(HomePage)
app.register_blueprint(contactUs)
app.register_blueprint(assignment3_1)
app.register_blueprint(assignment3_2)
app.register_blueprint(assignment4)


app.secret_key = '123'
app.config['SESSION_PERMANENT'] = True
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=30)


if __name__ == '__main__':
    app.run(debug=True)
