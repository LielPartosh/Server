from flask import Flask, redirect, render_template, url_for, Blueprint
from datetime import timedelta
from flask import request, session, jsonify
import mysql.connector

contactUs = Blueprint(
    'contactUs',
    __name__,
    static_folder='static',
    static_url_path='/pages/contactUs',
    template_folder='templates')


@contactUs.route('/contactUs')
def contactus_func():
    return render_template('contactUs.html')



