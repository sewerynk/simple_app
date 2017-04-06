from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_appbuilder.charts.views import DirectByChartView
from flask_appbuilder.models.sqla.interface import SQLAInterface

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


class CountryStats(Model):
    id = Column(Integer, primary_key=True)
    stat_date = Column(Date, nullable=True)
    population = Column(Float)
    unemployed_perc = Column(Float)
    poor_perc = Column(Float)
    college = Column(Float)


class CountryDirectChartView(DirectByChartView):
    datamodel = SQLAInterface(CountryStats)


if __name__ == '__main__':
    app.run()
