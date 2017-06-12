from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/table')
def table():
    return render_template('table.html',
    atten = [{'name': 'LSD768921'}, {'name': 'LSD768969'}, {'name': 'LSD768978'}],
    shifter = [{'name': 'LSP768935'}, {'name': 'LSP768911'}, {'name': 'LSP768789'}])


@app.route('/chart')
def chart():
    return render_template('chart.html')


@app.route('/send_data')
def send_data():
    return render_template('send_data.html')

@app.route('/table', methods=['GET', 'POST'])
def get_element_from_list():
    module = request.form.get('select_module')
    return(str(module))

# @app.route('/send_data', methods=['GET', 'POST'])
# def upload_data_file():
#     if request.method == 'POST':
#         data_file = request.files['File']
#         data_file.save()

# @app.route('/test')


if __name__ == '__main__':
    app.run()
