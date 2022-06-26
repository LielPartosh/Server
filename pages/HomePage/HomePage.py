from flask import redirect, render_template, url_for, Blueprint
from datetime import timedelta
from flask import request, session, jsonify
import mysql.connector


HomePage = Blueprint(
    'HomePage',
    __name__,
    static_folder='static',
    static_url_path='/pages/HomePage',
    template_folder='templates')


@HomePage.route('/HomePage')
def homepage_func():
    return render_template('HomePage.html')


@HomePage.route('/')
def redirect_homepage_func():
    return redirect(url_for('HomePage.homepage_func'))



