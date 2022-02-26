from flask import Flask, request, json, make_response, send_from_directory, send_file, render_template, url_for
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
    return render_template('login.html')

@app.route('/showSignUp')
def showSignUp():
    return render_template('login.html')


@app.route('/signup', methods = ['POST', 'GET'])
def signup():

    data = request.data
    _name = request.form.get("inputName")
    _email = request.form.get("email")
    _password = request.form.get("password")
    if _name and _email and _password:
        print(_name)
        print(_email)
        print(_password)

    return render_template('login.html')


    # if _name and _email and _password:
    #     return redirect(url_for('home'))



if __name__ == "__main__":
    app.run(debug=True)
