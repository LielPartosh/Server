from flask import Flask, redirect, render_template, url_for, Blueprint
from datetime import timedelta
from flask import request, session, jsonify
import mysql.connector
import requests

assignment4 = Blueprint(
    'assignment4',
    __name__,
    static_folder='static',
    static_url_path='/pages/assignment4',
    template_folder='templates')


# ------------- DATABASE CONNECTION --------------- #
def interact_db(query, query_type: str):
    return_value = False
    connection = mysql.connector.connect(host='localhost',
                                         user='root',
                                         passwd='root',
                                         database='myflaskdb')
    cursor = connection.cursor(named_tuple=True)
    cursor.execute(query)
    #

    if query_type == 'commit':
        # Use for INSERT, UPDATE, DELETE statements.
        # Returns: The number of rows affected by the query (a non-negative int).
        connection.commit()
        return_value = True

    if query_type == 'fetch':
        # Use for SELECT statement.
        # Returns: False if the query failed, or the result of the query if it succeeded.
        query_result = cursor.fetchall()
        return_value = query_result

    connection.close()
    cursor.close()
    return return_value


# ------------------- SELECT ---------------------- #

@assignment4.route('/assignment4')
def assignment4_func():
    query = 'select * from users'
    users_list = interact_db(query, query_type='fetch')
    return render_template('assignment4.html', users=users_list)


# -------------------- INSERT --------------------- #

@assignment4.route('/insert_user', methods=['POST'])
def insert_user_func():
    username = request.form['username']
    email = request.form['email']
    phone_number = request.form['phone_number']
    query = 'select * from users'
    users = interact_db(query, query_type='fetch')

    counter = 0
    for user in users:
        if (username == user.username):
            counter += 1

    if counter == 1:
        return render_template('assignment4.html',
                                users=users,
                                message1='User already exists.')

    if counter == 0:
        query = "INSERT INTO users(username, email, phone_number) VALUES ('%s', '%s', '%s')" % (username, email, phone_number)
        interact_db(query=query, query_type='commit')
        query = 'select * from users'
        users1 = interact_db(query, query_type='fetch')
        return render_template('assignment4.html',
                                users=users1,
                                message1='The user has been inserted successfully!')


# -------------------- UPDATE --------------------- #

@assignment4.route('/update_user', methods=['POST'])
def update_user_func():
    username = request.form['username']
    email = request.form['email']
    phone_number = request.form['phone_number']
    query = 'select * from users'
    users = interact_db(query, query_type='fetch')

    counter = 0
    for user in users:
        if (username == user.username):
            counter+=1

    if counter==0:
        return render_template('assignment4.html',
                               users=users,
                               message3='User not found.')

    if counter == 1:
        query = "UPDATE users "\
                "SET email='%s', phone_number='%s'"\
                "WHERE username='%s';" %(email, phone_number, username)
        interact_db(query=query, query_type='commit')
        query = 'select * from users'
        users1 = interact_db(query, query_type='fetch')
        return render_template('assignment4.html',
                               users=users1,
                               message3='The user details has been updated successfully!')


# -------------------- DELETE --------------------- #

@assignment4.route('/delete_user', methods=['POST'])
def delete_user_func():
    username = request.form['username']
    query = 'select * from users'
    users = interact_db(query, query_type='fetch')

    counter = 0
    for user in users:
        if (username == user.username):
           counter+=1

    if counter == 0:
        return render_template('assignment4.html',
                               users=users,
                               message2='User not found.')

    if counter == 1:
        query = "DELETE FROM users WHERE username='%s';" % username
        interact_db(query, query_type='commit')
        query = 'select * from users'
        users1 = interact_db(query, query_type='fetch')
        return render_template('assignment4.html',
                               users=users1,
                               message2='The user has been deleted successfully!')


# -------------------- PART B --------------------- #
@assignment4.route('/assignment4/users')
def assignment4_json_func():
    query = 'select * from users'
    users_list = interact_db(query, query_type='fetch')
    listdict = []
    for i in users_list:
        tempdict = {'email': i[0], 'phone_number': i[1], 'username': i[2]}
        listdict.append(tempdict)
    return jsonify(listdict)


@assignment4.route('/assignment4/outer_source')
def get_user_from_outer_source():
    user_id = request.args['user_id']
    response = requests.get(url=f"https://reqres.in/api/users/{user_id}")
    user = response.json()
    session['user'] = user.get('data')
    return redirect(url_for('assignment4.assignment4_func'))


# -------------------- PART C --------------------- #

def check_if_int(string):
    try:
        int(string)
        return True
    except ValueError:
        return False


@assignment4.route('/assignment4/restapi_users', defaults={'USER_ID': 3}, methods=['GET'])
@assignment4.route('/assignment4/restapi_users/<USER_ID>', methods=['GET'])
def get_restapi_users(USER_ID):
    if check_if_int(USER_ID):
        response = requests.get(url=f"https://reqres.in/api/users/{USER_ID}")
        if response.status_code is 200:
            users = response.json()
            return users.get('data')
        else:
            message = "User doesn't exist"
            return jsonify(message)
    else:
        message = "Insert integer please "
        return jsonify(message)

