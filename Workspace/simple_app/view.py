from flask import Flask, render_template, Markup
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/table')
def table():
    return render_template('table.html')


@app.route('/chart')
def chart():
    return render_template('chart.html')


@app.route('/help')
def help():
    return render_template('help.html')


@app.route('/load_data')
def load_data():
    return render_template('load_data.html')


@app.route('/send_data')
def send_data():
    return render_template('send_data.html')


if __name__ == '__main__':
    app.run()
