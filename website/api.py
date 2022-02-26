from flask import Flask, request, jsonify, make_response, send_from_directory, send_file, render_template, url_for
import os
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/api/login', methods=['POST'])
def login():

    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)