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
    return render_template('table.html')


@app.route('/chart')
def chart():
    return render_template('chart.html')


@app.route('/send_data')
def send_data():
    return render_template('send_data.html')

@app.route('/get_atten', methods=['GET', 'POST'])
def get_atten():
    atten_list = ['LSP768935', 'LSP768911', 'LSP768789']
    return render_template('table.html', atten = atten_list)

@app.route('/get_shifter', methods=['GET', 'POST'])
def get_shifter():
    shifter_list = ['LSD768921', 'LSD768969', 'LSD768978']
    return render_template('table.html', shifter=shifter_list)

@app.route('/process', methods=['GET', 'POST'])
def process():
    name = request.formdata

# @app.route('/', methods=['GET', 'POST'])
# def get_the_frequency():
#     freq = request.form.
# @app.route('/send_data', methods=['GET', 'POST'])
# def upload_data_file():
#     if request.method == 'POST':
#         data_file = request.files['File']
#         data_file.save()

# @app.route('/test')


if __name__ == '__main__':
    app.run()
