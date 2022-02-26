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

@app.route('/login')
def login():
    print("Hi")
    return render_template('login.html')

@app.route('/showSignUp')
def showSignUP():
    return render_template('login.html')


@app.route('/signup', methods = ['POST', 'GET'])
def signUp(): 
    print("YES")
    _name = request.form.get('Username')
    _email = request.form.get('Email')
    _password = request.form.get('Password')
    print(_name)
    return render_template('login.html')


    # if _name and _email and _password:
    #     return redirect(url_for('home'))



if __name__ == "__main__":
    app.run(debug=True)