from flask import Flask, render_template, request, jsonify
import os
import traceback
from lib import base64_to_pdf

app = Flask(__name__)

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
    return render_template('index.html')

@app.route('/local/decode', methods = ['POST'])
def decode():
    data = request.form.to_dict()['request']
    try:
        base64_to_pdf.decode(data)
    except Exception as e:
        traceback.print_exc(chain=False)
        return jsonify({"error": repr(e)})
    else:
        return jsonify({'response': "Success"})

## Main ##
if __name__ == '__main__':

    port = int(os.getenv('PORT', 8080))
    app.run(host='0.0.0.0', port=port)