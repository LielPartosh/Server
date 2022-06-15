from flask import Flask, redirect, render_template, url_for
from datetime import timedelta
from flask import request, session, jsonify
import mysql.connector

app = Flask(__name__)

app.secret_key = '123'
app.config['SESSION_PERMANENT'] = True
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=30)


@app.route('/home')
def homepage_func():
    return render_template('HomePage.html')


@app.route('/')
def redirect_homepage_func():
    return redirect(url_for('homepage_func'))


@app.route('/contactUs')
def contactus_func():
    return render_template('contactUs.html')


@app.route('/about')
def about_page_func():
    user_info = {'name': 'Ragnar', 'second name': 'Lothbrok', 'nickname': 'Viking'}
    preferences_in_music = ('Hip-hop', 'Mainstream', 'Classical', 'Jazz', 'Jamaican')
    hobbies = ('dancing', 'baking', 'Kangoo jump', 'sap')
    return render_template('assignment3_1.html',
                           user_info=user_info,
                           preferences_in_music=preferences_in_music,
                           hobbies=hobbies)


@app.route('/Registration-Search', methods=['GET', 'POST'])
def registration_search_func():
    if request.method == 'GET':
        if 'UsernameSearch' in request.args:
            username = request.args['UsernameSearch']
            if username in user_dictionary:
                return render_template('assignment3_2.html',
                                       Username=username,
                                       Email=user_dictionary[username][0],
                                       PhoneNumber=user_dictionary[username][1])
            if len(username)==0:
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


@app.route('/log_out')
def logout_func():
    session['was registered'] = False
    session.clear()
    return redirect(url_for('registration_search_func'))


@app.route('/session')
def session_func():
    return jsonify(dict(session))


user_dictionary = {
    'RagnarLot': ['Rag@gmail.com', '0526334075'],
    'JessicaAlba': ['Jessi@gmail,com', '054378256'],
    'Beyonce': ['QueenB@gmail.com', '050783542'],
    'GeraldButler': ['Gery@gmail.com', '052356478'],
    'GreenDay': ['Green@gmail.com', '0544893261'],
    'NoaKirel': ['NoaK@gmail.com', '0525364789'],
    'AngelinaJolie': ['angle@gmail.com', '0544893361']

}

if __name__ == '__main__':
    app.run(debug=True)
