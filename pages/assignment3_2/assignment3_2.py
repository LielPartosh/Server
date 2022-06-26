from flask import Flask, redirect, render_template, url_for, Blueprint
from datetime import timedelta
from flask import request, session, jsonify
import mysql.connector

assignment3_2 = Blueprint(
    'assignment3_2',
    __name__,
    static_folder='static',
    static_url_path='/pages/assignment3_2',
    template_folder='templates')


@assignment3_2.route('/assignment3_2', methods=['GET', 'POST'])
def registration_search_func():
    if request.method == 'GET':
        if 'UsernameSearch' in request.args:
            username = request.args['UsernameSearch']
            if username in user_dictionary:
                return render_template('assignment3_2.html',
                                       Username=username,
                                       Email=user_dictionary[username][0],
                                       PhoneNumber=user_dictionary[username][1])
            if len(username) == 0:
                return render_template('assignment3_2.html',
                                       user_dictionary=user_dictionary)

            else:
                return render_template('assignment3_2.html',
                                       message='User not found.')

    if request.method == 'POST':
        username = request.form['UsernameRegistration']
        email = request.form['Email']
        phonenumber = request.form['PhoneNumber']

        session['UsernameRegistration'] = username
        session['Email'] = email
        session['PhoneNumber'] = phonenumber
        session['was registered'] = True

        return render_template('assignment3_2.html')

    return render_template('assignment3_2.html')


@assignment3_2.route('/log_out')
def logout_func():
    session['was registered'] = False
    session.clear()
    return redirect(url_for('assignment3_2.registration_search_func'))


@assignment3_2.route('/session')
def session_func():
    return jsonify(dict(session))


user_dictionary = {
    'RagnarLot': ['Rag@gmail.com', '0526334075'],
    'JessicaAlba': ['Jessi@gmail.com', '0543782560'],
    'Beyonce': ['QueenB@gmail.com', '0507835421'],
    'GeraldButler': ['Gery@gmail.com', '0523564781'],
    'GreenDay': ['Green@gmail.com', '0544893261'],
    'NoaKirel': ['NoaK@gmail.com', '0525364789'],
    'AngelinaJolie': ['angle@gmail.com', '0544893361']

}

