from flask import Flask, redirect, render_template, url_for, Blueprint
from datetime import timedelta
from flask import request, session, jsonify
import mysql.connector

assignment3_1 = Blueprint(
    'assignment3_1',
    __name__,
    static_folder='static',
    static_url_path='/pages/assignment3_1',
    template_folder='templates')


@assignment3_1.route('/assignment3_1')
def about_page_func():
    user_info = {'name': 'Ragnar', 'second name': 'Lothbrok', 'nickname': 'Viking'}
    preferences_in_music = ('Hip-hop', 'Mainstream', 'Classical', 'Jazz', 'Jamaican')
    hobbies = ('dancing', 'baking', 'Kangoo jump', 'sap')
    return render_template('assignment3_1.html',
                           user_info=user_info,
                           preferences_in_music=preferences_in_music,
                           hobbies=hobbies)
