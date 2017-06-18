from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from wtforms import Form, StringField, IntegerField

app = Flask(__name__)
Bootstrap(app)

class Modules:
    atten_list = [{'name':'LSP768935', "value": 45}, {'name':'LSP768911', "value": 43}, {'name':'LSP768789',"value": 41}
        , {'name': 'LSP768453',"value": 37}, {'name':'LSP768754', "value": 26}]
    shifter_list= [ {'name':'LSD768921'},{'name':'LSD768969'}, {'name':'LSD768978'}
        , {'name': 'LSD76678'}, {'name':'LSD768789'}]


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html' )


@app.route('/table')
def table():
    return render_template('table.html', atten = Modules.atten_list, shifter = Modules.shifter_list)


@app.route('/chart')
def chart():
    return render_template('chart.html')

@app.route('/get_atten', methods=['GET', 'POST'])
def get_atten():
    atten = request.form.get('atten_get')
    return(str(atten))

@app.route('/get_shifter', methods=['GET', 'POST'])
def get_shifter():
    shifter = request.form.get('shifter_get')
    return(str(shifter))

@app.route('/get_atten/<string:name>')
def get_value(name):
    return None


if __name__ == '__main__':
    app.run(debug=True)
