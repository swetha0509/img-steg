from flask import Flask, render_template, request, send_file, jsonify, redirect, url_for, session
from PIL import Image
import os
import io
import base64
import json
from predict import generate_key
from encryption import encrypt_text
from encoder import encode
from decryption import decrypt_text
from decoder import decode

app = Flask(__name__)
app.secret_key = '641241e2aa187610d0b91e3b91373303'
app.config['UPLOAD_FOLDER'] = 'uploads'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/encoder', methods=['GET', 'POST'])
def encoder():
    if request.method == 'POST':
        # Get the file from the request data
        file = request.files['image']
        text = request.form['text']

        # Do something with the file, for example process it and get the results
        results = generate_key(file)
        results = results[2:]
        session['key'] = results
        print(session['key'])
        key = bytes.fromhex(results)
        results = encrypt_text(text, key)
        path = encode(file, results)

        # Render the encoder template with the results
        return render_template('encoder.html', results=path)
    else:
        # If the request is a GET request, render the encoder template
        return render_template('encoder.html')

@app.route('/decoder', methods=['POST', 'GET'])
def decoder():
    if request.method == 'POST':
        print(1)
        file = request.files['image']
        print(2)
        data = decode(file)
        print(3)
        key = session.get('key')
        print(4)
        print(data)
        print(key)
        data = decrypt_text(data, key)
        print(5)
        return render_template('decoder.html', results = data)
    else:
        return render_template('decoder.html')



@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    file.save(os.path.join('uploads', file.filename))
    image = Image.open(os.path.join('uploads', file.filename))
    # Process the image here
    # ...
    return render_template('result.html', filename=file.filename)

if __name__ == '__main__':
    app.run(debug=True)
