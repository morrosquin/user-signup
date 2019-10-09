from flask import Flask, request, redirect, render_template
import cgi
import os

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return render_template('homepage.html')

@app.route("/homepage", methods=['POST'])
def validate():
    username = request.form['username']
    password = request.form['password']
    verify = request.form['verify']
    email = request.form['email']

    username_error = ''
    password_error = ''
    verify_error = ''
    email_error = ''

    if int(len(username)) <= 0:
        username_error = 'Thats not a valid username'
        username = ''
    else:
        if int(len(username)) < 3 or int(len(username)) > 20:
            username_error = 'Thats not a valid username'
            username = ''  

    if int(len(password)) <= 0:
        password_error = 'Thats not a valid password'
        password = ''
    else:
        if int(len(password)) < 3 or int(len(password)) > 20:
            password_error = 'Thats not a valid password'
            password = ''

    if int(len(verify)) <= 0:
        verify_error = 'Password do not match'
        verify = ''
    else:
        if password != verify:
            verify_error = 'Password do not match'
            verify = ''  
    
    if int(len(email)) > 0:
        if "@" not in email and "." not in email and " " not in email:
            email_error = 'Thats not a valid email'
            email = ''
        elif int(len(email)) < 3 or int(len(password)) > 20:
            email_error = 'Thats not a valid email'
            email = ''

    if not username_error and not password_error and not verify_error and not email_error:
        username = str(username)
        return redirect('/welcome_page?username={0}'.format(username))
    else:
        return render_template('homepage.html', username_error=username_error, password_error=password_error, 
        verify_error=verify_error, email_error=email_error, username=username, password=password, verify=verify, email=email)

@app.route("/welcome_page")
def welcome():
    username = request.args.get('username')
    return render_template('welcome_page.html', username = username)

app.run()