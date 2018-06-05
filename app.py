from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)
app.config.from_object('config')



@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/test', methods=['POST'])
def test():
    review = request.form['review']
    model = request.form['model']
    return str(request.form['review'] + request.form['model'])


if __name__ == '__main__':
    app.run()
