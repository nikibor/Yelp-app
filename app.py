from flask import Flask
from flask import render_template
from flask import request

import json

import requests as http_requests

app = Flask(__name__)
app.config.from_object('config')



@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/analyse', methods=['POST'])
def test():
    review = request.form['review']
    model = request.form['model']

    data = json.dumps({'text': str(review), 'token': "test"})
    # cnn_response = http_requests.post(url='https://yelp-classification-service.herokuapp.com/api/cnn', json=data)
    if model == 'CNN':
        model_response = http_requests.post(url='http://127.0.0.1:5001/api/cnn', json=data)
    elif model == 'RNN':
        model_response = http_requests.post(url='http://127.0.0.1:5001/api/rnn', json=data)
    elif model == 'Xgboost':
        model_response = http_requests.post(url='http://127.0.0.1:5001/api/xgb', json=data)
    elif model == 'Linreg':
        model_response = http_requests.post(url='http://127.0.0.1:5001/api/lin', json=data)

    return model_response.text


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
