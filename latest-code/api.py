from django.shortcuts import redirect
from flask import Flask, request, jsonify, make_response, send_from_directory, send_file, render_template, url_for
import os
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/login')
def login():
    print("Hi")
    return render_template('login.html')

@app.route('/blog')
def blog():
    print("Hi")
    return render_template('blog.html')

@app.route('/showSignUp')
def showSignUP():
    return render_template('login.html')

@app.route('/result')
def result():
    return render_template('resultDeveloper.html')

@app.route('/signup', methods = ['POST', 'GET'])
def signup():

    _name = request.form.get("username")
    _email = request.form.get("email")
    _password = request.form.get("password")
    data = request.data
    print(data)
    if _name and _email and _password:
        print(_name)
        render_template('login.html')

    return render_template('login.html')


    # if _name and _email and _password:
    #     return redirect(url_for('home'))


@app.route('/loggedIn', methods = ['POST', 'GET'])
def loggedIn():
    _name = request.form.get("inputName")
    if(_name):
        if(_name == "sarthak@slack.com"):
            return render_template('resultDeveloper.html')
    return render_template('blog.html')



if __name__ == "__main__":
    app.run(debug=True)