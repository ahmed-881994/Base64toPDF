from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from argparse import ArgumentParser
import os
import traceback
from lib import base64_to_pdf

app = Flask(__name__)
CORS(app)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.route('/')
def home():
    cleanup()
    return render_template('index.html')


@app.route('/local/decode', methods=['POST'])
def decode():
    data = request.form.to_dict()['request']
    try:
        base64_to_pdf.decode(data)
    except Exception as e:
        traceback.print_exc(chain=False)
        return jsonify({"error": e.args[0]})
    else:
        return jsonify({'response': "Success"})


def cleanup():
    if os.path.exists("static/result/document.pdf"):
        os.remove("static/result/document.pdf")


## Main ##
if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('-p', '--port', type=int, default=5000)
    args = parser.parse_args()
    port = args.port
    app.run(host='0.0.0.0', port=port)
